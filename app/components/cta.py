import reflex as rx
from app.states.landing_state import LandingState


def cta() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Ready to skyrocket your campaigns?",
                    class_name="text-3xl md:text-4xl lg:text-5xl font-bold text-white mb-6 text-center",
                ),
                rx.el.p(
                    "Join 10,000+ marketers who are already using Boomrang to grow their business.",
                    class_name="text-blue-50 text-lg md:text-xl mb-10 text-center max-w-2xl mx-auto",
                ),
                rx.el.div(
                    rx.el.input(
                        placeholder="Enter your email",
                        on_change=LandingState.update_email,
                        class_name="w-full md:w-96 px-6 py-4 rounded-xl text-white bg-white/10 placeholder-blue-100 focus:outline-none focus:ring-4 focus:ring-white/30 border border-white/20",
                        default_value=LandingState.email_input,
                    ),
                    rx.el.button(
                        "Sign Up Now",
                        class_name="w-full md:w-auto px-8 py-4 bg-white text-black font-bold rounded-xl hover:bg-gray-100 transition-colors shadow-lg",
                    ),
                    class_name="flex flex-col md:flex-row items-center justify-center gap-4",
                ),
                rx.el.p(
                    "No credit card required • 14-day free trial",
                    class_name="text-blue-100 text-sm mt-6 text-center",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10",
            ),
            rx.el.div(
                class_name="absolute top-0 left-0 w-full h-full overflow-hidden z-0"
            ),
        ),
        class_name="py-24 md:py-32 relative bg-gradient-to-br from-blue-600 via-green-500 to-lime-500",
    )