import reflex as rx


def character_card(title: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.image(
                src="/placeholder.svg",
                class_name="absolute top-0 left-0 w-full h-full object-cover rounded-[20px] opacity-20 grayscale brightness-50 transform translate-x-6 translate-y-6 transition-all duration-500 ease-out group-hover:translate-x-9 group-hover:translate-y-9",
            ),
            rx.image(
                src="/placeholder.svg",
                class_name="absolute top-0 left-0 w-full h-full object-cover rounded-[20px] opacity-40 grayscale brightness-75 transform translate-x-4 translate-y-4 transition-all duration-500 ease-out group-hover:translate-x-6 group-hover:translate-y-6",
            ),
            rx.image(
                src="/placeholder.svg",
                class_name="absolute top-0 left-0 w-full h-full object-cover rounded-[20px] opacity-60 grayscale transform translate-x-2 translate-y-2 transition-all duration-500 ease-out group-hover:translate-x-3 group-hover:translate-y-3",
            ),
            rx.el.div(
                rx.image(
                    src="/placeholder.svg",
                    alt=title,
                    class_name="w-[110%] h-[110%] max-w-none object-cover -ml-[5%] -mt-[5%] rounded-[20px] transition-transform duration-500 ease-out group-hover:scale-105 group-hover:-translate-y-2",
                ),
                rx.el.div(
                    rx.el.h3(
                        title, class_name="text-white font-bold text-xl relative z-10"
                    ),
                    class_name="absolute bottom-0 left-0 right-0 p-6 bg-gradient-to-t from-black/90 via-black/50 to-transparent rounded-b-[20px]",
                ),
                class_name="relative w-full h-full rounded-[20px] overflow-hidden z-10 bg-gray-900 shadow-[0_20px_40px_rgba(0,0,0,0.15)]",
            ),
            class_name="relative w-full h-80 group select-none cursor-pointer",
        ),
        class_name="p-4",
    )