import sys

if __name__ == "__main__":
    day = sys.argv[1]
    try:
        if day == "1":
            import puzzle_1.part_1.part_1 as d1_part1
            import puzzle_1.part_2.part_2 as d1_part2

            result_part_1 = d1_part1.sonarSweep()
            result_part_2 = d1_part2.sonarSweepSlidingWindow()
            print(result_part_1)
            print(result_part_2)
        elif day == "5":
            import puzzle_5.part_1.part_1 as d5_part1

            result_part_1 = d5_part1.hidrotermalVenture()
            print(result_part_1)
        else:
            print("Nothing")
            
    except:
        raise RuntimeError(f"Check if you called program correctly")