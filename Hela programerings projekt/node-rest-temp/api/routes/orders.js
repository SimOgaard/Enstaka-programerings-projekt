const express = require("express");
const router = express.Router();

router.get("/", (res) => {
    res.status(200).json({
        message: "orders were fetched"
    });
});

router.get("/:orderId", (req, res,) => {
    res.status(200).json({
        message: "order details",
        orderId: req.params.orderId
    });
});

module.exports = router;