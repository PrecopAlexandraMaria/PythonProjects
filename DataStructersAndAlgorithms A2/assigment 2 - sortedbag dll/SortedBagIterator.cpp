#include "SortedBagIterator.h"
#include "SortedBag.h"
#include <exception>

using namespace std;

SortedBagIterator::SortedBagIterator(const SortedBag& b) : bag(b) {
	// constructor
	first();
}
//Complexity BC=theta(1) WC=theta(1) Total=theta(1)

TComp SortedBagIterator::getCurrent() {
	//returns the current element from the iterator
	if (!valid())
		throw exception();
	return currentNode->value;
}
//Complexity BC=theta(1) WC=theta(1) Total=theta(1)

bool SortedBagIterator::valid() {
	return currentNode != nullptr;
}
//Complexity BC=theta(1) WC=theta(1) Total=theta(1)

void SortedBagIterator::next() {
	//moves the iterator to the next element in the sorted bag
	//throws an exception if the iterator is not valid
	//if the iterator is valid, it moves to the next element

	if (!valid())
		throw exception();

	if (frequencyIndex < currentNode->frequency) {
		frequencyIndex++;
	}
	else {
		currentNode = currentNode->next;
		frequencyIndex = 1;
	}
}
//Complexity BC=theta(1) WC=theta(1) Total=theta(1)

void SortedBagIterator::first() {
	//moves the iterator to the first element of the sorted bag
	//if the sorted bag is empty, the iterator is invalid

	currentNode = bag.head;
	frequencyIndex = 1;
}
//Complexity BC=theta(1) WC=theta(1) Total=theta(1)

int SortedBagIterator::removeOccurences(int nr, TComp elem) {
	//removes nr occurrences of elem. If element appears less than nr times, it removes all occurrences
	//returns the number of occurrences removed
	//throws an exception if nr is negative
	if (nr < 0)
		throw exception();
	int removed = 0;
	while (valid() && currentNode->value == elem && removed < nr) {
		removed++;
		if (frequencyIndex < currentNode->frequency) {
			currentNode->frequency--;
			frequencyIndex++;
		}
		else {
			currentNode = currentNode->next;
			frequencyIndex = 1;
		}
	}
	return removed;
}
//Complexity BC=theta(1) WC=theta(nr) Total=theta(nr)