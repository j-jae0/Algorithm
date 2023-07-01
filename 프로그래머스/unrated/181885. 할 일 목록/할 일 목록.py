def solution(todo_list, finished):
    return [td for td, f in zip(todo_list, finished) if not f]