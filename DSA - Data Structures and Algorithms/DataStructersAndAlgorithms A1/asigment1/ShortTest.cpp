#include "ShortTest.h"
#include <assert.h>
#include "Set.h"
#include "SetIterator.h"
#include <iostream>
using namespace std;
void testAll() {
	Set s;
	assert(s.isEmpty() == true);
	assert(s.size() == 0);
	assert(s.add(5) == true);
	assert(s.add(1) == true);
	assert(s.add(10) == true);
	assert(s.add(7) == true);
	assert(s.add(1) == false);
	assert(s.add(10) == false);
	assert(s.add(-3) == true);
	assert(s.size() == 5);
	assert(s.search(10) == true);
	assert(s.search(16) == false);
	assert(s.remove(1) == true);
	assert(s.remove(6) == false);
	assert(s.size() == 4);


	SetIterator it = s.iterator();
	it.first();
	int sum = 0;
	while (it.valid()) {
		TElem e = it.getCurrent();
		sum += e;
		it.next();
	}
	assert(sum == 19);

    Set s2;
    s2.add(10);
    s2.add(20);
    s2.add(30);

    SetIterator it2 = s2.iterator();
    it2.first();
    assert(it2.valid());

    // Remove first element
    TElem removed = it2.remove();
    assert((removed == 10 || removed == 20 || removed == 30)); // Order is not guaranteed
    assert(s2.search(removed) == false); // Removed element is gone

    // Remove second element
    assert(it2.valid()); // Should point to next valid element
    TElem removed2 = it2.remove();
    assert((removed2 != removed)); // Should not be same as first removed
    assert(s2.search(removed2) == false);

    // Remove third (last) element
    assert(it2.valid());
    TElem removed3 = it2.remove();
    assert(s2.search(removed3) == false);

    // Now the set should be empty
    assert(s2.isEmpty() == true);
    assert(it2.valid() == false);

    // Trying to remove again should throw exception
    try {
        it2.remove();
        assert(false); // Should not reach here
    }
    catch (std::exception&) {
        assert(true);
    }
}
