
import enum

# Enumerations
# 1. BookGenre: Automatic integer values starting from 1.
class BookGenre(enum.IntEnum):
    FICTION = enum.auto()
    NON_FICTION = enum.auto()
    SCIENCE = enum.auto()
    HISTORY = enum.auto()
    BIOGRAPHY = enum.auto()

# 2. MembershipLevel: Custom annual fee values.
class MembershipLevel(enum.Enum):
    BASIC = 100
    PREMIUM = 200
    GOLD = 500

# Custom Exceptions
class BookNotAvailableError(Exception):
    """Raised when a book is not available for borrowing."""
    pass

class InvalidMembershipError(Exception):
    """Raised when a non-existent membership level is referenced."""
    pass

class LateReturnError(Exception):
    """Raised when a book is returned after its due date."""
    pass

# Classes

class Book:
    def __init__(self, title, genre, is_available):
        """
        Initialize a Book with a title, a genre (must be a BookGenre), 
        and an availability flag.
        """
        self.title = title
        if not isinstance(genre, BookGenre):
            raise ValueError("genre must be a BookGenre")
        self.genre = genre
        self.is_available = is_available

    def borrow(self):
        """
        Marks a book as unavailable for borrowing.
        Raises BookNotAvailableError if the book is already borrowed.
        """
        if not self.is_available:
            raise BookNotAvailableError("Book is not available for borrowing")
        self.is_available = False

    def return_book(self, is_late: bool):
        """
        Marks a book as available.
        If the book is returned late (is_late=True), raises LateReturnError.
        """
        if is_late:
            raise LateReturnError("Book returned late")
        self.is_available = True

class Member:
    def __init__(self, name, membership_level):
        """
        Initialize a Member with a name and a membership_level.
        The membership_level must be one of the MembershipLevel enumeration.
        """
        self.name = name
        self.membership_level = membership_level

    def get_fee(self):
        """
        Returns the fee associated with the membership level.
        Raises InvalidMembershipError if the membership level is invalid.
        """
        if not isinstance(self.membership_level, MembershipLevel):
            raise InvalidMembershipError("Invalid membership level")
        return self.membership_level.value
