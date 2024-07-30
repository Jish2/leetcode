from leetcode import get_submission_calendar
from readme_heatmap.utils import get_quartiles, get_date_map_from_timestamp_map
from readme_heatmap.generate_images import generate_images


def main():
    submission_calendar = get_submission_calendar("jgoon3")
    quartiles = get_quartiles(submission_calendar)
    date_map = get_date_map_from_timestamp_map(submission_calendar)

    generate_images(date_map, quartiles, outDir="./")


if __name__ == "__main__":
    main()
