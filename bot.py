from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

import os
from dotenv import load_dotenv, dotenv_values

ENV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
env = dotenv_values(ENV_FILE)

TOKEN = env.get("BOT_TOKEN")

# Social media links
TELEGRAM_LINK = "https://t.me/ammieljewelry"
INSTAGRAM_LINK = "https://www.instagram.com/tesfalesion?stkn=dzBkd3E3emJsN3F3"
FACEBOOK_LINK = "https://www.facebook.com/profile.php?id=61574100142725"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛍️ Browse Bracelets", callback_data="browse")],
        [InlineKeyboardButton("🎨 Designs & Colors", callback_data="designs")],
        [InlineKeyboardButton("💰 Prices", callback_data="prices")],
        [InlineKeyboardButton("📦 Place an Order", callback_data="order")],
        [InlineKeyboardButton("📍 Pickup & Delivery", callback_data="delivery")],
        [InlineKeyboardButton("📱 Follow Us", callback_data="social")],
        [InlineKeyboardButton("💬 Contact Us", callback_data="contact")],
        [InlineKeyboardButton("ℹ️ About AMMIEL", callback_data="about")],
    ]

    await update.message.reply_text(
        "💎 *AMMIEL JEWELRY*\n\n"
        "Welcome to AMMIEL JEWELRY! 👋\n\n"
        "Handmade bracelets • Made for your style\n\n"
        "What would you like to do?",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "browse":
        text = (
            "💎 *OUR COLLECTION*\n\n"
            "🧵 Paracord Bracelets\n"
            "✨ Classic Bracelets\n"
            "🎨 Colorful Bracelets\n"
            "👑 Premium Designs\n"
        )

        keyboard = [
            [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="back")]
        ]

    elif query.data == "designs":
        text = (
            "🎨 *DESIGNS & COLORS*\n\n"
            "Choose the colors and style you like.\n\n"
            "More designs will be added soon! 💎"
        )

        keyboard = [
            [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="back")]
        ]

    elif query.data == "prices":
        text = (
            "💰 *PRICES*\n\n"
            "Our bracelet prices depend on the design and customization.\n\n"
            "Contact us for the current price of your chosen design."
        )

        keyboard = [
            [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="back")]
        ]

    elif query.data == "order":
        text = (
            "📦 *PLACE YOUR ORDER*\n\n"
            "1️⃣ Choose your bracelet\n"
            "2️⃣ Choose your color\n"
            "3️⃣ Choose quantity\n"
            "4️⃣ Tell us your size\n"
            "5️⃣ Confirm your order\n\n"
            "💬 Contact us to begin your order."
        )

        keyboard = [
            [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="back")]
        ]

    elif query.data == "delivery":
        text = (
            "📍 *PICKUP & DELIVERY*\n\n"
            "📍 Location: Arbaminch\n\n"
            "Pickup and delivery details will be confirmed when you order."
        )

        keyboard = [
            [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="back")]
        ]

    elif query.data == "social":
        text = (
            "📱 *FOLLOW AMMIEL JEWELRY*\n\n"
            "Stay connected with us and see our latest bracelets, "
            "designs and updates. 💎\n\n"
            "Choose a platform below 👇"
        )

        keyboard = [
            [InlineKeyboardButton("📢 Telegram", url=TELEGRAM_LINK)],
            [InlineKeyboardButton("📸 Instagram", url=INSTAGRAM_LINK)],
            [InlineKeyboardButton("📘 Facebook", url=FACEBOOK_LINK)],
            [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="back")],
        ]

    elif query.data == "contact":
        text = (
            "💬 *CONTACT AMMIEL JEWELRY*\n\n"
            "Send us a message here to ask about bracelets, "
            "prices, custom designs, or orders. 💎"
        )

        keyboard = [
            [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="back")]
        ]

    elif query.data == "about":
        text = (
            "ℹ️ *ABOUT AMMIEL JEWELRY*\n\n"
            "AMMIEL JEWELRY creates handmade bracelets made for your style.\n\n"
            "✨ Handmade\n"
            "🎨 Customizable\n"
            "💎 Made with care\n\n"
            "A business under AMMIEL KINGDOM."
        )

        keyboard = [
            [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="back")]
        ]

    else:
        return

    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )


async def back_to_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("🛍️ Browse Bracelets", callback_data="browse")],
        [InlineKeyboardButton("🎨 Designs & Colors", callback_data="designs")],
        [InlineKeyboardButton("💰 Prices", callback_data="prices")],
        [InlineKeyboardButton("📦 Place an Order", callback_data="order")],
        [InlineKeyboardButton("📍 Pickup & Delivery", callback_data="delivery")],
        [InlineKeyboardButton("📱 Follow Us", callback_data="social")],
        [InlineKeyboardButton("💬 Contact Us", callback_data="contact")],
        [InlineKeyboardButton("ℹ️ About AMMIEL", callback_data="about")],
    ]

    await query.edit_message_text(
        "💎 *AMMIEL JEWELRY*\n\n"
        "Welcome back! 👋\n\n"
        "What would you like to do?",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        CallbackQueryHandler(back_to_menu, pattern="^back$")
    )

    app.add_handler(
        CallbackQueryHandler(button_handler)
    )

    print("💎 AMMIEL JEWELRY BOT IS RUNNING...")

    app.run_polling()


if __name__ == "__main__":
    main()
