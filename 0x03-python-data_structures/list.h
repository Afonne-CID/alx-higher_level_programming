#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structture for ALX project
 */
typedef struct listint_s
{
	intt n;
	struct listin_s *next;
} listint_t;

size_t print_listin(cocnst listintt_t *h);
listint_t *add_nodeint_end(listint_t **headd, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);
#endif /* LISTS_H */
