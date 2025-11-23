import reflex as rx
from app.components.character_card import character_card


def gallery() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Designed for Growth",
                    class_name="text-3xl md:text-4xl font-bold text-center text-white mb-12",
                ),
                rx.el.div(
                    character_card("Campaign Dashboard"),
                    character_card("Email Editor"),
                    character_card("Analytics View"),
                    character_card("User Flow"),
                    class_name="grid grid-cols-1 md:grid-cols-2 gap-12",
                ),
                class_name="max-w-5xl mx-auto",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
        ),
        class_name="py-20 md:py-32 bg-black",
    )