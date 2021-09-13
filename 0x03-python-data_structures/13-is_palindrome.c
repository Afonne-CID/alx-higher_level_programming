#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @h: linked list
 * Return: 1 if it is palindrome, 0 otherwise
 */
int is_palindrome(listint_t **h)
{
	listint_t *slow, *fast, *current;
	int len = 0;

	if (!(*h))
		return (1);
	
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
		free(fast);
		free(slow);
		return (0);
	}

	fast = *h;
	slow = *h;
	current = *h;

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
			while (current->next == slow->next)
			{
				if ((current->next->next == slow)
						&& (slow->next->next == NULL))
					return (1);
				current = current->next;
				slow = slow->next;
			}
			return (0);
		}
		else
		{
			slow = slow->next;
			while (current->next == slow->next)
			{
				if ((current->next->next == slow)
						&& (slow->next->next == NULL))
					return (1);
				current = current->next;
				slow = slow->next;
			}
		}
	}
	return (0);
}
