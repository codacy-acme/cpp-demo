#include <stdlib.h>

int v_error() {
  int* p = new int;
  *p = 2;

  int* u = (int *)malloc(sizeof(int));
  *u = 4;

  return *p + *u;
}
