<h6 align="right">памятка-курс созданная учеником 11 А класса Серебряковым Саввой</h6>
<h1 align="center">Сортировки их виды и реализации</h1>
<br>
<b>Алгоритмы и структуры данных</b> являются основой всего программирования и без их знания не получится быть грамотным специалистом. В данном репозитории речь пойдет об одном из самых главных алгоритмах в программировании - <b>сортировке.</b>

<b>Сортировка</b> - это упорядочивание данных по некоторым признакам


<h2>Сортировка пузырьком</h2>
Сортировка пузырьком, сортировка простыми обменами, метод сортировки обменами — один из алгоритмов сортировки. По сравнению с другими алгоритмами считается простейшим для понимания и реализации. Эффективен для массивов небольшого размера. Относится к алгоритмам устойчивой сортировки 

Алгоритм считается учебным, на практике (вне учебной литературы) не применяется (на практике применяются более эффективные алгоритмы). Лежит в основе некоторых более эффективных алгоритмов. 
<br>

<details>  
  
<summary><i>Реализация на Python:</i></summary>

```python
 def bubble_sort(array):  
    N = len(array)  
    for i in range(N-1):  
        for j in range(N-i-1):  
            if array[j] > array[j+1]: 
                array[j],array[j+1] \ 
                    = array[j+1], array[j]
```
</details>
<details>
<summary><i>Реализация на C++:</i></summary>
  
```C++
void bubbleSort(int arr[], int n)
{
    int i, j;
    bool swapped;
    for (i = 0; i < n - 1; i++) {
        swapped = false;
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (swapped == false)
            break;
    }
}
```
</details>
<details>
  
<summary><i>Реализация на Java:</i></summary>
  
```java
static void bubbleSort(int arr[], int n)
    {
        int i, j, temp;
        boolean swapped;
        for (i = 0; i < n - 1; i++) {
            swapped = false;
            for (j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }
            if (swapped == false)
                break;
        }
    }
```
</details>

<h2>Шейкерная сортировка</h2>
Сортировка перемешиванием, шейкерная сортировка, или двунаправленная — разновидность пузырьковой сортировки. Имеет схожие с пузырьковой свойства, но немного быстрее за счет прохода в обе стороны. Относится к алгоритмам устойчивой сортировки.
<br>
<br>

<details>
  
<summary><i>Реализация на Python:</i></summary>
  
```python
def shake_sort(array):  
    left = 0  
    right = len(array) - 1  
    while left <= right:  
        for i in range(left, right, 1):  
            if array[i] > array[i + 1]:  
                array[i], array[i + 1] = array[i + 1], array[i]  
            right -= 1 
        for i in range(right, left, -1):  
           if array[i - 1] > array[i]:
              array[i], array[i - 1] = array[i - 1], array[i]  
            left += 1 
```
</details>

<details>
<summary><i>Реализация на C++:</i></summary>
  
```C++
void shake_sort(int arr[], int n)
{
    int i, j;
    bool swapped = true;
    while (swapped) {
        swapped = false;
        for (j = 0; j < n - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        for (j = n-1; j > 0; j--) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        
    }
}
```
</details>

<details>
<summary><i>Реализация на Java:</i></summary>
  
```java
void CocktailSort(int a[], int n)
{
    bool swapped = true;
    int start = 0;
    int end = n - 1;
    while (swapped) {
        swapped = false;
        for (int i = start; i < end; ++i) {
            if (a[i] > a[i + 1]) {
                swap(a[i], a[i + 1]);
                swapped = true;
            }
        }
        if (!swapped)
            break;
        swapped = false;
        --end;
        for (int i = end - 1; i >= start; --i) {
            if (a[i] > a[i + 1]) {
                swap(a[i], a[i + 1]);
                swapped = true;
            }
        }
        ++start;
    }
}
```
</details>

<h2>Сортировка вставками </h2>
Сортировка вставками — алгоритм сортировки, в котором элементы входной последовательности просматриваются по одному, и каждый новый поступивший элемент размещается в подходящее место среди ранее упорядоченных элементов. Относится к алгоритмам устойчивой сортировки 
<br>
<br>

<details>

<summary><i>Реализация на Python:</i></summary>
  
```python
def sort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i - 1 
        while j >= 0 and key < arr[j]: 
            arr[j+1] = arr[j] 
            j -= 1 
        arr[j+1] = key
```

</details>

<details>
<summary><i>Реализация на C++:</i></summary>
  
```C++
void insertionSort(int arr[], int n)
{
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}
```

</details>

<details>

<summary><i>Реализация на Java:</i></summary>
  
```java
public class InsertionSort {
    void sort(int arr[])
    {
        int n = arr.length;
        for (int i = 1; i < n; ++i) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
    }
```

</details>

<h2>Сортировка выбором</h2>
Сортировка выбором — еще один из алгоритмов сортировки. Может быть как устойчивый, так и неустойчивый. 
В ходе алгоритма мы ищем наименьший элемент массива и перемещаем его в начало, после мы рекурсивно повторяем это для всех последующих элементов. 

<br>
<br>

<details>

<summary><i>Реализация на Python:</i></summary>
  
```python
def selection_sort(A): 
    for i in range(len(A) - 1): 
        min_index = i 
        for k in range(i + 1, len(A)): 
            if A[k] < A[min_index]: 
                min_index = k 
        A[i], A[min_index] = A[min_index], A[i] 
```

</details>

<details>
<summary><i>Реализация на C++:</i></summary>
  
```C++
void selectionSort(int arr[], int n) 
{ 
    int i, j, min_idx; 
    for (i = 0; i < n - 1; i++) { 
        min_idx = i; 
        for (j = i + 1; j < n; j++) { 
            if (arr[j] < arr[min_idx]) 
                min_idx = j; 
        } 
        if (min_idx != i) 
            swap(arr[min_idx], arr[i]); 
    } 
} 
```

</details>

<details>

<summary><i>Реализация на Java:</i></summary>
  
```java
public class SelectionSort 
{ 
    void sort(int arr[]) 
    { 
        int n = arr.length; 
  
        for (int i = 0; i < n-1; i++) 
        { 
            int min_idx = i; 
            for (int j = i+1; j < n; j++) 
                if (arr[j] < arr[min_idx]) 
                    min_idx = j; 
            int temp = arr[min_idx]; 
            arr[min_idx] = arr[i]; 
            arr[i] = temp; 
        } 
    }
} 
```

</details>

<h2>Сортировка подсчётом</h2>
Сортировка подсчётом — алгоритм сортировки, в котором используется диапазон чисел сортируемого массива  для подсчёта совпадающих элементов. Применение сортировки подсчётом целесообразно лишь тогда, когда сортируемые числа имеют (или их можно отобразить в) диапазон возможных значений, который достаточно мал по сравнению с сортируемым множеством, например, миллион натуральных чисел меньших 1000. 

<br>
<br>

<details>

<summary><i>Реализация на Python:</i></summary>
  
```python
def count_sort(array): 
    scope = max(array) + 1 
    C = [0] * scope 
    for x in array: 
        C[x] += 1 
    array[:] = [] 
    for number in range(scope): 
        array += [number] * C[number] 
```

</details>

<details>
<summary><i>Реализация на C++:</i></summary>
  
```C++
void count_sort(int arr[], int n) 
{ 
    int k = *max_element(arr, arr + n);
    int count[k + 1] = { 0 }; 
    for (int i = 0; i < n; i++) { 
        count[arr[i]]++; 
    } 
    for (int i = 1; i <= k; i++) { 
        count[i] = count[i] + count[i - 1]; 
    } 
    int ans[n]; 
    for (int i = n - 1; i >= 0; i--) { 
        ans[--count[arr[i]]] = arr[i]; 
    } 
    for (int i = 0; i < n; i++) { 
        arr[i] = ans[i]; 
    } 
} 
  
```

</details>

<details>

<summary><i>Реализация на Java:</i></summary>
  
```java
public class CountingSort {
    void sort(char arr[])
    {
        int n = arr.length;
        char output[] = new char[n];
        int count[] = new int[256];
        for (int i = 0; i < 256; ++i)
            count[i] = 0;
        for (int i = 0; i < n; ++i)
            ++count[arr[i]];
        for (int i = 1; i <= 255; ++i)
            count[i] += count[i - 1];
        for (int i = 0; i < n; ++i) {
            output[count[arr[i]] - 1] = arr[i];
            --count[arr[i]];
        }
        for (int i = 0; i < n; ++i)
            arr[i] = output[i];
    }
```

</details>

<h2>Быстрая сортировка</h2>
Быстрая сортировка, сортировка Хоара, часто называемая qsort (по имени в стандартной библиотеке языка Си) — алгоритм сортировки, разработанный английским информатиком Тони Хоаром во время своей работы в МГУ в 1960 году. Один из самых быстрых известных универсальных алгоритмов сортировки массивов; из-за наличия ряда недостатков на практике обычно используется с некоторыми доработками. 
QuickSort является существенно улучшенным вариантом алгоритма сортировки с помощью прямого обмена (его варианты известны как «Пузырьковая сортировка» и «Шейкерная сортировка»), известного в том числе своей низкой эффективностью.  
Принципиальное отличие состоит в том, что в первую очередь производятся перестановки на наибольшем возможном расстоянии и после каждого прохода элементы делятся на две независимые группы (таким образом улучшение самого неэффективного прямого метода сортировки дало в результате один из наиболее эффективных улучшенных методов). 
В ходе алгоритма мы выбираем опорный элемент из массива и переносим все большие элементы массива в правую часть, а меньшие в левую. Рекурсивно выполняем для обоих образовавшихся подмассивов. 

<br>
<br>

<details>

<summary><i>Реализация на Python:</i></summary>
  
```python
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)
```

</details>

<details>
<summary><i>Реализация на C++:</i></summary>
  
```C++
int partition(int arr[],int low,int high)
{
  int pivot=arr[high];
  int i=(low-1);
  for(int j=low;j<=high;j++)
  {
    if(arr[j]<pivot)
    {
      i++;
      swap(arr[i],arr[j]);
    }
  }
  swap(arr[i+1],arr[high]);
  return (i+1);
}

void quickSort(int arr[],int low,int high)
{
  if(low<high)
  {
    int pi=partition(arr,low,high);
    quickSort(arr,low,pi-1);
    quickSort(arr,pi+1,high);
  }
}
  
```

</details>

<details>

<summary><i>Реализация на Java:</i></summary>
  
```java
static void swap(int[] arr, int i, int j)
    {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    static int partition(int[] arr, int low, int high)
    {
        int pivot = arr[high];
        int i = (low - 1);
        for (int j = low; j <= high - 1; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, high);
        return (i + 1);
    }
    static void quickSort(int[] arr, int low, int high)
    {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }
    public static void printArr(int[] arr)
    {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
```

</details>

<h2>Сортировка слиянием</h2>
Сортировка слиянием — алгоритм сортировки, хороший пример использования принципа «разделяй и властвуй». Сначала задача разбивается на несколько подзадач меньшего размера. Затем эти задачи решаются с помощью рекурсивного вызова или непосредственно, если их размер достаточно мал. Наконец, их решения комбинируются, и получается решение исходной задачи. Данный метод сортировки стабилен и всегда имеет одну и ту же сложность. 
Алгоритм был изобретён Джоном фон Нейманом в 1945 году. 
Также немного модифицированная сортировка слиянием используется в Java как сортировка по умолчанию(в котором слияние опускается, если последний элемент в нижнем подсписке меньше первого элемента в верхнем подсписке). 
Алгоритм заключается в разбиении массива давнных на два субмассива, если длина получившегося массива равна двум, тогда мы возвращаем отсортированный массив из двух элементов. Рекурсивно повторяя этот алгоритм мы получаем отсортированный массив данных. 

<br>
<br>

<details>

<summary><i>Реализация на Python:</i></summary>
  
```python
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
```

</details>

<details>
<summary><i>Реализация на C++:</i></summary>
  
```C++
void merge(int array[], int const left, int const mid,
           int const right)
{
    int const subArrayOne = mid - left + 1;
    int const subArrayTwo = right - mid;
    auto *leftArray = new int[subArrayOne],
         *rightArray = new int[subArrayTwo];
    for (auto i = 0; i < subArrayOne; i++)
        leftArray[i] = array[left + i];
    for (auto j = 0; j < subArrayTwo; j++)
        rightArray[j] = array[mid + 1 + j];
 
    auto indexOfSubArrayOne = 0, indexOfSubArrayTwo = 0;
    int indexOfMergedArray = left;
    while (indexOfSubArrayOne < subArrayOne
           && indexOfSubArrayTwo < subArrayTwo) {
        if (leftArray[indexOfSubArrayOne]
            <= rightArray[indexOfSubArrayTwo]) {
            array[indexOfMergedArray]
                = leftArray[indexOfSubArrayOne];
            indexOfSubArrayOne++;
        }
        else {
            array[indexOfMergedArray]
                = rightArray[indexOfSubArrayTwo];
            indexOfSubArrayTwo++;
        }
        indexOfMergedArray++;
    }
    while (indexOfSubArrayOne < subArrayOne) {
        array[indexOfMergedArray]
            = leftArray[indexOfSubArrayOne];
        indexOfSubArrayOne++;
        indexOfMergedArray++;
    }
    while (indexOfSubArrayTwo < subArrayTwo) {
        array[indexOfMergedArray]
            = rightArray[indexOfSubArrayTwo];
        indexOfSubArrayTwo++;
        indexOfMergedArray++;
    }
    delete[] leftArray;
    delete[] rightArray;
}
void mergeSort(int array[], int const begin, int const end)
{
    if (begin >= end)
        return;
 
    int mid = begin + (end - begin) / 2;
    mergeSort(array, begin, mid);
    mergeSort(array, mid + 1, end);
    merge(array, begin, mid, end);
}
```

</details>

<details>

<summary><i>Реализация на Java:</i></summary>
  
```java
class MergeSort {
    void merge(int arr[], int l, int m, int r)
    {
        int n1 = m - l + 1;
        int n2 = r - m;
        int L[] = new int[n1];
        int R[] = new int[n2];
        for (int i = 0; i < n1; ++i)
            L[i] = arr[l + i];
        for (int j = 0; j < n2; ++j)
            R[j] = arr[m + 1 + j];
        int i = 0, j = 0;
        int k = l;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            }
            else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }
        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }
        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }
    void sort(int arr[], int l, int r)
    {
        if (l < r) {
            int m = l + (r - l) / 2;
            sort(arr, l, m);
            sort(arr, m + 1, r);
            merge(arr, l, m, r);
        }
    }
```

</details>


<h2>Пирамидальная сортировка</h2>
Пирамидальная сортировка — это один из эффективных алгоритмов сортировки данных. Алгоритм получил свое название от структуры данных, называемой пирамидой или кучей. 
Процесс пирамидальной сортировки включает в себя несколько шагов: 
Строительство пирамиды из заданного массива данных. 
Удаление наибольшего элемента (вершины пирамиды) и замена его с последним элементом пирамиды. 
Повторение шага 2 для оставшейся пирамиды.Извлечение элементов из пирамиды в обратном порядке, чтобы получить отсортированный массив. 

<br>

<br>

<details>

<summary><i>Реализация на Python:</i></summary>
  
```python
def heapify(arr, N, i):
    largest = i  
    l = 2 * i + 1    
    r = 2 * i + 2     
    if l < N and arr[largest] < arr[l]:
        largest = l
    if r < N and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] 
        heapify(arr, N, largest)
 
def heapSort(arr):
    N = len(arr)
    for i in range(N//2 - 1, -1, -1):
        heapify(arr, N, i)
    for i in range(N-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
```

</details>

<details>
<summary><i>Реализация на C++:</i></summary>
  
```C++
void heapify(int arr[], int N, int i)
{

    int largest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;
    if (l < N && arr[l] > arr[largest])
        largest = l;
    if (r < N && arr[r] > arr[largest])
        largest = r;
    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, N, largest);
    }
}
void heapSort(int arr[], int N)
{
    for (int i = N / 2 - 1; i >= 0; i--)
        heapify(arr, N, i);
    for (int i = N - 1; i > 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}
```

</details>

<details>

<summary><i>Реализация на Java:</i></summary>
  
```java
public class HeapSort {
    public void sort(int arr[])
    {
        int N = arr.length;
        for (int i = N / 2 - 1; i >= 0; i--)
            heapify(arr, N, i);
        for (int i = N - 1; i > 0; i--) {
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;
            heapify(arr, i, 0);
        }
    }
    void heapify(int arr[], int N, int i)
    {
        int largest = i; 
        int l = 2 * i + 1; 
        int r = 2 * i + 2; 
        if (l < N && arr[l] > arr[largest])
            largest = l;
        if (r < N && arr[r] > arr[largest])
            largest = r;
        if (largest != i) {
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;
            heapify(arr, N, largest);
        }
    }
}
```

</details>
