<!DOCTYPE html>
<html lang="en">
<head>
  <title>Worldwide Top News</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
  
  <style>
	.card {
		margin: 20px auto;
		max-width: 500px;
	}
	.card .card-body {
		min-height: 220px;
		background-size: cover;
		background-repeat: no-repeat;
		background-position: center;
		padding: 0;
		position: relative;
	}
	.card .card-body p {
		background-color: #000000b8;
		color: #FFF;
		padding: 10px;
		position: absolute;
		left: 0;
		right: 0;
		bottom: 0;
		margin: 0;
	}
	h2 {
		margin: 30px 0;
	}
  </style>
</head>
<body> 
	<div class="container">
		<h2 class="text-center">Worldwide Top News</h2>
		<?php
		$data = exec('python scrapping.py');
		$data = json_decode($data, true);

		if($data) {
		foreach($data as $d) {
			$image = !empty($d['image']) ? $d['image'] : 'img/no-image.png';
			?>
			<div class="card">
				<div class="card-header"><?= $d['heading'] ?></div>
				<div class="card-body" style="background-image: url('<?= $image ?>')">
					<p><?= $d['content'] ?></p>
				</div>
				<div class="card-footer">
					<div class="row">
						<div class="col-md-6"><a target="_blank" href="<?= $d['url'] ?>"><?= $d['reference'] ?></a></div>
						<div class="col-md-6 text-right"><a href="<?= $d['link'] ?>" target="_blank">Read more</a></div>
					</div>
				</div>
			</div>
		<?php } ?>
		<?php } else { ?>
			<h3>Not found</h3>
		<?php } ?>
	</div>
</body>
</html>