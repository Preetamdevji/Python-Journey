for i in range(2, 21):
    with open(f"filehandling\Multiplication_table{i}.txt", 'wt') as f:
        for j in range(1, 11):
            f.write(f"{i}x{j}= {i*j}")
            if j!=10:
                f.write('\n')

            

