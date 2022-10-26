#include <stdio.h>

int main(int argc, char *argv[], char *envp[]) {
  for (int i = 0; i < argc; i ++) {
    printf("argv[%d] = %s\n", i, argv[i]);
  }

  printf("environment variables:\n");
  for (char **p = envp; *p != NULL; p ++) {
    printf("%s\n", *p);
  }
  return 0;
}
