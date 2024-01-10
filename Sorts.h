#pragma once
#include <iostream>
#include <list>
#include <vector>

#include <iterator>
template <typename T> class Sorts
{
public:
	std::list<T> arrayList;
	std::vector<T> bubbleArray,insertionArray,heapArray,shakeArray;
	float BubbleSort()
	{
		std::cout <<"Time to Bubble>" << std::endl;
		unsigned int start_time = clock(); // начальное время
		int size = bubbleArray.size();
		for (int i = 1; i < size; i++)
			for (int j = size-1; j >=i; j--)
				if (bubbleArray[j-1] > bubbleArray[j])
					swap(&bubbleArray, j - 1, j);
		unsigned int end_time = clock(); // конечное время
		unsigned int search_time = end_time - start_time; // искомое время
		std::cout << (float)search_time / CLOCKS_PER_SEC << std::endl;
		return (float)search_time / CLOCKS_PER_SEC;
	}
	float InsertionSort()
	{
		std::cout << "Time to Insertion>" << std::endl;
		unsigned int start_time = clock(); // начальное время
		int size = insertionArray.size();
		for (int i = 1; i < size; i++)
		{
			T tmp = insertionArray[i];
			int j = i;
			while (j > 0 && insertionArray[j - 1] > tmp)
			{
				insertionArray[j] = insertionArray[j - 1];
				j = j - 1;
			}
			insertionArray[j] = tmp;
		}
		unsigned int end_time = clock(); // конечное время
		unsigned int search_time = end_time - start_time; // искомое время
		std::cout << (float)search_time / CLOCKS_PER_SEC << std::endl;
		return (float)search_time / CLOCKS_PER_SEC;
	}
	void swap(std::vector<T> *v, int n, int m)
	{
		T tmp = (*v)[n];
		(*v)[n] = (*v)[m];
		(*v)[m] = tmp;
	}
	float HeapSort()
	{
		std::cout << "Time to Heap>" << std::endl;
		unsigned int start_time = clock(); // начальное время
		int size = heapArray.size();
		for (int j = 0; j < size; j++)
		{
			for (int i = size / 2 - 1 - j / 2; i > -1; i--)
			{
				if (2 * i + 2 <= size - 1 - j)
				{
					if (heapArray[2 * i + 1] > heapArray[2 * i + 2])
					{
						if (heapArray[i] < heapArray[2 * i + 1])
						{
							swap(&heapArray, i, 2 * i + 1);
						}
					}
					else
						if (heapArray[i] < heapArray[2 * i + 2])
						{
							swap(&heapArray, i, 2 * i + 2);
						}
				}
				else
					if (2 * i + 1 <= size - 1 - j)
						if (heapArray[i] < heapArray[2 * i + 1])
							swap(&heapArray, i, 2 * i + 1);
			}
			swap(&heapArray, 0, size - 1 - j);
		}
		unsigned int end_time = clock(); // конечное время
		unsigned int search_time = end_time - start_time; // искомое время
		std::cout << (float)search_time / CLOCKS_PER_SEC << std::endl;
		return (float)search_time / CLOCKS_PER_SEC;
	}
	float ShakeSort()
	{
		std::cout << "Time to Shake>" << std::endl;
		unsigned int start_time = clock(); // начальное время
		int size = shakeArray.size();
		int left = 0;
		int right = size - 1;
		do {
			for (int i = left; i < right; i++) {
				if (shakeArray[i] > shakeArray[i + 1])
					swap(&shakeArray,i,i+1);
			}
			right--;
			for (int i = right; i > left; i--) {
				if (shakeArray[i] < shakeArray[i - 1])
					swap(&shakeArray, i-1, i);
			}
			left++;
		} while (left < right);
		unsigned int end_time = clock(); // конечное время
		unsigned int search_time = end_time - start_time; // искомое время
		std::cout << (float)search_time / CLOCKS_PER_SEC << std::endl;
		return (float)search_time / CLOCKS_PER_SEC;
	}
	void PrintArray(int num)
	{
		switch (num)
		{
		case 0:
			for (typename std::list<T>::iterator it = arrayList.begin(); it != arrayList.end(); it++)
				std::cout << (*it) << " ";
			break;
		case 1:
			for (typename std::vector<T>::iterator it = bubbleArray.begin(); it != bubbleArray.end(); it++)
				std::cout << (*it) << " ";
			break;
		case 2:
			for (typename std::vector<T>::iterator it = shakeArray.begin(); it != shakeArray.end(); it++)
				std::cout << (*it) << " ";
			break;
		case 3:
			for (typename std::vector<T>::iterator it = heapArray.begin(); it != heapArray.end(); it++)
				std::cout << (*it) << " ";
			break;
		case 4:
			for (typename std::vector<T>::iterator it = insertionArray.begin(); it != insertionArray.end(); it++)
				std::cout << (*it) << " ";
			break;
		default:
			break;
		
		}
		std::cout << std::endl;
	}
};