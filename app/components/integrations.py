import reflex as rx


def integrations() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.image(
                            src="/placeholder.svg",
                            class_name="w-full h-auto rounded-2xl shadow-2xl border border-white/10",
                        ),
                        rx.el.div(
                            rx.icon("blocks", class_name="h-6 w-6 text-blue-400"),
                            class_name="absolute -top-6 -right-6 bg-gray-800 p-4 rounded-full shadow-xl animate-bounce border border-white/10",
                        ),
                        class_name="relative",
                    ),
                    class_name="lg:w-1/2 order-2 lg:order-1",
                ),
                rx.el.div(
                    rx.el.h2(
                        "Connect Seamlessly with Your Tools",
                        class_name="text-3xl md:text-4xl font-bold text-white mb-6",
                    ),
                    rx.el.p(
                        "Boomrang integrates with over 50+ tools you already use. Sync your CRM, e-commerce store, and support platforms in just one click.",
                        class_name="text-lg text-gray-400 mb-8",
                    ),
                    rx.el.div(
                        rx.el.div(
                            "CRM Tools",
                            class_name="px-4 py-2 bg-blue-900/30 text-blue-300 rounded-lg font-medium text-sm border border-blue-800/30",
                        ),
                        rx.el.div(
                            "E-commerce",
                            class_name="px-4 py-2 bg-green-900/30 text-green-300 rounded-lg font-medium text-sm border border-green-800/30",
                        ),
                        rx.el.div(
                            "Social Media",
                            class_name="px-4 py-2 bg-purple-900/30 text-purple-300 rounded-lg font-medium text-sm border border-purple-800/30",
                        ),
                        class_name="flex flex-wrap gap-3 mb-10",
                    ),
                    rx.el.button(
                        "Explore Integrations",
                        rx.icon("arrow-right", class_name="ml-2 h-4 w-4"),
                        class_name="flex items-center px-6 py-3 bg-white text-black rounded-xl font-semibold hover:bg-gray-200 transition-colors",
                    ),
                    class_name="lg:w-1/2 order-1 lg:order-2 flex flex-col justify-center",
                ),
                class_name="flex flex-col lg:flex-row gap-16 lg:gap-24",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
        ),
        class_name="py-20 md:py-32 bg-black",
    )