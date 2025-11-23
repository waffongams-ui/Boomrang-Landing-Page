import reflex as rx


def navbar() -> rx.Component:
    return rx.el.nav(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.el.span(
                        "Boomrang",
                        class_name="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-green-400",
                    ),
                    href="/",
                    class_name="flex items-center",
                ),
                class_name="flex-shrink-0 flex items-center",
            ),
            rx.el.div(
                rx.el.a(
                    "Features",
                    href="#features",
                    class_name="text-gray-300 hover:text-white font-medium transition-colors",
                ),
                rx.el.a(
                    "Testimonials",
                    href="#testimonials",
                    class_name="text-gray-300 hover:text-white font-medium transition-colors",
                ),
                rx.el.a(
                    "Pricing",
                    href="#pricing",
                    class_name="text-gray-300 hover:text-white font-medium transition-colors",
                ),
                rx.el.a(
                    "FAQ",
                    href="#faq",
                    class_name="text-gray-300 hover:text-white font-medium transition-colors",
                ),
                class_name="hidden md:flex items-center space-x-8",
            ),
            rx.el.div(
                rx.el.a(
                    "Log in",
                    href="/login",
                    class_name="text-gray-300 hover:text-white font-medium mr-4 transition-colors",
                ),
                rx.el.a(
                    "Start free",
                    href="/signup",
                    class_name="bg-gradient-to-r from-blue-500 via-green-400 to-lime-400 text-white px-5 py-2 rounded-full font-semibold hover:shadow-lg hover:opacity-90 transition-all duration-200 transform hover:-translate-y-0.5",
                ),
                class_name="flex items-center",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between",
        ),
        class_name="fixed w-full z-50 bg-black/80 backdrop-blur-md border-b border-white/10 top-0 left-0",
    )