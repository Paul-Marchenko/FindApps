def take_screenshot(driver, generate_name):

    """
    Takes screenshot of the current open web page
    :param driver
    :return:
    """
    file_name = str(generate_name) + ".png"
    screenshot_directory = "/Users/pavel/PycharmProjects/FindApps/screenshots/"
    destination_file = screenshot_directory + file_name

    try:
        driver.save_screenshot(destination_file)
        print("Screenshot saved to directory --> :: " + destination_file)
    except NotADirectoryError:
        print("Not a directory issue")