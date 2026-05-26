# struktur-data-20-05-2026

Siap, ini aku bikinin versi **README.md GitHub** yang clean, rapi, dan enak dilihat (tinggal copy aja ke repo kamu) 👍

---

# 📦 Advanced Sorting & Binary Tree Algorithms

Proyek ini berisi implementasi dan analisis algoritma sorting lanjutan serta struktur data binary tree sesuai dengan studi kasus keterbatasan memori dan efisiensi tinggi.

---

## 🚀 Fitur Utama

### 🔢 Sorting Algorithms

* **Merge Sort (Array)**

  * Menggunakan *virtual sublists*
  * Hanya 1 `tmpArray` (efisien memori)
  * Stabil

* **Merge Sort (Linked List)**

  * Menggunakan *fast-slow pointer*
  * Tidak membuat node baru
  * Stabil & optimal untuk linked list

* **Quick Sort (Improved)**

  * Menggunakan **Median-of-Three Pivot**
  * Menghindari worst-case O(n²)

* **Heap Sort (In-Place)**

  * Tidak menggunakan memori tambahan
  * Kompleksitas tetap O(n log n)

---

### 🌳 Binary Tree & Expression Processing

* **Expression Tree Builder**
* **Postorder Evaluation**
* **Infix → Postfix Conversion (implicit)**
* **Handling Division by Zero**

---

### 🧠 Heap & Validation

* **Max Heap Construction (In-Place)**
* **Sift-Down Operation**
* **Complete Binary Tree Validation**

---

## 📁 Struktur Kode

```bash
.
├── advanced_sorter.py
├── expr_heap_sorter.py
└── README.md
```

---

## ⚙️ Cara Menjalankan

### 1. Clone Repository

```bash
git clone https://github.com/username/repo-name.git
cd repo-name
```

### 2. Jalankan Python

```bash
python main.py
```

---

## 🧪 Contoh Penggunaan

### 🔹 Sorting Array

```python
sorter = AdvancedSorter()
arr = [5, 2, 9, 1, 3]
print(sorter.sort_array(arr))
```

### 🔹 Sorting Linked List

```python
head = ListNode(3, ListNode(1, ListNode(2)))
sorted_head = sorter.sort_linked_list(head)
```

### 🔹 Heapsort

```python
heap = ExprHeapSorter("((8*5)+(9/(7-4)))")
arr = [5, 3, 8, 1]
print(heap.heapsort_inplace(arr))
```

---

## ⚠️ Batasan Implementasi

* ❌ Tidak menggunakan `sorted()` atau `list.sort()`
* ❌ Tidak menggunakan library eksternal
* ❌ Tidak membuat array tambahan (kecuali `tmpArray` sekali)
* ❌ Tidak membuat node baru pada linked list

---

## 📊 Kompleksitas

| Algoritma  | Waktu          | Ruang    |
| ---------- | -------------- | -------- |
| Merge Sort | O(n log n)     | O(n)     |
| Quick Sort | O(n log n) avg | O(log n) |
| Heap Sort  | O(n log n)     | O(1)     |

---

## 💡 Insight Penting

* Merge Sort lebih cocok untuk **linked list**
* Quick Sort butuh strategi pivot yang baik
* Heap Sort terbaik untuk kondisi **memori terbatas**
* Radix Sort cepat tapi tidak cocok untuk O(1) space

---

## 👨‍💻 Author

* Nama: (Isi Nama Kamu)
* Kelas: (Isi Kelas)
* Mata Kuliah: Analisis & Desain Algoritma
