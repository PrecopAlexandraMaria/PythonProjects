#include "SortedBag.h"
#include "SortedBagIterator.h"

SortedBag::SortedBag(Relation r) {
	this->rel = r; // the relation used to sort the elements
	this->head = nullptr; // the first node in the list
	this->tail = nullptr; // the last node in the list
	this->totalElements = 0; // the number of elements in the list
}
//Complexity BC=theta(1) WC=theta(1) Total=theta(1)

void SortedBag::add(TComp e) {
	// Check if the element already exists
	// If it does, increment its frequency and return
	// If it doesn't, create a new node and insert it in the correct position

    Node* current = head;
    while (current != nullptr) {
        if (current->value == e) {
            current->frequency++;
            totalElements++;
            return;
        }
        current = current->next;
    }

    // Not found — insert while preserving order
    Node* newNode = new Node{ e, 1, nullptr, nullptr };

    if (head == nullptr) {
        head = tail = newNode;
    }
    else if (!rel(head->value, e)) {
        // Insert at beginning
        newNode->next = head;
        head->prev = newNode;
        head = newNode;
    }
    else {
        current = head;
        while (current != nullptr && rel(current->value, e)) {
            current = current->next;
        }

        if (current == nullptr) {
            // Insert at end
            tail->next = newNode;
            newNode->prev = tail;
            tail = newNode;
        }
        else {
            // Insert in middle
            newNode->next = current;
            newNode->prev = current->prev;
            current->prev->next = newNode;
            current->prev = newNode;
        }
    }

    totalElements++;
}
// Complexity BC=theta(1) WC=theta(n) Total=theta(n)

bool SortedBag::remove(TComp e) {
	// Check if the element exists
	// If it does, decrement its frequency
	// If the frequency becomes 0, remove the node from the list
	// If it doesn't exist, return false
    Node* current = head;
    while (current != nullptr && current->value != e) {
        current = current->next;
    }

    if (current == nullptr)
        return false;

    current->frequency--;
    totalElements--;
    if (current->frequency == 0) {
        if (current == head && current == tail) {
            head = tail = nullptr;
        }
        else if (current == head) {
            head = head->next;
            head->prev = nullptr;
        }
        else if (current == tail) {
            tail = tail->prev;
            tail->next = nullptr;
        }
        else {
            current->prev->next = current->next;
            current->next->prev = current->prev;
        }
        delete current;
    }

    return true;
}
// Complexity BC=theta(1) WC=theta(n) Total=theta(n)

bool SortedBag::search(TComp elem) const {
	// Check if the element exists in the list
	// If it does, return true
	// If it doesn't, return false

    Node* current = head;
    while (current != nullptr) {
        if (current->value == elem)
            return true;
        current = current->next;
    }
    return false;
}
// Complexity BC=theta(1) WC=theta(n) Total=theta(n)

int SortedBag::nrOccurrences(TComp elem) const {
	// Check if the element exists in the list
	// If it does, return its frequency

    Node* current = head;
    while (current != nullptr) {
        if (current->value == elem)
            return current->frequency;
        current = current->next;
    }
    return 0;
}
// Complexity BC=theta(1) WC=theta(n) Total=theta(n)


int SortedBag::size() const {
    return totalElements;
}
// Complexity BC=theta(1) WC=theta(1) Total=theta(1)

bool SortedBag::isEmpty() const {
    return totalElements == 0;
}
//Complexity BC=theta(1) WC=theta(1) Total=theta(1)

SortedBagIterator SortedBag::iterator() {
	return SortedBagIterator(*this);
}
// Complexity BC=theta(1) WC=theta(1) Total=theta(1)

void SortedBag::empty() {
	// Delete all nodes in the list
	// Set head and tail to nullptr
	// Set totalElements to 0

    Node* current = head;
    while (current != nullptr) {
        Node* temp = current;
        current = current->next;
        delete temp;
    }
    head = tail = nullptr;
    totalElements = 0;
}
// Complexity BC=theta(1) WC=theta(n) Total=theta(n)

SortedBag::~SortedBag() {
    empty();
}
// Complexity BC=theta(1) WC=theta(n) Total=theta(n)