#include <stdio.h>
#include <iostream>
#include <cstdlib>
#include <omp.h>
#include <vector>
using namespace std;

int main() {
    int r = 3, c = 2;
    int matrix[r][c], vector[c], out[r];

    for (int row = 0; row < r; row++) {
        for (int col = 0; col < c; col++) {
            matrix[row][col] = 1;
        }
    }
    cout << "Input matrix" << endl;
    for (int row = 0; row < r; row++) {
        for (int col = 0; col < c; col++) {
            cout << "\t" << matrix[row][col];
        }
        cout << endl;
    }
    for (int col = 0; col < c; col++) {
        vector[col] = 3;
    }
    cout << "Input col-vector" << endl;
    for (int row = 0; row < c; row++) {
        cout << vector[row] << endl;
    }
    #pragma omp parallel for
    for (int row = 0; row < r; row++) {
        out[row] = 0;
        for (int col = 0; col < c; col++) {
            out[row] += matrix[row][col] * vector[col];
        }
    }
    cout << "Resultant col-vector" << endl;
    for (int row = 0; row < r; row++) {
        cout << "\nVector [" << row << "]: " << out[row] << endl;
    }   return 0;
}
