$(document).ready(function () {
    let miningInterval;
    let miningInProgress = false;

    $("#start-mining").click(function () {
        startMining();
    });

    $("#stop-mining").click(function () {
        stopMining();
    });

    function startMining() {
        miningInProgress = true;
        $("#start-mining").prop("disabled", true);
        $("#stop-mining").prop("disabled", false);
        $("#progress-text").text("Mining in progress...");
        miningInterval = setInterval(updateMiningProgress, 100);
    }

    function stopMining() {
        miningInProgress = false;
        $("#start-mining").prop("disabled", false);
        $("#stop-mining").prop("disabled", true);
        clearInterval(miningInterval);
        $("#progress-text").text("Mining stopped.");
    }

    function updateMiningProgress() {
        // Simulate mining progress
        let progress = parseInt($("#mining-progress-bar").val());
        if (progress < 100) {
            progress += Math.floor(Math.random() * 10); // Update progress randomly
            $("#mining-progress-bar").val(progress);
        } else {
            stopMining();
        }
    }
});
