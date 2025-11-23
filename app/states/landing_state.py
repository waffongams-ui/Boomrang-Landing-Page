import reflex as rx


class LandingState(rx.State):
    """State for the landing page interactivity."""

    active_faq_index: int = -1

    @rx.event
    def toggle_faq(self, index: int):
        """Toggle the active FAQ item. If clicked again, close it."""
        if self.active_faq_index == index:
            self.active_faq_index = -1
        else:
            self.active_faq_index = index

    email_input: str = ""

    @rx.event
    def update_email(self, value: str):
        self.email_input = value