import reflex as rx
from app.states.landing_state import LandingState


def faq_item(question: str, answer: str, index: int) -> rx.Component:
    is_active = LandingState.active_faq_index == index
    return rx.el.div(
        rx.el.button(
            rx.el.span(
                question, class_name="text-lg font-semibold text-white text-left"
            ),
            rx.cond(
                is_active,
                rx.icon("minus", class_name="h-5 w-5 text-blue-400 flex-shrink-0"),
                rx.icon("plus", class_name="h-5 w-5 text-gray-500 flex-shrink-0"),
            ),
            on_click=lambda: LandingState.toggle_faq(index),
            class_name="w-full flex justify-between items-center py-6 focus:outline-none",
        ),
        rx.el.div(
            rx.el.div(answer, class_name="pb-6 text-gray-400 leading-relaxed"),
            class_name=rx.cond(is_active, "block animate-fade-in", "hidden"),
        ),
        class_name="border-b border-gray-800 last:border-0",
    )


def faq() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Frequently Asked Questions",
                    class_name="text-3xl md:text-4xl font-bold text-center text-white mb-4",
                ),
                rx.el.p(
                    "Everything you need to know about Boomrang.",
                    class_name="text-center text-gray-400 mb-12",
                ),
                rx.el.div(
                    faq_item(
                        "Is there a free trial available?",
                        "Yes, you can try Boomrang for free for 14 days. No credit card required.",
                        0,
                    ),
                    faq_item(
                        "Can I change my plan later?",
                        "Absolutely! You can upgrade or downgrade your plan at any time from your dashboard settings.",
                        1,
                    ),
                    faq_item(
                        "How does the integration work?",
                        "We offer one-click integrations for most popular tools. For custom needs, our API documentation is extensive and developer-friendly.",
                        2,
                    ),
                    faq_item(
                        "What kind of support do you offer?",
                        "We offer 24/7 email support for all plans, and priority live chat support for Pro and Enterprise plans.",
                        3,
                    ),
                    class_name="max-w-3xl mx-auto bg-gray-900 rounded-2xl shadow-sm border border-white/10 px-8 py-2",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
            )
        ),
        class_name="py-20 md:py-32 bg-black",
        id="faq",
    )