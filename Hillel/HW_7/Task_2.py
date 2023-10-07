def check_string(input_sent: str) -> bool:
    count_number = 0
    for word in (
            input_sent
            .replace(",", "")
            .split(" ")
    ):
        if word.isalpha():
            count_number += 1
        else:
            count_number = 0

    if count_number >= 3:
        return True

    return False


print(
    check_string(
        input_sent="Some 1 issue 2 2milk some some"
    )
)