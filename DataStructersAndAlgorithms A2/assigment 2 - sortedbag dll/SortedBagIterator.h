#pragma once
#include "SortedBag.h"

class SortedBag;

class SortedBagIterator
{
	friend class SortedBag;

private:
	const SortedBag& bag;
	SortedBagIterator(const SortedBag& b);

	SortedBag::Node* currentNode;
	int frequencyIndex;

public:
	TComp getCurrent();
	bool valid();
	void next();
	void first();
	int removeOccurences(int nr, TComp elem);
};

