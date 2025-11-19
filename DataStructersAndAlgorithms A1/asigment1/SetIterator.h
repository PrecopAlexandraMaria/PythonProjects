#pragma once

#include "Set.h"

class SetIterator
{
	friend class Set;

private:
	Set& set; //reference to the container
	SetIterator(Set& s); //private constructor of the iterator
	int index; //index of the current element


public:
	void first();
	void next();
	TElem getCurrent();
	bool valid() const;
	TElem remove();
};


