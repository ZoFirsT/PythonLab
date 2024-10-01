#include <stdio.h>

int main() {
    int n, m;
    
    // Input number of rows and columns
    printf("Enter the number of rows: ");
    scanf("%d", &n);
    printf("Enter the number of columns: ");
    scanf("%d", &m);
    
    // Declare 2D array
    int matrix[n][m];
    int columnSum[m];
    
    // Initialize columnSum array to 0
    for (int j = 0; j < m; j++) {
        columnSum[j] = 0;
    }
    
    // Input matrix elements
    printf("Enter the matrix elements:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &matrix[i][j]);
            columnSum[j] += matrix[i][j];
        }
    }
    
    // Print column sums
    printf("Sum of each column:\n");
    for (int j = 0; j < m; j++) {
        printf("Column %d: %d\n", j+1, columnSum[j]);
    }
    
    return 0;
}
