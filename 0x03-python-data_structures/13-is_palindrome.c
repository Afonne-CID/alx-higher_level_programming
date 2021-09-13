#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @h: linked list
 * Return: 1 if it is palindrome, 0 otherwise
 */
int is_palindrome(listint_t **h)
{
	listint_t **tmp = h, *slow = *tmp, *current = *tmp, *fast = *tmp;
	int len = 0;

	if (!(*h))
		return (1);
	if (!(*h)->next)
		return (0);
	alot(fast, slow, current);
	while (*h)
	{
		len += 1;
		if ((*h)->next == NULL)
			break;
		*h = (*h)->next;
	}
	if ((*h)->n == current->n)
	{
		while (fast && fast->next)
		{
			slow = slow->next;
			fast = fast->next->next;
		}
		if ((len % 2) == 0)
		{
			slow = reverse_listint(slow);
			while ((current->n == slow->n) && slow)
			{
				if (current->next == slow)
					return (1);
				current = current->next;
				slow = slow->next;
			}
		}
		else
		{
			if (oddlen_listint(slow, tmp))
				return (1);
		}
	}
	return (0);
}

/**
 * reverse_listint - reverses linked list
 * @h: linked list
 * Return: A reversed linked list
 */
listint_t *reverse_listint(listint_t *h)
{
	listint_t *first, *last = NULL;


	if (!h)
		return (NULL);

	while (h->next)
	{
		first = h->next;
		h->next = last;
		last = h;
		h = first;
	}
	h->next = last;
	return (h);
}

/**
 * oddlen_listint - checks for palindrome for odd length linked list
 * @slow: half of a linked list
 * @tmp: double pointer to the first node in llist
 * Return: 1 if palindrome, 0 otherwise
 */
int oddlen_listint(listint_t *slow, listint_t **tmp)
{
	listint_t *current = malloc(sizeof(listint_t));

	if (!current)
		return (0);

	current = *tmp;
	slow = slow->next;

	slow = reverse_listint(slow);
	while ((current->n == slow->n) && slow)
	{
		if (current->next == slow->next)
		{
			slow = reverse_listint(slow);
			return (1);
		}
		current = current->next;
		slow = slow->next;
	}
	slow = reverse_listint(slow);
	return (0);
}

/**
 * alot - mallocs memory
 * @fast: first param
 * @slow: second parma
 * @current: third param
 * Return: 1 on success, 0 otherwise
 */
int alot(listint_t *fast, listint_t *slow, listint_t *current)
{
	fast = malloc(sizeof(listint_t));
	if (!fast)
		return (0);

	slow = malloc(sizeof(listint_t));
	if (!slow)
	{
		free(fast);
		return (0);
	}

	current = malloc(sizeof(listint_t));
	if (!current)
	{
		free(slow);
		return (0);
	}
	return (1);
}
