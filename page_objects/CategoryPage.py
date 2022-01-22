from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class CategoryPage(BasePage):
    CATEGORY_PAGE = (By.ID, "product-category")
    COLUMN_LEFT = (By.ID, "column-left")
    LIST_VIEW_BUTTON = (By.ID, "list-view")
    GRID_VIEW_BUTTON = (By.ID, "grid-view")
    PRODUCT_COMPARE_LINK = (By.ID, "compare-total")
