
$correct = 0
$total = 0
while (1) {
    python ./generate_random_testcase.py > input.txt
    $ans1 = (Get-Content input.txt | python test.py)
    $ans2 = (Get-Content input.txt | python ./guchoku.py)
    $total++
    if ($ans1 -ne $ans2) {
        Write-Host "Wrong Answer"
        Write-Host "mytry: ${ans1}"
        Write-Host "gucho: ${ans2}"
        exit
    }
    else {
        $correct++
        # Write-Host "Correct"
        Write-Host "correct ${correct} / ${total}"
    }
}