/**
* @file main.c
* @brief 중계기가 커버하지 못하는 집의 개수를 구하는 프로그램
* @author leejonghun (ejonghoon0530@naver.com)
* @date 2025-11-25
*/

/**
 * @mainpage 중계기가 커버하지 못하는 집의 개수를 구하는 프로그램
 * @section 프로그램 개요
 * 이 프로그램은 2차원 문자 배열로 표현된 집과 중계기의 상태를 입력받아, 각 중계기가 커버하지 못하는 집의 개수를 계산하여 출력합니다.
 * 중계기는 A급, B급, C급으로 나뉘며, 각 등급에 따라 커버할 수 있는 범위가 다릅니다.
 * @section 사용법
 * 1. 입력 파일(sample_input.txt)을 준비합니다. 첫 번째 줄에는 테스트 케이스의 수가, 그 다음 줄부터는 각 테스트 케이스에 대한 행과 열의 수, 그리고 2차원 문자 배열이 포함되어야 합니다.
 * 2. 프로그램을 컴파일하고 실행합니다.
 * 3. 결과는 각 테스트 케이스에 대해 커버하지 못하는 집의 개수가 출력됩니다.
 * @see UTF-8로 인코딩 되었습니다. CP949 환경에서 컴파일 시 인코딩 문제로 인해 오류가 발생할 수 있습니다.
 */


#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

/**
 * @brief 2차원 문자 배열 출력 함수
 * @param arr 2차원 문자 배열
 * @param row 행의 수
 * @param col 열의 수
 */
void see(char arr[][101], int row, int col);

/**
 * @brief 중계기의 종류에 따라 커버하지 못하는 집의 개수를 계산하여 반환하는 함수
 * @param arr 2차원 문자 배열 
 * @param row 행의 수
 * @param col 열의 수
 * @return 커버하지 못하는 집의 개수
*/
int cover_range(char arr[][101], int row, int col);


/**
* @brief 메인 함수
*/
int main(void)
{
	FILE* fp = NULL;
	int n = 0;	//테스트 케이스 수
	int result = 0;	//결과 값
	int row = 0; //행의 수
	int col = 0; //열의 수
	char arr[101][101] = { 0, }; //집의 상태를 저장하는 2차원 배열, 최대 크기 101 x 101
	char buf[101]; //한 줄 입력을 저장하는 버퍼

	if ((fp = fopen("sample_input.txt", "r")) == NULL){ //파일이 존재하지 않을 때 에러 처리
		fprintf(stderr, "No file exist!\n");
		return -1;
	}
	fscanf(fp, "%d", &n); //테스트 케이스 수 입력
	while (n-- > 0) { //테스트 케이스 반복 처리
		if (fscanf(fp, "%d %d", &row, &col) != 2) { //행과 열의 수 입력
			printf("fail to read row/col!\n");
			return -1;
		}
		if (row < 1 || row > 100 || col < 1 || col > 100) { //행과 열의 수가 범위를 벗어날 경우 에러 처리
			printf("row/col out of range!\n");
			return -1;
		}
		for (int i = 0; i < row; i++) {
			if (fscanf(fp, "%100s", buf) != 1) { //한 줄 입력을 읽지 못했을 경우
				fprintf(stderr, "buf error!\n");
				fclose(fp);
				return -1;
			}
			for (int j = 0; j < col; j++) { //2차원 배열에 저장
				arr[i][j] = buf[j];
			}
		}
		result = cover_range(arr, row, col);

		row = col = 0; //행과 열 초기화
		printf("result : %d\n", result); //결과 출력
		result = 0; //결과 값 초기화
	}

	fclose(fp);
	return 0;
}


void see(char arr[][101], int row, int col) {
	for (int i = 0; i < row; i++) {
		for(int j = 0; j < col; j++) {
			printf("%c ", arr[i][j]);
		}
		printf("\n");
	}
}


int cover_range(char arr[][101], int row, int col) {
    int uncovered_houses = 0;
    char dat[101][101] = {0, };
    int cover_a[12][2] = { //A급 중계기의 커버 범위
        {-1, 0}, {1, 0}, {0, -1}, {0, 1},
        {-2, 0}, {2, 0}, {0, -2}, {0, 2},
        {-3, 0}, {3, 0}, {0, -3}, {0, 3}
    };
    int cover_b[8][2] = { //B급 중계기의 커버 범위
        {-1, 0}, {1, 0}, {0, -1}, {0, 1},
        {-2, 0}, {2, 0}, {0, -2}, {0, 2},
    };
    int cover_c[4][2] = { //C급 중계기의 커버 범위
        {-1, 0}, {1, 0}, {0, -1}, {0, 1},
    };
    //배열 3개를 하나로 묶어서 처리해도 되긴하지만 가독성이 나빠서 일단은 이렇게 처리


    for(int i = 0; i < row; i++){ //배열 복사 *사실 굳이 안 해도 되긴 함 하지만 추후 유지보수를 위해
        memcpy(dat[i], arr[i], sizeof(char) * col);
    }
    
    for(int i = 0; i < row; i++){
        for(int j = 0; j < col; j++){
            if(dat[i][j] == 'A'){
                for(int k = 0; k < 12; k++){
                    int ni = i + cover_a[k][0];
                    int nj = j + cover_a[k][1];
                    if(ni >= 0 && ni < row && nj >= 0 && nj < col && dat[ni][nj] == 'H'){
                        dat[ni][nj] = 'P'; //커버 처리
                    }
                }
            }
            else if(dat[i][j] == 'B'){
                for(int k = 0; k < 8; k++){
                    int ni = i + cover_b[k][0];
                    int nj = j + cover_b[k][1];
                    if(ni >= 0 && ni < row && nj >= 0 && nj < col && dat[ni][nj] == 'H'){
                        dat[ni][nj] = 'P'; //커버 처리
                    }
                }
            }
            else if(dat[i][j] == 'C'){
                for(int k = 0; k < 4; k++){
                    int ni = i + cover_c[k][0];
                    int nj = j + cover_c[k][1];
                    if(ni >= 0 && ni < row && nj >= 0 && nj < col && dat[ni][nj] == 'H'){
                        dat[ni][nj] = 'P'; //커버 처리
                    }
                }
            }
        }
    }
    for(int i = 0; i < row; i++){
        for(int j = 0; j < col; j++){
            if(dat[i][j] == 'H'){
                uncovered_houses++; //커버하지 못한 집 개수 세기
            }
        }
    }
    // see(dat, row, col); //디버깅용 출력
    // printf("uncovered_houses: %d\n", uncovered_houses); //디버깅용 출력
    // see(arr, row, col); //디버깅용 출력
    // while(getchar() != '\n'); //디버깅용 일시정지
    return uncovered_houses;
}  