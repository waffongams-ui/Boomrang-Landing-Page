import reflex as rx
from app.components.navbar import navbar
from app.components.hero import hero
from app.components.features import features
from app.components.gallery import gallery
from app.components.stats import stats
from app.components.integrations import integrations
from app.components.faq import faq
from app.components.cta import cta
from app.components.footer import footer


def index() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            hero(),
            features(),
            gallery(),
            stats(),
            integrations(),
            faq(),
            cta(),
            class_name="pt-20",
        ),
        footer(),
        class_name="font-sans antialiased bg-black min-h-screen text-gray-100 selection:bg-blue-500 selection:text-white",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
        rx.el.style("""
            .font-sans { font-family: 'Inter', sans-serif; }
            @keyframes blob {
                0% { transform: translate(0px, 0px) scale(1); }
                33% { transform: translate(30px, -50px) scale(1.1); }
                66% { transform: translate(-20px, 20px) scale(0.9); }
                100% { transform: translate(0px, 0px) scale(1); }
            }
            .animate-blob {
                animation: blob 7s infinite;
            }
            .animation-delay-2000 {
                animation-delay: 2s;
            }
            .animation-delay-4000 {
                animation-delay: 4s;
            }
            """),
    ],
)
app.add_page(index, route="/")