import reflex as rx


def stat_card(number: str, label: str, icon: str, color: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name=f"h-8 w-8 {color} mb-4"),
            class_name="flex justify-center",
        ),
        rx.el.h3(number, class_name="text-4xl font-bold text-white mb-2"),
        rx.el.p(
            label,
            class_name="text-gray-400 font-medium uppercase tracking-wider text-sm",
        ),
        class_name="text-center p-6 rounded-2xl bg-gray-800/50 backdrop-blur-sm border border-gray-700 hover:border-gray-600 transition-all duration-300",
    )


def stats() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                stat_card("97%", "Deliverability", "send", "text-blue-400"),
                stat_card("5k+", "Daily Clicks", "mouse-pointer-2", "text-green-400"),
                stat_card("76%", "Open Rate", "mail-open", "text-purple-400"),
                stat_card("3x", "Conversions", "trending-up", "text-lime-400"),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
        ),
        class_name="py-20 bg-gray-900",
    )