import reflex as rx


def footer_link(text: str, href: str = "#") -> rx.Component:
    return rx.el.li(
        rx.el.a(
            text,
            href=href,
            class_name="text-gray-400 hover:text-white transition-colors",
        ),
        class_name="mb-3",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.a(
                        rx.el.span(
                            "Boomrang", class_name="text-xl font-bold text-white"
                        ),
                        class_name="flex items-center mb-6",
                    ),
                    rx.el.p(
                        "Automate your success. The marketing platform built for modern growth teams.",
                        class_name="text-gray-400 mb-6",
                    ),
                    rx.el.div(
                        rx.el.a(
                            rx.icon("twitter", class_name="h-5 w-5"),
                            href="#",
                            class_name="text-gray-500 hover:text-blue-500 transition-colors",
                        ),
                        rx.el.a(
                            rx.icon("linkedin", class_name="h-5 w-5"),
                            href="#",
                            class_name="text-gray-500 hover:text-blue-700 transition-colors",
                        ),
                        rx.el.a(
                            rx.icon("github", class_name="h-5 w-5"),
                            href="#",
                            class_name="text-gray-500 hover:text-white transition-colors",
                        ),
                        class_name="flex space-x-5",
                    ),
                    class_name="col-span-1 md:col-span-2 lg:col-span-1",
                ),
                rx.el.div(
                    rx.el.h4("Product", class_name="font-bold text-white mb-6"),
                    rx.el.ul(
                        footer_link("Features"),
                        footer_link("Integrations"),
                        footer_link("Pricing"),
                        footer_link("Changelog"),
                        class_name="text-sm",
                    ),
                    class_name="col-span-1",
                ),
                rx.el.div(
                    rx.el.h4("Company", class_name="font-bold text-white mb-6"),
                    rx.el.ul(
                        footer_link("About Us"),
                        footer_link("Careers"),
                        footer_link("Blog"),
                        footer_link("Contact"),
                        class_name="text-sm",
                    ),
                    class_name="col-span-1",
                ),
                rx.el.div(
                    rx.el.h4("Legal", class_name="font-bold text-white mb-6"),
                    rx.el.ul(
                        footer_link("Privacy Policy"),
                        footer_link("Terms of Service"),
                        footer_link("Cookie Policy"),
                        class_name="text-sm",
                    ),
                    class_name="col-span-1",
                ),
                class_name="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-4 gap-12 lg:gap-8",
            ),
            rx.el.div(
                rx.el.p(
                    "© 2024 Boomrang Inc. All rights reserved.",
                    class_name="text-gray-500 text-sm text-center",
                ),
                class_name="border-t border-gray-800 mt-16 pt-8",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16",
        ),
        class_name="bg-black border-t border-white/10",
    )