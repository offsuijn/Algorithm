package baekjoon.Interface_form;

/**
 * Java Stack Interface
 *
 * @param <E> stack의 element 타
 */

public interface StackInterface<E> {

    /**
     * 스택의 맨 위에 요소를 추가한다.
     *
     * @param item 스택에 추가할 요소
     * @return 스택에 추가된 요소
     */
    E push(E item);

    /**
     * 스택의 맨 위에 있는 요소를 제거하고 그 요소를 반환한다.
     *
     * @return 제거된 요소
     */
    E pop();

    /**
     * 스택의 최상단 요소를 제거하지 않고 반환한다.
     *
     * @return 스택 최상단 요소
     */
    E peek();


    /**
     * 스택의 최상단부터 특정 요소가 몇 번째 위치에 있는지 반환한다.
     * 원소가 중복될 경우 가장 위에 있는 요소의 위치가 반환된다.
     *
     * @param value 스택에서 위치를 찾을 요소
     * @return 스택의 최상단부터 처음으로 해당 요소가 나타나는 위치를 반환
     *         없을 경우 -1 반환
     */
    int search(Object value);

    /**
     * 스택의 요소 개수를 반환한다.
     *
     * @return 스택의 요소 개수
     */
    int size();

    /**
     * 스택에 있는 모든 요소 삭제
     */
    void clear();

    boolean empty();

}
