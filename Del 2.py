import shutil

def check_disk_space(path="/", threshold_gb=5):
    total, used, free = shutil.disk_usage(path)
    free_gb = free / (1024**3)

    print(f"Fritt utrymme: {free_gb:.2f} GB")

    if free_gb < threshold_gb:
        print("VARNING: Lågt diskutrymme!")
    else:
        print("Tillräckligt med utrymme tillgängligt.")

if __name__ == "__main__":
    check_disk_space("/", threshold_gb=5)
