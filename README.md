# Library Management System

The Library Management System is designed to provide a robust and intuitive solution for managing a library’s collection of books and its membership structure. The project required the creation of a system that incorporates enumerations and custom exception handling to streamline common operations in a library, such as borrowing and returning books, as well as managing different membership levels. This document details what was expected from the assignment, what has been implemented, and how the solution meets these expectations.

---

## Project Requirements and Expectations

The assignment called for the development of a system that leverages Python’s advanced features, such as enumerations and custom exceptions, to manage two core components: the books and the members of a library. Specifically, the following were expected:

1. **Enumerations for Book Genres and Membership Levels:**  
   Two separate enumerations needed to be implemented. One for book genres, which would automatically assign sequential integer values starting from 1 for genres like Fiction, Non-Fiction, Science, History, and Biography. The other enumeration was for membership levels, which should associate specific custom annual fee values with each level. This design ensures that each membership type carries an inherent fee value, streamlining fee retrieval.

2. **Custom Exceptions:**  
   The system was required to define and use custom exceptions for handling error scenarios gracefully. Three specific exceptions were to be implemented:
   - An exception for attempting to borrow a book that is already checked out.
   - An exception to capture scenarios where an invalid membership level is referenced.
   - An exception for handling cases where a book is returned after its due date.
   
   These exceptions serve to encapsulate error conditions in meaningful ways, thereby making error handling more descriptive and easier to manage.

3. **Core Classes – Book and Member:**  
   The Book class had to be capable of representing individual books with attributes such as title, genre, and availability status. Moreover, it needed to provide methods for borrowing and returning books. Borrowing a book should mark it as unavailable and throw a custom error if the book is not available. Returning a book should mark it as available and, if returned late, should trigger a corresponding error.  
   The Member class was expected to encapsulate member details, including a name and a membership level. A key functionality of this class was to return the annual fee associated with the membership level, which relies on the custom enumeration values. If an invalid membership level is supplied, the class should raise a custom exception to prevent misuse.

4. **System Behavior and Error Handling:**  
   The solution needed to handle various scenarios gracefully by catching exceptions and providing meaningful feedback. This not only ensures the robustness of the system but also helps in debugging and maintaining data integrity. The design should lead to a system where every operation – whether borrowing a book, returning a book on time or late, or retrieving a membership fee – behaves predictably and reliably.

---

## What Is Being Implemented

In order to meet the above requirements, the Library Management System has been implemented with the following key components:

### Enumerations

Two enumerations form the backbone of the system's data structure:

- **BookGenre:**  
  This enumeration categorizes books into distinct genres. Using Python’s enumeration capabilities, the system automatically assigns sequential integer values starting at 1. Each genre, such as Fiction, Non-Fiction, Science, History, and Biography, is represented by an enumerated value, ensuring that each genre is unique and can be easily compared or iterated over.

- **MembershipLevel:**  
  This enumeration defines the different levels of library membership. Each membership level – BASIC, PREMIUM, and GOLD – is associated with a custom annual fee. For instance, the BASIC level might have a fee of 100, while the PREMIUM and GOLD levels are assigned higher fee values. By embedding fee values directly into the enumeration, the system simplifies the process of fee retrieval and enforces consistency.

### Custom Exception Handling

To ensure that errors are managed elegantly, several custom exceptions have been defined:

- **BookNotAvailableError:**  
  This exception is thrown when an attempt is made to borrow a book that is not available. Its purpose is to alert the system and the user that the desired book cannot be checked out because it is already in use.

- **InvalidMembershipError:**  
  This exception is raised when an invalid membership level is referenced. It acts as a safeguard against improper data entry or programming mistakes that could lead to incorrect fee calculations or membership assignments.

- **LateReturnError:**  
  This exception signals that a book has been returned after its due date. It enforces the library’s rules regarding timely returns and helps maintain order within the system.

### Class Implementations

The solution centers around two primary classes: Book and Member.

- **Book Class:**  
  This class represents individual books in the library. Each book is characterized by its title, its genre (which must be one of the values from the BookGenre enumeration), and an availability status. Two essential methods are implemented:
  - A method for borrowing the book, which sets the availability status to false. If the book is already borrowed, the system raises the BookNotAvailableError.
  - A method for returning the book, which sets the availability status back to true. If the book is returned late, the method raises a LateReturnError. This approach ensures that the borrowing process is controlled and that errors are flagged as soon as they occur.

- **Member Class:**  
  The Member class holds information about library members, including their name and their membership level. The membership level is linked to the MembershipLevel enumeration, meaning that it carries a pre-defined fee value. A dedicated method is implemented to retrieve the fee associated with the member’s level. If the membership level does not correspond to a valid enumerated value, an InvalidMembershipError is raised. This validation prevents errors in fee computation and ensures the integrity of member data.

---
## How the System Achieves Its Goals

The Library Management System is built with clarity, consistency, and maintainability in mind. By using enumerations, the system standardizes data—each book genre and membership level is clearly defined with automatic or custom-assigned values. This reduces ambiguity and minimizes errors in data handling.

Custom exception handling is central to the system's robustness. Tailored exceptions detect and report errors immediately, providing clear messages that help guide users and developers. This proactive error management reduces the risk of unhandled exceptions and ensures a smooth user experience.

The design also emphasizes a clear separation of concerns. Enumerations, exception handling, and class logic are encapsulated in distinct, self-contained components. This modularity makes it easy to extend or modify the system without disrupting existing functionality—for example, adding new membership levels or book genres in the future.

Consistency is enforced throughout the system. Every operation, whether borrowing a book, returning it, or calculating membership fees, follows a well-defined process. This uniformity simplifies both development and debugging, and ensures predictable behavior in production.

In summary, the system leverages modern Python features to create a scalable, reliable, and maintainable solution. Enumerations provide a clear, self-documenting framework for categorizing data, while custom exceptions offer precise error handling. Together, these techniques create a comprehensive and flexible foundation for managing library operations, ensuring that users can interact with the system seamlessly and confidently.
