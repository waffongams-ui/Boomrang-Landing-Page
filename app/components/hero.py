import reflex as rx


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        rx.el.span(
                            "Boost your reach with ", class_name="block text-white"
                        ),
                        rx.el.span(
                            "Boomrang Campaigns",
                            class_name="bg-clip-text text-transparent bg-gradient-to-r from-blue-500 via-green-400 to-lime-400",
                        ),
                        class_name="text-5xl md:text-6xl lg:text-7xl font-extrabold tracking-tight leading-tight mb-6",
                    ),
                    rx.el.p(
                        "The all-in-one platform to automate your marketing campaigns, track performance, and engage your audience like never before.",
                        class_name="text-xl text-gray-400 mb-10 max-w-2xl leading-relaxed",
                    ),
                    rx.el.div(
                        rx.el.a(
                            rx.el.button(
                                "Get Started Free",
                                rx.icon("arrow-right", class_name="ml-2 h-5 w-5"),
                                class_name="flex items-center justify-center w-full sm:w-auto px-8 py-4 text-lg font-bold rounded-xl text-white bg-gradient-to-r from-blue-500 via-green-400 to-lime-400 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1",
                            ),
                            href="/signup",
                        ),
                        rx.el.button(
                            rx.icon(
                                "circle-play", class_name="mr-2 h-5 w-5 text-white"
                            ),
                            "Watch Demo",
                            class_name="flex items-center justify-center w-full sm:w-auto px-8 py-4 text-lg font-bold rounded-xl text-white border-2 border-gray-700 hover:border-blue-500 hover:bg-white/10 transition-all duration-300",
                        ),
                        class_name="flex flex-col sm:flex-row gap-4",
                    ),
                    class_name="flex flex-col justify-center lg:w-1/2",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.image(
                            src="/placeholder.svg",
                            alt="Dashboard Preview",
                            class_name="rounded-2xl shadow-2xl border-4 border-white transform rotate-2 hover:rotate-0 transition-transform duration-500",
                        ),
                        class_name="relative z-10",
                    ),
                    rx.el.div(
                        class_name="absolute top-0 right-0 -mr-20 -mt-20 w-72 h-72 bg-blue-400 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob"
                    ),
                    rx.el.div(
                        class_name="absolute -bottom-8 left-20 w-72 h-72 bg-green-400 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob animation-delay-2000"
                    ),
                    rx.el.div(
                        class_name="absolute -bottom-8 right-20 w-72 h-72 bg-lime-400 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob animation-delay-4000"
                    ),
                    class_name="relative lg:w-1/2 flex justify-center items-center mt-12 lg:mt-0",
                ),
                class_name="flex flex-col lg:flex-row gap-12 lg:gap-20",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
        ),
        class_name="pt-32 pb-20 md:pt-48 md:pb-32 overflow-hidden",
    )