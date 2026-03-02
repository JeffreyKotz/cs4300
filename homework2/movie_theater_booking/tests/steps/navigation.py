from behave import given, when, then
from pageobjects.pages import (HomePage,
                               MoviesPage,
                               BookSeatPage,
                               BookingHistoryPage
                               )


@given('I am at the Home page')
def start(context):
    """Users begin at the landing page
    """
    context.current_page = HomePage(context)
    assert context.current_page.response.status_code == 200


@when('I click the "{button_name}" button')
def click_button(context, button_name):
    """Model clicking a button of the page
    """
    # get the button of the current page
    button = context.current_page.get_link(button_name)

    # click the button and set the resulting page to the new page
    new_page = context.get_url(button.click().page)

    # match the new page to the different existing pages
    if (new_page == context.get_url('bookings:base_view')):
        context.current_page = HomePage(context)
    elif (new_page == context.get_url('bookings:movies') + '.html'):
        context.current_page = MoviesPage(context)
    elif (new_page == context.get_url('bookings:book_seat') + '.html'):
        context.current_page = BookSeatPage(context)
    elif (new_page == context.get_url('bookings:booking_history') + '.html'):
        context.current_page = BookingHistoryPage(context)

    assert context.current_page.response.status_code == 200


@then('I will be brought to the "{page_name}" page')
def page_loaded(context, page_name):
    """Check that corret page was traveled too
    """
    match page_name:
        case 'Home':
            page = HomePage(context)
        case 'Movies':
            page = MoviesPage(context)
        case 'Book Seat':
            page = BookSeatPage(context)
        case 'Booking History':
            page = BookingHistoryPage(context)

    assert page == context.current_page
