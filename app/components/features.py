import reflex as rx


def feature_item(icon: str, title: str, description: str) -> rx.Component:
    return rx.el.li(
        rx.el.div(
            rx.icon(icon, class_name="h-6 w-6 text-green-400 mr-3 flex-shrink-0"),
            rx.el.div(
                rx.el.h4(title, class_name="font-bold text-white"),
                rx.el.p(description, class_name="text-gray-400 text-sm mt-1"),
            ),
            class_name="flex items-start",
        )
    )


def features() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        "Workflow Magic",
                        class_name="text-blue-500 font-semibold tracking-wider uppercase text-sm",
                    ),
                    rx.el.h2(
                        "Créez des Campagnes Facilement",
                        class_name="text-3xl md:text-4xl font-bold text-white mt-2 mb-6",
                    ),
                    rx.el.p(
                        "Our drag-and-drop builder allows you to create stunning email sequences in minutes, not hours. Visualize your customer journey.",
                        class_name="text-lg text-gray-400 mb-8",
                    ),
                    rx.el.ul(
                        feature_item(
                            "check",
                            "Smart Templates",
                            "Start fast with pre-built industry templates.",
                        ),
                        feature_item(
                            "check",
                            "A/B Testing",
                            "Automatically optimize for the best performing variants.",
                        ),
                        feature_item(
                            "check",
                            "Real-time Analytics",
                            "Watch your results roll in as they happen.",
                        ),
                        class_name="space-y-6 mb-8",
                    ),
                    rx.el.div(
                        rx.el.div(class_name="h-3 w-3 rounded-full bg-blue-500"),
                        rx.el.div(
                            class_name="h-3 w-3 rounded-full bg-gray-700 hover:bg-blue-500 cursor-pointer transition-colors"
                        ),
                        rx.el.div(
                            class_name="h-3 w-3 rounded-full bg-gray-700 hover:bg-blue-500 cursor-pointer transition-colors"
                        ),
                        class_name="flex space-x-2",
                    ),
                    class_name="lg:w-1/2",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.div(
                                rx.icon("mail", class_name="h-8 w-8 text-white"),
                                class_name="bg-blue-600 p-3 rounded-lg shadow-lg mb-4 w-fit",
                            ),
                            rx.el.div(class_name="h-2 bg-gray-700 rounded w-3/4 mb-2"),
                            rx.el.div(class_name="h-2 bg-gray-700 rounded w-1/2"),
                            class_name="bg-gray-900 p-6 rounded-xl shadow-xl border border-white/10 w-64 absolute top-0 left-0 z-20 transform hover:scale-105 transition-transform duration-300",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.icon("send", class_name="h-8 w-8 text-white"),
                                class_name="bg-green-600 p-3 rounded-lg shadow-lg mb-4 w-fit",
                            ),
                            rx.el.div(class_name="h-2 bg-gray-700 rounded w-3/4 mb-2"),
                            rx.el.div(class_name="h-2 bg-gray-700 rounded w-1/2"),
                            class_name="bg-gray-900 p-6 rounded-xl shadow-xl border border-white/10 w-64 absolute bottom-0 right-0 z-10 transform hover:scale-105 transition-transform duration-300",
                        ),
                        rx.el.div(
                            class_name="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-48 h-0.5 bg-gray-700 -rotate-45 z-0"
                        ),
                        class_name="relative h-96 w-full max-w-md mx-auto",
                    ),
                    class_name="lg:w-1/2 flex justify-center items-center bg-gray-900 rounded-3xl p-8",
                ),
                class_name="flex flex-col lg:flex-row items-center gap-16",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
        ),
        class_name="py-20 md:py-32 bg-black",
        id="features",
    )