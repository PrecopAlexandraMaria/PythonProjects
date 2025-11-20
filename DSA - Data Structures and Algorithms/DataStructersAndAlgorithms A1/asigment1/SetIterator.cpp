#include "SetIterator.h"
#include "Set.h"
#include <stdexcept>
#include <algorithm>

using namespace std;

SetIterator::SetIterator(Set& s) : set(s), index(0) {
	first();
}
//Complexity: BC=theta(1) WC=AC=theta(capacity)

void SetIterator::first() {
    index = 0;
    while (index < set.capacity && !set.elements[index]) {
        index++;
    }
}
//Complexity: BC=theta(1) WC=AC=theta(capacity)

void SetIterator::next() {
    if (!valid())
        throw exception();

    index++;
    while (index < set.capacity && !set.elements[index]) {
        index++;
    }
}
//Complexity: BC=theta(1) WC=AC=theta(capacity)

TElem SetIterator::getCurrent() {
    if (!valid())
        throw exception();
    return index + set.minElem;
}
//Complexity: BC=WC=AC=theta(1)

bool SetIterator::valid() const {
    return index < set.capacity;
}
//Complexity: BC=WC=AC=theta(1)

TElem SetIterator::remove() {
    if (!valid())
        throw exception();
    TElem current = getCurrent();
    set.elements[index] = false;
    set.length--;
    next();
    return current;
}
//Complexity: BC=theta(1) WC=AC=theta(capacity)