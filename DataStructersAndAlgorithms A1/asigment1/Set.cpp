#include "Set.h"
#include "SetIterator.h"
#include <iostream>
#include <exception>
using namespace std;

Set::Set() {
	minElem = 0;
	maxElem = -1;
	capacity = 0;
	elements = nullptr;
	length = 0;
}
//Complexity: BC=WC=AC=theta(1)

bool Set::add(TElem e) {
    if (capacity == 0) {
        // First element
        capacity = 1;
        elements = new bool[1];
        elements[0] = true;
        minElem = e;
        maxElem = e;
        length = 1;
        return true;
    }

    if (e < minElem || e > maxElem) {
        // Resize array to fit new range
        int newMin = min(minElem, e);
        int newMax = max(maxElem, e);
        int newCapacity = newMax - newMin + 1;
        bool* newElements = new bool[newCapacity] {false};

        for (int i = minElem; i <= maxElem; ++i) {
            newElements[i - newMin] = elements[i - minElem];
        }

        delete[] elements;
        elements = newElements;
        capacity = newCapacity;
        minElem = newMin;
        maxElem = newMax;
    }

    int index = e - minElem;

    if (elements[index])
        return false; // already in set

    elements[index] = true;
    length++;
    return true;
}
//Complexity: BC=theta(1) WC=AC=theta(capacity)


bool Set::remove(TElem elem) {
    if (elem < minElem || elem > maxElem)
        return false;

    int index = elem - minElem;
    if (!elements[index])
        return false;

    elements[index] = false;
    length--;

    return true;
}
//Complexity: BC=theta(1), WC=theta(1), AC=theta(1)

bool Set::search(TElem elem) const {
    if (elem < minElem || elem > maxElem)
        return false;
    return elements[elem - minElem];
}
//Complexity: BC=theta(1), WC=theta(1), AC=theta(1)


int Set::size() const {
    return length;
}
//Complexity: BC=WC=AC=theta(1)

bool Set::isEmpty() const {
    return length == 0;
}
//Complexity: BC=WC=AC=theta(1)

Set::~Set() {
	delete[] elements;
}
//Complexity: BC=WC=AC=theta(1)

SetIterator Set::iterator() {
	return SetIterator(*this);
}
//Complexity: BC=theta(1) WC=AC=theta(capacity)

