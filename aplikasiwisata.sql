-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 07, 2020 at 11:37 AM
-- Server version: 10.4.16-MariaDB
-- PHP Version: 7.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aplikasiwisata`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `person_id` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `person_id`, `nama`, `created_date`) VALUES
(1, 1, 'Mas Admin', '2020-12-01 16:15:52');

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `id` int(11) NOT NULL,
  `person_id` int(11) NOT NULL,
  `nama_lengkap` varchar(255) NOT NULL,
  `no_ktp` varchar(255) NOT NULL,
  `no_hp` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`id`, `person_id`, `nama_lengkap`, `no_ktp`, `no_hp`) VALUES
(1, 2, 'Dummy Customer', '3509220101010001', '0812345678901');

-- --------------------------------------------------------

--
-- Table structure for table `destinasi_dalam_paket`
--

CREATE TABLE `destinasi_dalam_paket` (
  `id` int(11) NOT NULL,
  `paket` int(11) NOT NULL,
  `destinasi` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `destinasi_dalam_paket`
--

INSERT INTO `destinasi_dalam_paket` (`id`, `paket`, `destinasi`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 2, 1),
(5, 2, 2),
(6, 2, 3),
(7, 2, 11),
(8, 2, 4),
(9, 3, 8),
(10, 3, 9),
(11, 3, 10),
(12, 4, 8),
(13, 4, 9),
(14, 4, 10),
(15, 4, 12),
(16, 4, 13),
(17, 5, 5),
(18, 5, 6),
(19, 5, 7);

-- --------------------------------------------------------

--
-- Table structure for table `destinasi_wisata`
--

CREATE TABLE `destinasi_wisata` (
  `id` int(11) NOT NULL,
  `nama_tempat` varchar(255) NOT NULL,
  `kota` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `destinasi_wisata`
--

INSERT INTO `destinasi_wisata` (`id`, `nama_tempat`, `kota`) VALUES
(1, 'Watu Ulo', 1),
(2, 'Rembangan', 1),
(3, 'J88', 1),
(4, 'Dira Garden', 1),
(5, 'Malioboro', 2),
(6, 'Borobudur', 2),
(7, 'Merapi Park', 2),
(8, 'Jatim Park', 3),
(9, 'Jatim Park 2', 3),
(10, 'Jatim Park 3', 3),
(11, 'Papuma', 1),
(12, 'Kebun Apel Batu', 3),
(13, 'Dino Park', 3);

-- --------------------------------------------------------

--
-- Table structure for table `kota`
--

CREATE TABLE `kota` (
  `id` int(11) NOT NULL,
  `nama_kota` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `kota`
--

INSERT INTO `kota` (`id`, `nama_kota`) VALUES
(1, 'Jember'),
(2, 'Yogyakarta'),
(3, 'Malang');

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

CREATE TABLE `order` (
  `id` int(11) NOT NULL,
  `kode_booking` varchar(255) NOT NULL,
  `customer` int(11) NOT NULL,
  `id_paket_wisata` int(11) NOT NULL,
  `id_status_order` enum('menunggu_pembayaran','menunggu_verifikasi','terbayar','menunggu_pembatalan','dibatalkan') NOT NULL,
  `tanggal_berangkat` date NOT NULL,
  `tanggal_pulang` date NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `order`
--

INSERT INTO `order` (`id`, `kode_booking`, `customer`, `id_paket_wisata`, `id_status_order`, `tanggal_berangkat`, `tanggal_pulang`, `created_date`) VALUES
(1, 'JBR10001', 1, 1, 'menunggu_pembayaran', '2020-12-09', '2020-12-12', '2020-12-07 10:34:25');

-- --------------------------------------------------------

--
-- Table structure for table `order_detail`
--

CREATE TABLE `order_detail` (
  `id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `nama_peserta` varchar(255) NOT NULL,
  `no_ktp` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `order_detail`
--

INSERT INTO `order_detail` (`id`, `order_id`, `nama_peserta`, `no_ktp`) VALUES
(1, 1, 'Dummy Customer', '3509220101010001');

-- --------------------------------------------------------

--
-- Table structure for table `order_status_string`
--

CREATE TABLE `order_status_string` (
  `id_status_order` enum('menunggu_pembayaran','menunggu_verifikasi','terbayar','menunggu_pembatalan','dibatalkan') NOT NULL,
  `keterangan` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `order_status_string`
--

INSERT INTO `order_status_string` (`id_status_order`, `keterangan`) VALUES
('menunggu_pembayaran', 'Menunggu Pembayaran'),
('menunggu_verifikasi', 'Menunggu Verifikasi'),
('terbayar', 'Terbayar'),
('menunggu_pembatalan', 'Menunggu Pembatalan'),
('dibatalkan', 'Dibatalkan');

-- --------------------------------------------------------

--
-- Table structure for table `paket_wisata`
--

CREATE TABLE `paket_wisata` (
  `id` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `kota` int(11) NOT NULL,
  `durasi` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `paket_wisata`
--

INSERT INTO `paket_wisata` (`id`, `nama`, `kota`, `durasi`) VALUES
(1, 'Paket Jember 3 Hari', 1, 3),
(2, 'Paket Jember 1 Minggu', 1, 7),
(3, 'Paket Malang 3 Hari', 3, 3),
(4, 'Paket Malang 5 Hari', 3, 5),
(5, 'Paket Yogyakarta 3 Hari', 2, 3),
(6, 'Paket Yogyakarta 1 Minggu', 2, 7);

-- --------------------------------------------------------

--
-- Table structure for table `pembayaran`
--

CREATE TABLE `pembayaran` (
  `id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `kode_bukti` varchar(255) NOT NULL,
  `status_verifikasi` enum('belum_verifikasi','telah_verifikasi') NOT NULL,
  `petugas_verifikasi` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `person`
--

CREATE TABLE `person` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('admin','customer') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `person`
--

INSERT INTO `person` (`id`, `email`, `password`, `role`) VALUES
(1, 'admin@aplikasiwisata', 'admin', 'admin'),
(2, 'dummy_cust@email.com', 'dummy', 'customer');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`),
  ADD KEY `person_id` (`person_id`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `person_id` (`person_id`);

--
-- Indexes for table `destinasi_dalam_paket`
--
ALTER TABLE `destinasi_dalam_paket`
  ADD PRIMARY KEY (`id`),
  ADD KEY `paket` (`paket`),
  ADD KEY `destinasi` (`destinasi`);

--
-- Indexes for table `destinasi_wisata`
--
ALTER TABLE `destinasi_wisata`
  ADD PRIMARY KEY (`id`),
  ADD KEY `kota` (`kota`);

--
-- Indexes for table `kota`
--
ALTER TABLE `kota`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `kode_booking` (`kode_booking`),
  ADD KEY `customer` (`customer`),
  ADD KEY `id_paket_wisata` (`id_paket_wisata`),
  ADD KEY `id_status_order` (`id_status_order`);

--
-- Indexes for table `order_detail`
--
ALTER TABLE `order_detail`
  ADD PRIMARY KEY (`id`),
  ADD KEY `order_id` (`order_id`);

--
-- Indexes for table `order_status_string`
--
ALTER TABLE `order_status_string`
  ADD PRIMARY KEY (`id_status_order`);

--
-- Indexes for table `paket_wisata`
--
ALTER TABLE `paket_wisata`
  ADD PRIMARY KEY (`id`),
  ADD KEY `kota` (`kota`);

--
-- Indexes for table `pembayaran`
--
ALTER TABLE `pembayaran`
  ADD PRIMARY KEY (`id`),
  ADD KEY `order_id` (`order_id`),
  ADD KEY `petugas_verifikasi` (`petugas_verifikasi`);

--
-- Indexes for table `person`
--
ALTER TABLE `person`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `destinasi_dalam_paket`
--
ALTER TABLE `destinasi_dalam_paket`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `destinasi_wisata`
--
ALTER TABLE `destinasi_wisata`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `kota`
--
ALTER TABLE `kota`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `order`
--
ALTER TABLE `order`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `order_detail`
--
ALTER TABLE `order_detail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `paket_wisata`
--
ALTER TABLE `paket_wisata`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `pembayaran`
--
ALTER TABLE `pembayaran`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `person`
--
ALTER TABLE `person`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `admin`
--
ALTER TABLE `admin`
  ADD CONSTRAINT `admin_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `person` (`id`);

--
-- Constraints for table `customers`
--
ALTER TABLE `customers`
  ADD CONSTRAINT `customers_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `person` (`id`);

--
-- Constraints for table `destinasi_dalam_paket`
--
ALTER TABLE `destinasi_dalam_paket`
  ADD CONSTRAINT `destinasi_dalam_paket_ibfk_1` FOREIGN KEY (`paket`) REFERENCES `paket_wisata` (`id`),
  ADD CONSTRAINT `destinasi_dalam_paket_ibfk_2` FOREIGN KEY (`destinasi`) REFERENCES `destinasi_wisata` (`id`);

--
-- Constraints for table `destinasi_wisata`
--
ALTER TABLE `destinasi_wisata`
  ADD CONSTRAINT `destinasi_wisata_ibfk_1` FOREIGN KEY (`kota`) REFERENCES `kota` (`id`);

--
-- Constraints for table `order`
--
ALTER TABLE `order`
  ADD CONSTRAINT `order_ibfk_1` FOREIGN KEY (`customer`) REFERENCES `customers` (`id`),
  ADD CONSTRAINT `order_ibfk_2` FOREIGN KEY (`id_paket_wisata`) REFERENCES `paket_wisata` (`id`),
  ADD CONSTRAINT `order_ibfk_3` FOREIGN KEY (`id_status_order`) REFERENCES `order_status_string` (`id_status_order`);

--
-- Constraints for table `order_detail`
--
ALTER TABLE `order_detail`
  ADD CONSTRAINT `order_detail_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `order` (`id`);

--
-- Constraints for table `paket_wisata`
--
ALTER TABLE `paket_wisata`
  ADD CONSTRAINT `paket_wisata_ibfk_1` FOREIGN KEY (`kota`) REFERENCES `kota` (`id`);

--
-- Constraints for table `pembayaran`
--
ALTER TABLE `pembayaran`
  ADD CONSTRAINT `pembayaran_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `order` (`id`),
  ADD CONSTRAINT `pembayaran_ibfk_2` FOREIGN KEY (`petugas_verifikasi`) REFERENCES `admin` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
