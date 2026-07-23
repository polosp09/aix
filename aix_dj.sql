-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 12, 2025 at 04:20 PM
-- Server version: 10.5.26-MariaDB
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aix_dj`
--

-- --------------------------------------------------------

--
-- Table structure for table `aix_absencedatemodel`
--

CREATE TABLE `aix_absencedatemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `date` date NOT NULL,
  `is_half_day` tinyint(1) NOT NULL,
  `absence_type_id` char(32) NOT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_absencetypemodel`
--

CREATE TABLE `aix_absencetypemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_accountcodeprefixmodel`
--

CREATE TABLE `aix_accountcodeprefixmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `prefixcode` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_accountmodel`
--

CREATE TABLE `aix_accountmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(10) NOT NULL,
  `name` varchar(100) NOT NULL,
  `role` varchar(25) NOT NULL,
  `balance_type` varchar(6) NOT NULL,
  `locked` tinyint(1) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `coa_id` char(32) NOT NULL,
  `parent_id` char(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_accountmodel`
--

INSERT INTO `aix_accountmodel` (`created`, `updated`, `uuid`, `code`, `name`, `role`, `balance_type`, `locked`, `active`, `coa_id`, `parent_id`) VALUES
('2024-02-24 02:37:03.332888', '2024-02-24 02:37:03.332888', '021b2e6c411f4be49d8be129bae7075f', '6254', 'Water', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.545275', '2024-08-28 08:29:25.545275', '02571e530ae34f419382f0a955ec918f', '3010', 'Capital Account 1', 'eq_capital', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.332888', '2024-02-24 02:37:03.332888', '03705be8d2dc43fd972af6c601243403', '6280', 'Taxes', 'ex_taxes', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', '05b5ffc65f1d4a23bf64b71c8b030a0b', '6230', 'Postage', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', '064689169f814e0bb559e1f72658e82a', '2050', 'Current Maturities LT Debt', 'lia_cl_ltd_mat', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.547264', '2024-08-28 08:29:25.547264', '06d5afb156d848e092c3e2745570871f', '6250', 'Maintenance & Repairs', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', '07600d5fb68449ba8571f451e21f58e6', '4010', 'Sales Income', 'in_sales', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', '07b0e0ac3bdb413a994dc46beff3c96b', '2020', 'Wages Payable', 'lia_cl_wage_pay', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.546276', '2024-08-28 08:29:25.546276', '080a3cf313c54b04a5ce7b5dadcdcc7a', '6120', 'Insurance', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.330372', '2024-02-24 02:37:03.330372', '0ddc3a9298bd4cffaa7676fc360341bb', '1300', 'Prepaid Expenses', 'asset_ca_prepaid', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.330372', '2024-02-24 02:37:03.330372', '100846fca4c34f5684593663d3c530ea', '1200', 'Inventory', 'asset_ca_inv', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.545275', '2024-08-28 08:29:25.545275', '1108cb4401f648ca9964ac646c1f2d2f', '2070', 'Other Payables', 'lia_cl_other', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', '1252e79812db4d5b8b24114ef7ab9dc8', '6080', 'Employee Benefits', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.543268', '2024-08-28 08:29:25.543268', '12ec5f8690784321a5548b92ed9a2a43', '1100', 'Accounts Receivable', 'asset_ca_recv', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', '12f0cf6bb92f4ca2af3b130170d80497', '6220', 'Printing', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.546276', '2024-08-28 08:29:25.546276', '14197ce10e674923bd0d3ef93c95b20f', '6220', 'Printing', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.330372', '2024-02-24 02:37:03.330372', '147a212aae0843c7a71d9f95b526d9aa', '1641', 'Less: Vehicles Accumulated Depreciation', 'asset_ppe', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.543268', '2024-08-28 08:29:25.543268', '152c19500a364d3281411a43e6349b23', '1050', 'Short Term Investments', 'asset_ca_mkt_sec', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.544280', '2024-08-28 08:29:25.544280', '1bbe4cf017c2497ba18204603c21bc8f', '1611', 'Less: Buildings Accumulated Depreciation', 'asset_ppe', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', '1da61e9c10fa4d5490c5f696cf1bc46f', '2120', 'Bonds Payable', 'lia_ltl_bonds', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', '26691241a89d4806bd40460228710bd8', '3920', 'PPE Unrealized Gains/Losses', 'eq_adjustment', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', '2a42258d8fc04a8982890d6483d7d055', '2060', 'Deferred Revenues', 'lia_cl_def_rev', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', '2a96e2d275734198a5b9d1135b3d7bee', '6120', 'Insurance', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', '2d57dac7dfb848b1bf673390dd44d908', '6060', 'Commission Expense', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', '309cddeb4db94af0815bfd2a36217428', '2130', 'Mortgage Payable', 'lia_ltl_mortgage', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.332888', '2024-02-24 02:37:03.332888', '3204048f77314d5c85da32089715a51b', '6255', 'Lawn Care', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.545275', '2024-08-28 08:29:25.545275', '32122e8ecc61438fb980abd64b4df137', '3030', 'Capital Account 3', 'eq_capital', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', '351d55d4a01e4c9e925ffa23e616c645', '6070', 'Depreciation Expense', 'ex_cap', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.332888', '2024-02-24 02:37:03.332888', '355119d7f31a42a8a5e8317219d0f357', '6400', 'Vacancy', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.544280', '2024-08-28 08:29:25.544280', '3b3b43969b92411cbd787c103a5a5595', '1651', 'Less: Furniture & Fixtures Accumulated Depreciation', 'asset_ppe', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.546276', '2024-08-28 08:29:25.546276', '3c3360ce79e947d39f55cb30caceb237', '6140', 'Professional Fees', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.332888', '2024-02-24 02:37:03.332888', '3d23a15be7204801bd39052386f915d4', '6293', 'Gas', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.545275', '2024-08-28 08:29:25.545275', '408663ae320341749b23e39a9ccdb7be', '6030', 'Auto Expense', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.544280', '2024-08-28 08:29:25.544280', '40a887cec5a14230bc0c68a916162e8f', '2040', 'Short-Term Notes Payable', 'lia_cl_st_notes_payable', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.544280', '2024-08-28 08:29:25.544280', '40beb5f8c5b6460799003d3d9b87b7ca', '2060', 'Deferred Revenues', 'lia_cl_def_rev', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.330372', '2024-02-24 02:37:03.330372', '4177beb7a4d44f24b4f83a46b521f90a', '1510', 'Notes Receivable', 'asset_lti_notes', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.547264', '2024-08-28 08:29:25.547264', '417b903f71e74629a8c30999ac656e3b', '6270', 'Supplies', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.543268', '2024-08-28 08:29:25.543268', '433ab362962b4c1699375feeac611823', '1510', 'Notes Receivable', 'asset_lti_notes', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.332888', '2024-02-24 02:37:03.332888', '45f475bae59b4d359d9c80f97e547d21', '6292', 'Sewer', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.332888', '2024-02-24 02:37:03.332888', '469eef2901c74420bd3062b5cd31a00c', '6252', 'Repairs', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', '481021344f324845b5a07f5fd2e3be2e', '6130', 'Interest Expense', 'ex_interest', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.332888', '2024-02-24 02:37:03.332888', '4c893f985c5e48b28337c6a5f3bca89b', '6300', 'Property Management', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.547264', '2024-08-28 08:29:25.547264', '4d8675ca24b542a3a2524d488802a767', '6253', 'HOA', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.544280', '2024-08-28 08:29:25.544280', '4e20dd902f0549fd8f035d57ec8fa7ff', '1640', 'Vehicles', 'asset_ppe', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.543268', '2024-08-28 08:29:25.543268', '4e69855b236b4795a4eb06c5670dfae4', '1010', 'Cash', 'asset_ca_cash', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', '4f6bb20535f54f658a9cfb08965f6e63', '3020', 'Capital Account 2', 'eq_capital', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.330372', '2024-02-24 02:37:03.330372', '501a262df8234bf5a23e4c09840c0f44', '1100', 'Accounts Receivable', 'asset_ca_recv', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.544280', '2024-08-28 08:29:25.544280', '50bf869d68e4460b981b93b6e5cc95da', '1621', 'Less: Plant Accumulated Depreciation', 'asset_ppe', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.330372', '2024-02-24 02:37:03.330372', '50d58584c2974b7c99746ddaf628bcf6', '1620', 'Plant', 'asset_ppe', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.547264', '2024-08-28 08:29:25.547264', '53a3e765faa94565b00be883ad650467', '6254', 'Water', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.544280', '2024-08-28 08:29:25.544280', '54f6a170209a4ed7887c58731c8d0e24', '2050', 'Current Maturities LT Debt', 'lia_cl_ltd_mat', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.544280', '2024-08-28 08:29:25.544280', '572d0a7c71284703bf17af50aefa9b0a', '2030', 'Interest Payable', 'lia_cl_wage_pay', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.543268', '2024-08-28 08:29:25.543268', '580b661385104f229ab25921a7addb51', '1530', 'Securities', 'asset_lti_sec', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.330372', '2024-02-24 02:37:03.330372', '58d6aceabe744d56b4ab89213be24741', '1101', 'Uncollectibles', 'asset_ca_uncoll', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.330372', '2024-02-24 02:37:03.330372', '59264f044ff84d72bad5c3eb0d4ce939', '1631', 'Less: Equipment Accumulated Depreciation', 'asset_ppe', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.330372', '2024-02-24 02:37:03.330372', '5954445973724ae9a458dde8991f1560', '1530', 'Securities', 'asset_lti_sec', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.330372', '2024-02-24 02:37:03.330372', '5a173bfee7f645e7a101ed26d9d9c6e9', '1610', 'Buildings', 'asset_ppe', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.546276', '2024-08-28 08:29:25.546276', '5b84bb8f84f643e99fe8a02f36dc30bc', '6180', 'Meals & Entertainment', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', '5c9c5754f6c744f9bc7966b803466f68', '3110', 'Common Stock', 'eq_stock_c', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.332888', '2024-02-24 02:37:03.332888', '62c498a870c7457ebcb326af72bf39f8', '6294', 'Garbage', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.545275', '2024-08-28 08:29:25.545275', '65ea95a18f314e2f85c99d8baa8b44a2', '2130', 'Mortgage Payable', 'lia_ltl_mortgage', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.332888', '2024-02-24 02:37:03.332888', '660a56bc60b64b68a197d82c0db9166d', '6295', 'Electricity', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', '6887dc626745439ca6f005223bd5c150', '1651', 'Less: Furniture & Fixtures Accumulated Depreciation', 'asset_ppe', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.545275', '2024-08-28 08:29:25.545275', '6ab36e56e4ab444bbac6895e345e459f', '4010', 'Sales Income', 'in_sales', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.330372', '2024-02-24 02:37:03.330372', '6cfe7e3ecb624f088871bc7b5e353fa9', '1640', 'Vehicles', 'asset_ppe', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.330372', '2024-02-24 02:37:03.330372', '6ee1ba7714354c01bc3338ca2c27e5db', '1630', 'Equipment', 'asset_ppe', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.330372', '2024-02-24 02:37:03.330372', '6fe4fe62eba44a3bbf5ca23fdd2c5ae5', '1010', 'Cash', 'asset_ca_cash', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', '7085fadb87454a26a4f87c27994df01f', '4020', 'Passive Income', 'in_pass', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.330372', '2024-02-24 02:37:03.330372', '716f80390d0a487992933aef0433169c', '1621', 'Less: Plant Accumulated Depreciation', 'asset_ppe', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.545275', '2024-08-28 08:29:25.545275', '73c146220e0d412ba7152a4832aa3f62', '3920', 'PPE Unrealized Gains/Losses', 'eq_adjustment', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', '764913ce8a34462fbc6ac49da2fa7a79', '2010', 'Accounts Payable', 'lia_cl_acc_pay', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.543268', '2024-08-28 08:29:25.543268', '76a548fb110e49b48c3187d83eb46cd1', '1200', 'Inventory', 'asset_ca_inv', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.546276', '2024-08-28 08:29:25.546276', '77ee67eaf80e4b699268102e8b790b59', '6070', 'Depreciation Expense', 'ex_cap', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.547264', '2024-08-28 08:29:25.547264', '786f532b7e604f5ba0e7246a438e9568', '6240', 'Rent', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.543268', '2024-08-28 08:29:25.543268', '7a3ec0984dfd497fa55b7b238fe55dae', '1610', 'Buildings', 'asset_ppe', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.545275', '2024-08-28 08:29:25.545275', '7b222c30d54a4061bea36fb0acb0edd8', '4020', 'Passive Income', 'in_pass', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.332888', '2024-02-24 02:37:03.332888', '7d68791c7b2f42bba2b9c23359b28c8a', '6260', 'Salaries', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.332888', '2024-02-24 02:37:03.332888', '804e8b94869e4f09aacc2ec2b9a36123', '6251', 'Maintenance', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.547264', '2024-08-28 08:29:25.547264', '81df5a7f71534b2f92131e7facb2c560', '6260', 'Salaries', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.548289', '2024-08-28 08:29:25.548289', '83bc6b56ce1747928612527670326adf', '6400', 'Vacancy', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.547264', '2024-08-28 08:29:25.547264', '85e179f7caba47958db0a5d40914384a', '6295', 'Electricity', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', '861340916617419db90fc16a21750b68', '6150', 'License Expense', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', '8693069e830c4cf29979831ea344df0b', '6180', 'Meals & Entertainment', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.546276', '2024-08-28 08:29:25.546276', '87aee6555fc64e3aae98c8b5feb95189', '6150', 'License Expense', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', '8877aa33c64448e6ae05c5c84fa87c3f', '6050', 'Bank Charges', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', '8a44904d80e5442aaef6b865d20ae45b', '6140', 'Professional Fees', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.332888', '8b5d9ab2d7254cc9b6d17fc121cdf013', '6250', 'Maintenance & Repairs', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.546276', '2024-08-28 08:29:25.546276', '8ccb271ab5ca4a91b93f18db0037054d', '6090', 'Freight', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.546276', '2024-08-28 08:29:25.546276', '930ca0e155a44a8faf0a59fe757f13dd', '6080', 'Employee Benefits', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.545275', '2024-08-28 08:29:25.545275', '9389ac9fb7854db09190211e7df9981a', '5010', 'Cost of Goods Sold', 'ex_cogs', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.546276', '2024-08-28 08:29:25.546276', '94289caa261b42e8a50dca4ede31a5bb', '6110', 'Gifts', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.332888', '2024-02-24 02:37:03.332888', '963235aebf704154919b91161f14e1f2', '7510', 'Misc. Expense', 'ex_other', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.545275', '2024-08-28 08:29:25.545275', '976770307ed842569b6966e1c0671b35', '3020', 'Capital Account 2', 'eq_capital', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', '97cfe557e4894980b5fe509e5ab9ae1e', '6020', 'Amortization', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.545275', '2024-08-28 08:29:25.545275', '99ba4e885485476cacb384d8cffb53de', '6020', 'Amortization', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.330372', '2024-02-24 02:37:03.330372', '9ae3f6908acb492d99cb2d6ae6c7897f', '1050', 'Short Term Investments', 'asset_ca_mkt_sec', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', '9bbc62d1396d47fcad5da83c9cad79df', '1920', 'PPE Unrealized Gains/Losses', 'asset_adjustment', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.544280', '2024-08-28 08:29:25.544280', '9cf0bc718de348278fa7db1d593ac7d4', '1620', 'Plant', 'asset_ppe', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.545275', '2024-08-28 08:29:25.546276', '9d121b025d084f159bd001597dfe6669', '6040', 'Bad Debt', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.544280', '2024-08-28 08:29:25.544280', 'a40810d7c0254632bba382108c4661f4', '1820', 'Intellectual Property', 'asset_ia', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.547264', '2024-08-28 08:29:25.547264', 'a64f78806b4d42dcba75d7cbd0eb20fa', '6280', 'Taxes', 'ex_taxes', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.545275', '2024-08-28 08:29:25.545275', 'a6efa567511b4287bb853b435d6a8d4a', '2110', 'Long Term Notes Payable', 'lia_ltl_notes', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.544280', '2024-08-28 08:29:25.544280', 'ab6030b78f214d5994527bfcacbb3102', '2020', 'Wages Payable', 'lia_cl_wage_pay', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', 'abead60ecd8449c9b59b44529fd8435c', '6170', 'Maintenance Expense', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.545275', '2024-08-28 08:29:25.545275', 'ad581c43ad1f4ec68155f38a2472d2d7', '4030', 'Property Sales Income', 'in_other', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.332888', '2024-02-24 02:37:03.332888', 'ad8aa0c6e8f24a5e97aff9ffc61152fb', '6253', 'HOA', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.546276', '2024-08-28 08:29:25.546276', 'b20fd9ff79544a84b12b1d9350840ff7', '6170', 'Maintenance Expense', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.330372', '2024-02-24 02:37:03.330372', 'b5123fd7034d421081f200adaee108df', '1520', 'Land', 'asset_lti_land', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', 'b547788157374eb29e240b597fcdbb97', '6110', 'Gifts', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.545275', '2024-08-28 08:29:25.545275', 'b652558d3b70438bb17e9fc677a1182f', '3910', 'Available for Sale', 'eq_adjustment', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.545275', '2024-08-28 08:29:25.545275', 'b7172b738175428faad94c9bf76bf85d', '6010', 'Advertising', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', 'b835b83191b24661b61075ab898d8f75', '6210', 'Payroll Taxes', 'ex_taxes', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.544280', '2024-08-28 08:29:25.544280', 'b8e2f0ca2a9e499eac7876443cd0caa6', '1630', 'Equipment', 'asset_ppe', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.547264', '2024-08-28 08:29:25.547264', 'ba42ea280f4645908c2a6540b2e7528c', '6292', 'Sewer', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', 'ba7d74f47bbf45748673a5177db11621', '2040', 'Short-Term Notes Payable', 'lia_cl_st_notes_payable', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.544280', '2024-08-28 08:29:25.544280', 'bbba04655e9146ecb0a5d6f7fdbe1ad0', '1910', 'Securities Unrealized Gains/Losses', 'asset_adjustment', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.547264', '2024-08-28 08:29:25.547264', 'bc7566a39b174b55ba06848f8a94eaa3', '6290', 'Utilities', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.548289', '2024-08-28 08:29:25.548289', 'bdc2eb72400240f3a9cb2001121ac711', '7510', 'Misc. Expense', 'ex_other', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', 'bdeb7fa2061e488a9b463a0f0c55cc28', '1810', 'Goodwill', 'asset_ia', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', 'bf985619448445d48f4cd0d379bd238f', '3010', 'Capital Account 1', 'eq_capital', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', 'c0c5ee1d9e6f47dd86b22297b3b5b233', '6030', 'Auto Expense', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.545275', '2024-08-28 08:29:25.545275', 'c44aa322cfca439495209a56ba916139', '3110', 'Common Stock', 'eq_stock_c', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', 'c468e949c9b14a719c20d028f97dc7f2', '6040', 'Bad Debt', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', 'c4aecc7161e1459780a39826ddee6799', '6240', 'Rent', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.544280', '2024-08-28 08:29:25.544280', 'c4cc7350d7594631a0eb4d479fca1ec0', '1641', 'Less: Vehicles Accumulated Depreciation', 'asset_ppe', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', 'c578e259876045c590861c322517c777', '3030', 'Capital Account 3', 'eq_capital', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.332888', '2024-02-24 02:37:03.332888', 'c889f6d8fcc3493dad513c604108d652', '6290', 'Utilities', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', 'cbbdf1f977354bc4bdd1b6af5aa996bd', '6010', 'Advertising', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.546276', '2024-08-28 08:29:25.546276', 'cc6f255666ca40f7b6113edf5416746d', '6210', 'Payroll Taxes', 'ex_taxes', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', 'ccbf1dda6f6847cca5c308dbd3e85b12', '5010', 'Cost of Goods Sold', 'ex_cogs', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.546276', '2024-08-28 08:29:25.546276', 'cdc9e09622c4444dad32c9f082df129b', '6130', 'Interest Expense', 'ex_interest', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.545275', '2024-08-28 08:29:25.545275', 'ce3d478c3f0b492ebbbd7ba299331727', '2120', 'Bonds Payable', 'lia_ltl_bonds', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.330372', '2024-02-24 02:37:03.330372', 'cf4147528320449d90b124af12862a8d', '1611', 'Less: Buildings Accumulated Depreciation', 'asset_ppe', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.547264', '2024-08-28 08:29:25.547264', 'd1e1086d38694b5e9f5a9d199458705d', '6230', 'Postage', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', 'd20cb1b980884c19917fa8becfc1c3bb', '2030', 'Interest Payable', 'lia_cl_wage_pay', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', 'd4541078404b406089c2e4278dea9dcf', '4030', 'Property Sales Income', 'in_other', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', 'd4e0ff453ed3460e88901c2ce9d497cd', '2070', 'Other Payables', 'lia_cl_other', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', 'd5ad5ae261a14bd9ba6f74a33d7d9f55', '2110', 'Long Term Notes Payable', 'lia_ltl_notes', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', 'd6f61896cd284f53b297681207603d8d', '3910', 'Available for Sale', 'eq_adjustment', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.546276', '2024-08-28 08:29:25.546276', 'd7d2ff5d48d94fc4b9f25a940bdb2e37', '6060', 'Commission Expense', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.544280', '2024-08-28 08:29:25.544280', 'db37ad93d40c4bdfb921fc65c1ee2efe', '1810', 'Goodwill', 'asset_ia', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', 'ddb8d915fde94b2ba4a0096a713442b9', '1820', 'Intellectual Property', 'asset_ia', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.543268', '2024-08-28 08:29:25.543268', 'de3785e25bbc490483b39843f47113ff', '1300', 'Prepaid Expenses', 'asset_ca_prepaid', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.545275', '2024-08-28 08:29:25.545275', 'e0ab0feb135a482baeb17b07d93e9c64', '3120', 'Preferred Stock', 'eq_stock_p', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.332888', '2024-02-24 02:37:03.332888', 'e17154789ca64a7fab4ec4bce02676dd', '7010', 'Misc. Revenue', 'in_other', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.547264', '2024-08-28 08:29:25.547264', 'e204956970f64d2ebb4ae7df2c184d84', '6294', 'Garbage', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.543268', '2024-08-28 08:29:25.543268', 'e7f6b4cf97d347cb904fd58cdba19761', '1520', 'Land', 'asset_lti_land', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.332888', '2024-02-24 02:37:03.332888', 'ea4e1e238f47462ca3c49fb58476ef6f', '6270', 'Supplies', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.544280', '2024-08-28 08:29:25.544280', 'edfccbde3c98406194cb3306a907278c', '1920', 'PPE Unrealized Gains/Losses', 'asset_adjustment', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.547264', '2024-08-28 08:29:25.547264', 'ee3d813bc6f8404fb8088becfbce50b7', '6255', 'Lawn Care', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', 'f03b3c4a76cb44c6a9ddbc532da25d5a', '3120', 'Preferred Stock', 'eq_stock_p', 'credit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.544280', '2024-08-28 08:29:25.544280', 'f09822a1f5d943c882c358f9091b34f6', '1650', 'Furniture & Fixtures', 'asset_ppe', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.546276', '2024-08-28 08:29:25.546276', 'f13f340c39444a4f9e5d62240d2cf119', '6050', 'Bank Charges', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.547264', '2024-08-28 08:29:25.547264', 'f45d3e6dd1684c218e2abd2ec214d3c0', '6251', 'Maintenance', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.543268', '2024-08-28 08:29:25.543268', 'f49f165633894f84afb06916215c9454', '1101', 'Uncollectibles', 'asset_ca_uncoll', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.330372', '2024-02-24 02:37:03.330372', 'f4cd73add9374635b1671a6f93cbe034', '1650', 'Furniture & Fixtures', 'asset_ppe', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', 'f6b62daf2e1f4415b4272331c7f787db', '6090', 'Freight', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.547264', '2024-08-28 08:29:25.547264', 'f8c2169bfc194e42b52207436344b3e4', '6252', 'Repairs', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.548289', '2024-08-28 08:29:25.548289', 'f90528dab94a4bab8513aecfef20371f', '7010', 'Misc. Revenue', 'in_other', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.548289', '2024-08-28 08:29:25.548289', 'f92fbbd8d768470e84a78e2f3fa2069f', '6300', 'Property Management', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', 'fa36977f640542dc98752ceaf0ea51d5', '6190', 'Office Expense', 'ex_op', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.544280', '2024-08-28 08:29:25.544280', 'fb42d4fc4f6b4aa68f06bc0895066779', '2010', 'Accounts Payable', 'lia_cl_acc_pay', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.546276', '2024-08-28 08:29:25.546276', 'fb75ec28f79c4d3da5ff68aa0bed0b1c', '6190', 'Office Expense', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-02-24 02:37:03.331881', '2024-02-24 02:37:03.331881', 'fb9c3403744042c1b136c3525bff221f', '1910', 'Securities Unrealized Gains/Losses', 'asset_adjustment', 'debit', 0, 1, '4f29fa3345484b68bde3e5ea541de55b', NULL),
('2024-08-28 08:29:25.544280', '2024-08-28 08:29:25.544280', 'fdd847212d6146b3a181fea2ff7c41b9', '1631', 'Less: Equipment Accumulated Depreciation', 'asset_ppe', 'credit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL),
('2024-08-28 08:29:25.547264', '2024-08-28 08:29:25.547264', 'ff01defaa08b4751aca57ecbaa0ba92a', '6293', 'Gas', 'ex_op', 'debit', 0, 1, '1c24aef2c85e4ab0a76583cbe141d4df', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `aix_aixitshandovermodel`
--

CREATE TABLE `aix_aixitshandovermodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `equipment_condition` varchar(100) NOT NULL,
  `proper_use` varchar(255) DEFAULT NULL,
  `description` longtext NOT NULL,
  `issueDate` date DEFAULT NULL,
  `returnDate` date DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `entity_id` char(32) NOT NULL,
  `staff_id` char(32) NOT NULL,
  `equipment_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_aixitsstatusreportmodel`
--

CREATE TABLE `aix_aixitsstatusreportmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `activity` varchar(100) NOT NULL,
  `activity_type` varchar(255) DEFAULT NULL,
  `startDate` date DEFAULT NULL,
  `dueDate` date DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `priority` varchar(255) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `description` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_aixitsstatusreportmodel`
--

INSERT INTO `aix_aixitsstatusreportmodel` (`created`, `updated`, `uuid`, `code`, `activity`, `activity_type`, `startDate`, `dueDate`, `status`, `priority`, `is_active`, `entity_id`, `description`) VALUES
('2025-04-10 12:27:27.700331', '2025-04-10 12:27:27.701402', '2364bff22d8946d0a6f706077c329dca', 'AIXBOCDRP3UCW', 'Fix RKASUA No access to Shared Folders', 'IT Support', '2025-04-10', '2025-04-10', 'COMPLETED', 'IMMEDIATE', 1, '94a77b664b5d4efab801ba8560d83fc8', 'Tilenga-SLS-SN account was not able to SharePoint thereby limiting access to online shared documents.'),
('2025-05-29 15:16:57.625287', '2025-05-29 15:16:57.626051', '3131f5b4b399404daf6de3785b9206a5', 'AIX0FJVWAV72J', 'IT Support - DSB Bulisa', 'IT Support', '2025-05-28', '2025-05-28', 'COMPLETED', 'IMMEDIATE', 1, '94a77b664b5d4efab801ba8560d83fc8', 'Worked on the following issues\r\n- HSE Martin\'s laptop had booting/ slow performance issues\r\n- STS - Joseph Kigundu\'s laptop emails were not syncing\r\n- Trouble shooting the issues of the faulty printer showing that the printer failed to work and needed replacement'),
('2025-04-01 09:31:10.070870', '2025-04-01 09:31:10.073964', '315bd1e3feee473183658d8f69b8286e', 'AIXUJ1X704UUM', 'Fix Sandra\'s Mails', 'IT Support', '2025-04-01', '2025-04-01', 'COMPLETED', 'IMMEDIATE', 1, '94a77b664b5d4efab801ba8560d83fc8', 'The email account skainembabazi@threewaysshipping.com had a syncing error and was not able to receive or send mails.'),
('2025-03-31 07:45:37.929816', '2025-03-31 07:45:37.936341', '353a000654d14666b704fee0f8c05496', 'AIXVCY7UJU53B', 'DC AD Backup', 'General', '2025-03-28', '2025-03-28', 'IN PROGRESS', 'QUARTERLY', 1, '94a77b664b5d4efab801ba8560d83fc8', 'Daily Backup of Active Directory Domain Controller configuration'),
('2025-01-23 08:59:39.241103', '2025-01-23 08:59:39.244102', '47ba875a6e5947fcabe6418e4586a066', 'AIX822D509CA5', 'Reconfigure TA Access Control machines Time', 'Troubleshooting', '2025-01-20', '2025-01-23', 'COMPLETED', 'IMMEDIATE', 1, '94a77b664b5d4efab801ba8560d83fc8', 'The TA Access Control device at the reception has continually refreshed the time to a back date. \r\nThe solution was to Reset/ Reconfigure to correct the error'),
('2025-05-29 15:11:58.802786', '2025-05-29 15:24:51.301971', '505d164cfe7940a590922e97b30c4329', 'AIXS2BABLVQZT', 'IT Support - KISEMENI-1 RIG SITE', 'IT Support', '2025-05-28', '2025-05-28', 'COMPLETED', 'IMMEDIATE', 1, '94a77b664b5d4efab801ba8560d83fc8', 'Worked on the following Issues\r\n- Dan Komaks Laptop mails were not syncing\r\n- Dan Komaks Laptop needed to be partiotioned\r\n- SLS - Roy Kasua\'s laptop email account was not activated rkasua@threewaysshipping.com\r\n- HR Admin - Brenda\'s laptop needed configuration on slow excel processing'),
('2025-01-10 05:44:13.445433', '2025-01-10 05:44:13.449302', '6d8d62fee27e4d2bb5dad5b8508b3aa4', 'AIX883PRO52W', 'Tilenga SLS 1503 - Activate Account', 'IT Support', '2025-01-08', '2025-01-09', 'COMPLETED', 'IMMEDIATE', 1, '94a77b664b5d4efab801ba8560d83fc8', 'Activate the Tilenga SLS 1503 Rig Move Account.\r\n- activate tilenga-sls-1503 user account\r\n- configure email account and activate app license'),
('2025-05-29 15:24:17.764834', '2025-05-29 15:24:17.765834', '7f6bbbed801e4016bb78a535bb017121', 'AIXVY901YG6WR', 'IT Support - HOIMA KONTIK OFFICE', 'IT Support', '2025-05-27', '2025-05-27', 'COMPLETED', 'IMMEDIATE', 1, '94a77b664b5d4efab801ba8560d83fc8', 'Worked on the following issues\r\n- Fleet Monitoring - Elizabeth\'s Laptop needed to be connected to the printer\r\n- Admin Clerk - Faith\'s laptop was constantly freezing/ the performance was poor and needed replacement\r\n- HR Hoima - Morris Komakech\'s laptop had slow outlook syncing/ OneDrive syncing issues'),
('2025-01-07 07:17:07.042946', '2025-01-07 07:33:56.681531', '9691048448c6466fb490f50402231aa0', 'AIXY8KH6323T7', 'Update TA Info for Joseph Bukenya', 'General', '2025-01-06', '2025-01-07', 'COMPLETED', 'IMMEDIATE', 1, '94a77b664b5d4efab801ba8560d83fc8', '- update names to show in clockin machine'),
('2025-03-28 12:13:14.269947', '2025-03-28 12:13:14.271513', '9847f1cbc3ff4843889438ad37190925', 'AIXP9CHLGB3H4', 'Configuring KFDA MiFi', 'IT Support', '2025-03-28', '2025-03-28', 'COMPLETED', 'IMMEDIATE', 1, '94a77b664b5d4efab801ba8560d83fc8', 'The KFDA Mifi was not giving internet connection. It had connectivity issues of which i solved'),
('2025-01-07 12:44:11.998619', '2025-01-07 12:44:12.000797', '9d9ec4bfcdb0471b800a7dbd98fe659e', 'AIXN783M53KL28', 'Run Data Recovery on Server One', 'Troubleshooting', '2024-12-02', '2025-01-07', 'IN PROGRESS', 'IMMEDIATE', 1, '94a77b664b5d4efab801ba8560d83fc8', '- run data recovery on Server One\r\n- create a share for the recovered data'),
('2025-04-03 08:52:06.559987', '2025-04-03 09:26:45.590306', 'abb67a623111494898187ce32f965e56', 'AIX6UZE25R65V9', 'Fixed TA Machine F18', 'General', '2025-04-03', '2025-04-03', 'COMPLETED', 'SHORT TERM', 1, '94a77b664b5d4efab801ba8560d83fc8', 'Fixed the Time & Attendance Machine at lower Operations Area Serial Number [COAW2203600729] - Issue was missing Check Out option'),
('2025-01-06 13:03:31.750928', '2025-01-07 07:37:25.473314', 'cbf368cc097d4a0f95ec37baf89d8385', 'AIXHT378DLW773', 'IT Support - Toms computer', 'General', '2025-01-01', '2025-01-17', 'COMPLETED', 'SHORT TERM', 1, '94a77b664b5d4efab801ba8560d83fc8', 'Fix OneDrive sychronizing problems'),
('2025-01-07 12:36:14.270892', '2025-01-07 12:38:48.733125', 'd5b0881f81364e7bb562fccc9a91b9bf', 'AIX839MDJKE9DH', 'DC Server Shutdown Issue', 'Troubleshooting', '2024-12-16', '2025-01-07', 'COMPLETED', 'QUARTERLY', 1, '94a77b664b5d4efab801ba8560d83fc8', '- Server One Domain Controller shuts down unexpectedly\r\n- Solved the issue with troubleshooting and extra configuration'),
('2025-04-10 12:23:29.482528', '2025-04-10 12:23:29.483607', 'e078e7df09cd4129b1dbc901b35ec9a2', 'AIXFJFB52G53O', 'Fix SLS-1502 Emails', 'IT Support', '2025-04-10', '2025-04-10', 'COMPLETED', 'IMMEDIATE', 1, '94a77b664b5d4efab801ba8560d83fc8', 'SLS-1502 email account was not able to send or receive emails. Teams and OneDrive were also not active'),
('2025-01-06 13:07:31.490270', '2025-01-07 07:35:26.407205', 'e080898ef604485c9c526c430c48381a', 'AIXJKSY7293KKL', 'IT Support - Donalds Computer', 'IT Support', '2025-01-03', '2025-01-03', 'IN PROGRESS', 'IMMEDIATE', 1, '94a77b664b5d4efab801ba8560d83fc8', '- Free up Outlook Mails storage space\r\n- Backup Archived emails'),
('2025-01-07 13:00:30.250403', '2025-01-07 13:00:30.251477', 'ff3003b290544745ba4801a5dc92d273', 'AIX4JANNSM4I6', 'Restore PBX Telephone System', 'Troubleshooting', '2024-12-02', '2025-01-20', 'IN PROGRESS', 'SHORT TERM', 1, '94a77b664b5d4efab801ba8560d83fc8', '- Restore Configuration Database');

-- --------------------------------------------------------

--
-- Table structure for table `aix_announcementmodel`
--

CREATE TABLE `aix_announcementmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `date` date NOT NULL,
  `value` varchar(100) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_assetmodel`
--

CREATE TABLE `aix_assetmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `vehicle_id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `group_name` varchar(255) DEFAULT NULL,
  `license_plate` varchar(255) DEFAULT NULL,
  `year` varchar(255) DEFAULT NULL,
  `model` varchar(255) DEFAULT NULL,
  `make` varchar(255) DEFAULT NULL,
  `vehicle_type_name` varchar(255) DEFAULT NULL,
  `woStatus` varchar(50) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `imageUrl` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL,
  `wialon_id` int(11) DEFAULT NULL,
  `id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_assetmodel`
--

INSERT INTO `aix_assetmodel` (`created`, `updated`, `uuid`, `vehicle_id`, `name`, `group_name`, `license_plate`, `year`, `model`, `make`, `vehicle_type_name`, `woStatus`, `status`, `imageUrl`, `entity_id`, `wialon_id`, `id`) VALUES
('2023-07-26 13:48:36.000000', '2023-10-15 09:52:22.000000', '5ae47e77932b11eea0b90a0027000102', 2516374, 'CR220-001-UBN377H', 'TEEPU', 'UBN377H', '2017', 'SAC2200', 'Sany', 'Crane', 'ALLOCATED', 'ALLOCATED', 'https://d8g9nhlfs6lwh.cloudfront.net/8hjsdgOVS8Olttn1fW2a?signature=6883981cae7ea07258f1d3d2334863cdf7f18833945706eab634d395092e374b&policy=eyJoYW5kbGUiOiI4aGpzZGdPVlM4T2x0dG4xZlcyYSIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:36.000000', '2023-09-29 08:52:53.000000', '5ae58598932b11eea0b90a0027000102', 2517120, 'CR50-001-UBN296B', 'CNOOC', 'UBN296B', '2022', 'STC500C', 'Sany', 'Crane', NULL, 'ALLOCATED', 'https://d8g9nhlfs6lwh.cloudfront.net/owyBhfTyiLVyDzSHNTQP?signature=8181a8b1649c5c4e4c19adc2f6d3cdcf3b26fdaa97f1e7107c5138f777d55d3f&policy=eyJoYW5kbGUiOiJvd3lCaGZUeWlMVnlEelNITlRRUCIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:36.000000', '2023-10-15 09:52:22.000000', '5ae58936932b11eea0b90a0027000102', 2296240, 'CR50-001T-UAS 482M', 'TEEPU', 'UAS 482M', '2012', 'QT50V532', 'Zoomlion', 'Crane', 'ALLOCATED', 'ALLOCATED', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:36.000000', '2023-09-28 13:58:30.000000', '5ae58c29932b11eea0b90a0027000102', 2517119, 'CR50-002-UBN295B', 'CNOOC', 'UBN295B', '2022', 'STC500C', 'Sany', 'Crane', NULL, 'ALLOCATED', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:36.000000', '2023-09-28 13:58:30.000000', '5ae58fc5932b11eea0b90a0027000102', 2296241, 'CR50-002T-UAR 534M', 'CNOOC', 'UAR 534M', NULL, NULL, 'Zoomlion', 'Crane', NULL, 'ALLOCATED', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:36.000000', '2023-10-13 09:49:35.000000', '5ae592a9932b11eea0b90a0027000102', 2296226, 'CR55-001-UBN180D', 'TEEPU', 'UBN180D', '2022', 'ZTC550R532', 'Zoomlion', 'Crane', NULL, 'ALLOCATED', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:36.000000', '2023-09-28 13:58:30.000000', '5ae59590932b11eea0b90a0027000102', 2510445, 'CR80-001-UBM783M', 'TEEPU', 'UBM783M', '2022', 'ZTC800R532', 'Zoomlion', 'Crane', NULL, 'ALLOCATED', 'https://d8g9nhlfs6lwh.cloudfront.net/DpOphJa7TQCgJSJefLEN?signature=9a1cadd0abe0b00f22f126178117ac193e265fdbf7fbbbecb624c03601bfb9e0&policy=eyJoYW5kbGUiOiJEcE9waEphN1RRQ2dKU0plZkxFTiIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:36.000000', '2023-09-29 08:52:53.000000', '5ae5986d932b11eea0b90a0027000102', 2510453, 'CR80-002-UBM784M', 'TEEPU', 'UBM784M', '2022', 'ZTC800R532', 'Zoomlion', 'Crane', NULL, 'ALLOCATED', 'https://d8g9nhlfs6lwh.cloudfront.net/UkvmIrrnQKmBwpP6rx1g?signature=8b9205acc6d5871770dd3f53848f49f1f2bb54a68e205e8401b9c68740eca77e&policy=eyJoYW5kbGUiOiJVa3ZtSXJyblFLbUJ3cFA2cngxZyIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:36.000000', '2023-10-01 06:27:50.000000', '5ae662a3932b11eea0b90a0027000102', 2642727, 'CR80-003-UBN062W', 'TEEPU', 'UBN062W', '2022', 'STC800C5.', 'Sany', 'Crane', NULL, 'ALLOCATED', 'https://d8g9nhlfs6lwh.cloudfront.net/jedHuKpKQ5674JGVqO8R?signature=a39d27a2012c03e8d3c19b2de99ad61622110840e9d7625bc716bbfc671181b7&policy=eyJoYW5kbGUiOiJqZWRIdUtwS1E1Njc0SkdWcU84UiIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:36.000000', '2023-10-01 06:27:50.000000', '5ae66696932b11eea0b90a0027000102', 2642728, 'CR80-004-UBN097W', 'TEEPU', 'UBN097W', '2022', 'STC800C5.', 'Sany', 'Crane', NULL, 'ALLOCATED', 'https://d8g9nhlfs6lwh.cloudfront.net/HOyROt4pQTevPMPcmx8I?signature=b557adf39a853e82fc843264fadd3dc63e291a31abd5f08ad2d4f7075955a2f3&policy=eyJoYW5kbGUiOiJIT3lST3Q0cFFUZXZQTVBjbXg4SSIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:36.000000', '2023-09-08 15:50:14.000000', '5ae669f7932b11eea0b90a0027000102', 2296244, 'FB001T-UAT 073M', 'CNOOC', 'UAT 073M', '2013', NULL, 'Bhachu', 'Flatbed trailer', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:36.000000', '2023-10-01 06:31:25.000000', '5ae66d4e932b11eea0b90a0027000102', 2296246, 'FB002T-UAT 544H', 'CNOOC', 'UAT 544H', NULL, NULL, 'Bhachu', 'Flatbed trailer', NULL, 'ALLOCATED', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:36.000000', '2023-09-08 15:50:14.000000', '5ae670d9932b11eea0b90a0027000102', 2296248, 'FB003T-UAS 915P', 'CNOOC', 'UAS 915P', '2012', NULL, 'Bhachu', 'Flatbed trailer', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:36.000000', '2023-10-01 06:34:19.000000', '5ae674aa932b11eea0b90a0027000102', 2296250, 'FB004T-UAT 220W', 'CNOOC', 'UAT 220W', '2013', NULL, 'Bhachu', 'Flatbed trailer', NULL, 'ALLOCATED', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:36.000000', '2023-09-08 15:50:14.000000', '5ae6783a932b11eea0b90a0027000102', 2296252, 'FB005T-UAL 949X', 'TEEPU', 'UAL 949X', '201', NULL, 'Bhachu', 'Flatbed trailer', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:36.000000', '2023-09-08 15:50:14.000000', '5ae67bae932b11eea0b90a0027000102', 2296254, 'FB006T-UAT 794P', 'TEEPU', 'UAT 794P', '2013', NULL, 'Bhachu', 'Flatbed trailer', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:36.000000', '2023-09-08 15:50:14.000000', '5ae67ec2932b11eea0b90a0027000102', 2296255, 'FB007T-UAL839X', 'TEEPU', 'UAL 839X', '201', NULL, 'Bhachu', 'Flatbed trailer', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:36.000000', '2023-09-08 15:50:14.000000', '5ae681db932b11eea0b90a0027000102', 2296256, 'FB008T-UAL 947X', 'TEEPU', 'UAL 947X', '201', NULL, 'Bhachu', 'Flatbed trailer', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:36.000000', '2023-10-13 09:49:35.000000', '5ae68483932b11eea0b90a0027000102', 2296257, 'FB009T-UAT 541H', 'TEEPU', 'UAT 541H', '2013', NULL, 'Bhachu', 'Flatbed trailer', NULL, 'ALLOCATED', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:36.000000', '2023-09-08 15:50:14.000000', '5ae6874c932b11eea0b90a0027000102', 2642733, 'FB30-001-UBN233V', 'TEEPU', 'UBN233V', '2023', 'ZJV9534TJZP', 'CIMC (Nelion)', 'Flatbed Trailer (Extendable)', NULL, 'Inactive', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:36.000000', '2023-09-08 15:50:15.000000', '5ae68a94932b11eea0b90a0027000102', 2642734, 'FB30-002-UBN035V', 'TEEPU', 'UBN035V', '2023', 'ZJV9534TJZP', 'CIMC (Nelion)', 'Flatbed Trailer (Extendable)', NULL, 'Inactive', 'https://d8g9nhlfs6lwh.cloudfront.net/rIXzEOm2QgeQ8budyPWG?signature=2b3b1d9fefe9926a6e7881fec977de8ad3e6e0e9f298e760c76aa3ac90cd4b56&policy=eyJoYW5kbGUiOiJySVh6RU9tMlFnZVE4YnVkeVBXRyIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:36.000000', '2023-09-08 15:50:15.000000', '5ae68ec6932b11eea0b90a0027000102', 2642735, 'FB30-003-UBN036V', 'TEEPU', 'UBN036V', '2023', 'ZJV9534TJZP', 'CIMC (Nelion)', 'Flatbed Trailer (Extendable)', NULL, 'Inactive', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:36.000000', '2023-09-08 15:50:15.000000', '5ae692ac932b11eea0b90a0027000102', 2642736, 'FB30-004-UBN056V', 'TEEPU', 'UBN056V', '2023', 'ZJV9534TJZP', 'CIMC (Nelion)', 'Flatbed Trailer (Extendable)', NULL, 'Inactive', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae696ab932b11eea0b90a0027000102', 2642737, 'FB30-005-UBN058V', 'TEEPU', 'UBN058V', '2023', 'ZJV9534TJZP', 'CIMC (Nelion)', 'Flatbed Trailer (Extendable)', NULL, 'Inactive', 'https://d8g9nhlfs6lwh.cloudfront.net/3Ia9dCysQGK3KD7Jooec?signature=0603a844702c07cfb8c69e16a54f99a335314622ca2f18df9f827700ea6952c7&policy=eyJoYW5kbGUiOiIzSWE5ZEN5c1FHSzNLRDdKb29lYyIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae69aa9932b11eea0b90a0027000102', 2642738, 'FB30-006-UBN059V', 'SLB', 'UBN059V', '2023', 'ZJV9534TJZP', 'CIMC (Nelion)', 'Flatbed Trailer (Extendable)', NULL, 'Inactive', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-10-01 07:10:40.000000', '5ae69e93932b11eea0b90a0027000102', 2642739, 'FB30-007-UBN652Z', 'SLB', 'UBN652Z', '2023', 'ZJV9534TJZP', 'CIMC (Nelion)', 'Flatbed Trailer (Extendable)', NULL, 'ALLOCATED', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae6a2ad932b11eea0b90a0027000102', 2642740, 'FB30-008-UBN653Z', 'SLB', 'UBN653Z', '2023', 'ZJV9534TJZP', 'CIMC (Nelion)', 'Flatbed Trailer (Extendable)', NULL, 'Inactive', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae6a739932b11eea0b90a0027000102', 2642741, 'FB30-009-UBN654Z', 'CNOOC', 'UBN654Z', '2023', 'ZJV9534TJZP', 'CIMC (Nelion)', 'Flatbed Trailer (Extendable)', NULL, 'Inactive', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae6aacc932b11eea0b90a0027000102', 2642742, 'FB30-010-UBN655Z', 'CNOOC', 'UBN655Z', '2023', 'ZJV9534TJZP', 'CIMC (Nelion)', 'Flatbed Trailer (Extendable)', NULL, 'Inactive', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae6ae0d932b11eea0b90a0027000102', 2642743, 'FB30-011-UBN656Z', 'CNOOC', 'UBN656Z', '2023', 'ZJV9534TJZP', 'CIMC (Nelion)', 'Flatbed Trailer (Extendable)', NULL, 'Inactive', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae6b0bb932b11eea0b90a0027000102', 2296227, 'FL03-001-UBM291X', 'CNOOC', 'UBM291X', '2022', 'DP30NT', 'CAT', 'Forklift', NULL, 'Mobilized', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae6b38c932b11eea0b90a0027000102', 2296228, 'FL03-002-UBM326Z', 'CNOOC', 'UBM326Z', '202', 'DP30NT', 'CAT', 'Forklift', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae6b676932b11eea0b90a0027000102', 2296225, 'FL05-001-UBM027G', 'SLB', 'UBM027G', '2022', 'FD50', 'Zoomlion', 'Forklift', NULL, 'Mobilized', 'https://d8g9nhlfs6lwh.cloudfront.net/SjVWZ1KcQwi0v6MigtUN?signature=d1afae1a729d7ce318e94e615f0a1048e64ecc2b836643ee0a48f829b45d7238&policy=eyJoYW5kbGUiOiJTalZXWjFLY1F3aTB2Nk1pZ3RVTiIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae6ba10932b11eea0b90a0027000102', 2296229, 'FL05-002-UBM822X', 'TEEPU', 'UBM822X', '2022', 'DP50NT', 'CAT', 'Forklift', NULL, 'Inactive', 'https://d8g9nhlfs6lwh.cloudfront.net/Fd7grTOCQD2UQYp8ADg7?signature=2b5ef226ba453b4413f334633a07141f89a731ed23249415ea8d15eb7c10d6b4&policy=eyJoYW5kbGUiOiJGZDdnclRPQ1FEMlVRWXA4QURnNyIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae6be06932b11eea0b90a0027000102', 2642729, 'HT08-001-UBN478V', 'TEEPU', 'UBN478V', '2022', '2638 CRANE', 'Beiben /XCMG', 'Hiab Truck', NULL, 'Inactive', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae6c24e932b11eea0b90a0027000102', 2538798, 'LB80-001-UBN041P', 'TEEPU', 'UBN041P', '2023', 'Low Loader Semi Trailer', 'Transtrailers', 'Lowbed - 60 ton (8 axle)', NULL, 'Active', 'https://d8g9nhlfs6lwh.cloudfront.net/5B6EoCIuSfmhRbGmszTm?signature=c909099847f591adcb335cfc85bdb0b25b67ee20b46875bf32adee65514dfbfe&policy=eyJoYW5kbGUiOiI1QjZFb0NJdVNmbWhSYkdtc3pUbSIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae6c717932b11eea0b90a0027000102', 2538805, 'LB80-002-UBN147P', 'TEEPU', 'UBN147P', '2023', 'Low Loader Semi Trailer', 'Transtrailers', 'Lowbed - 60 ton (8 axle)', NULL, 'Active', 'https://d8g9nhlfs6lwh.cloudfront.net/7XNaCI83TSeYi52tDDGl?signature=12214475efec1c6db7cea6f6db8d78328544ebda1e2ee98e357260eff43fa8ca&policy=eyJoYW5kbGUiOiI3WE5hQ0k4M1RTZVlpNTJ0RERHbCIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae6d459932b11eea0b90a0027000102', 2538806, 'LB80-003-UBN622N', 'TEEPU', 'UBN622N', '2023', 'Low Loader Semi Trailer', 'Transtrailers', 'Lowbed - 60 ton (8 axle)', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae6da7b932b11eea0b90a0027000102', 2642639, 'LB80-004-UBN439T', 'TEEPU', 'UBN439T', '2023', 'Low Loader Semi Trailer', 'Transtrailers', 'Lowbed - 60 ton (8 axle)', NULL, 'Active', 'https://d8g9nhlfs6lwh.cloudfront.net/XspiQv0RB6QmpP9zTHrq?signature=fc34a5f6cf783f9c9b983a16b5cd1e327d1397d6611ea441f20244c479eff69a&policy=eyJoYW5kbGUiOiJYc3BpUXYwUkI2UW1wUDl6VEhycSIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae6ded2932b11eea0b90a0027000102', 2510460, 'PC14-001-UBM776Z', 'CNOOC', 'UBM776Z', '2022', 'KDH222R-LEMDY', 'Toyota HiACe', 'Bus', NULL, 'Mobilized', 'https://d8g9nhlfs6lwh.cloudfront.net/blkzvDWtSHuDK5DsZqc4?signature=41ebd26fd5eb928cc77d556f69769f615ab5488320b8f68c3011e60eedb917b7&policy=eyJoYW5kbGUiOiJibGt6dkRXdFNIdURLNURzWnFjNCIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae6e75a932b11eea0b90a0027000102', 2510468, 'PC30-001-UBN243G', 'TEEPU', 'UBN243G', '2022', 'HZB70R-ZGMNS H2', 'Toyota Coaster H2', 'Bus', NULL, 'Mobilized', 'https://d8g9nhlfs6lwh.cloudfront.net/lEakJeWET86qFZx6VNPJ?signature=5de89e6eca1a60e689ef0bef37cb68f8f723b489a4d69fde956f82def5332197&policy=eyJoYW5kbGUiOiJsRWFrSmVXRVQ4NnFGWng2Vk5QSiIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae6ebc2932b11eea0b90a0027000102', 2296234, 'PM001-UBM983X', 'TEEPU', 'UBM983X', '2022', '2636S', 'Beiben', 'Prime Mover', NULL, 'Mobilized', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae6ef23932b11eea0b90a0027000102', 2296243, 'PM001T-UAP 708Z', 'CNOOC', 'UAP 708Z', '201', NULL, 'Actros', 'Prime Mover', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae6f323932b11eea0b90a0027000102', 2296235, 'PM002-UBM984X', 'TEEPU', 'UBM984X', '2022', '2636S', 'Beiben', 'Prime Mover', NULL, 'Active', 'https://d8g9nhlfs6lwh.cloudfront.net/cWeM4G8Q7CiwhUa44pp1?signature=cd3d28f032381106ea6254850424b22476d591d7b6cd125aa250d941cd0a8f54&policy=eyJoYW5kbGUiOiJjV2VNNEc4UTdDaXdoVWE0NHBwMSIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae6f666932b11eea0b90a0027000102', 2296245, 'PM002T-UAU 662H', 'CNOOC', 'UAU 662H', '2013', NULL, 'Actros', 'Prime Mover', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-10-01 07:10:40.000000', '5ae6fc22932b11eea0b90a0027000102', 2296236, 'PM003-UBM985X', 'TEEPU', 'UBM985X', '2022', '2636S', 'Beiben', 'Prime Mover', NULL, 'ALLOCATED', 'https://d8g9nhlfs6lwh.cloudfront.net/NO4Z7fqFRoe471WzPI8w?signature=be015ef348d1a7e98fd69d33ee9562b6d58b6c1650f5329365d5ee3c8eaa7ca9&policy=eyJoYW5kbGUiOiJOTzRaN2ZxRlJvZTQ3MVd6UEk4dyIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae6ff39932b11eea0b90a0027000102', 2296247, 'PM003T-UAU 416D', 'CNOOC', 'UAU 416D', '2013', NULL, 'Beiben', 'Prime Mover', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae70161932b11eea0b90a0027000102', 2296237, 'PM004-UBM986X', 'TEEPU', 'UBM986X', '2022', '2636S', 'Beiben', 'Prime Mover', NULL, 'Mobilized', 'https://d8g9nhlfs6lwh.cloudfront.net/t71OwWv3QhCfOdIdw4kg?signature=ae73cc08d50f782d294f456d69903ec0a72b12b692cce3671b77cde30b57560e&policy=eyJoYW5kbGUiOiJ0NzFPd1d2M1FoQ2ZPZElkdzRrZyIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae703e5932b11eea0b90a0027000102', 2296249, 'PM004T-UAS 163S', 'CNOOC', 'UAS 163S', '2012', NULL, 'Beiben', 'Prime Mover', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae706a2932b11eea0b90a0027000102', 2296238, 'PM005-UBM987X', 'CNOOC', 'UBM987X', '2022', '2636S', 'Beiben', 'Prime Mover', NULL, 'Mobilized', 'https://d8g9nhlfs6lwh.cloudfront.net/YhWEoC6QZOj6D53OzMQ7?signature=824ce8a4ca54efba1f29749d65783fbc73e4234b750ecfc86b893b8dd95eb648&policy=eyJoYW5kbGUiOiJZaFdFb0M2UVpPajZENTNPek1RNyIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae70908932b11eea0b90a0027000102', 2296251, 'PM005T-UAP 696Z', 'TEEPU', 'UAP 696Z', '201', NULL, 'Actros', 'Prime Mover', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae70bf2932b11eea0b90a0027000102', 2296239, 'PM006-UBM988X', 'TEEPU', 'UBM988X', '2022', '2636S', 'Beiben', 'Prime Mover', NULL, 'Mobilized', 'https://d8g9nhlfs6lwh.cloudfront.net/SKvOUYD9RQGSrfVd82xa?signature=b2317461c2c7264c96a21339d9ded92c59a6527a4df3558ca6474bb28eedde2d&policy=eyJoYW5kbGUiOiJTS3ZPVVlEOVJRR1NyZlZkODJ4YSIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae70ea3932b11eea0b90a0027000102', 2296253, 'PM006T-UAT 959E', 'TEEPU', 'UAT 959E', '2005', NULL, 'Actros', 'Prime Mover', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae71154932b11eea0b90a0027000102', 2518079, 'PM007-UBN747J', 'TEEPU', 'UBN747J', '2022', '2638S', 'Beiben', 'Prime Mover', NULL, 'Mobilized', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae713e9932b11eea0b90a0027000102', 2538437, 'PM008-UBN060Q', 'TEEPU', 'UBN060Q', '2023', '2638S', 'Beiben', 'Prime Mover', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae71669932b11eea0b90a0027000102', 2538438, 'PM009-UBN061Q', 'TEEPU', 'UBN061Q', '2023', '2638S', 'Beiben', 'Prime Mover', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae718fb932b11eea0b90a0027000102', 2538439, 'PM010-UBN062Q', 'TEEPU', 'UBN062Q', '2023', '2638S', 'Beiben', 'Prime Mover', NULL, 'Active', 'https://d8g9nhlfs6lwh.cloudfront.net/YA5gIwXSpeFONkG56YAv?signature=78f7eb000da6550393f0f55a9e274dceb3f304182fc52fa244531a1f860cc3c7&policy=eyJoYW5kbGUiOiJZQTVnSXdYU3BlRk9Oa0c1NllBdiIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae74d1c932b11eea0b90a0027000102', 2538440, 'PM011-UBN065Q', 'TEEPU', 'UBN065Q', '2023', '2638S', 'Beiben', 'Prime Mover', NULL, 'Active', 'https://d8g9nhlfs6lwh.cloudfront.net/2CzDATQFSnISh2MvEBgI?signature=c2d42de686538ef062e39ee6214222a99387c8e4045edd5faf958da12f16668a&policy=eyJoYW5kbGUiOiIyQ3pEQVRRRlNuSVNoMk12RUJnSSIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae75216932b11eea0b90a0027000102', 2538441, 'PM012-UBN066Q', 'TEEPU', 'UBN066Q', '2023', '2638S', 'Beiben', 'Prime Mover', NULL, 'Active', 'https://d8g9nhlfs6lwh.cloudfront.net/lEI2u5StKXQnRMs8KItA?signature=7af5d509c6247c51d4e8be7d7bcc932eb77033f36a3f89287f17b11033877f38&policy=eyJoYW5kbGUiOiJsRUkydTVTdEtYUW5STXM4S0l0QSIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae7553a932b11eea0b90a0027000102', 2538771, 'PM013-UBN004R', 'TEEPU', 'UBN004R', '2023', '2638S', 'Beiben', 'Prime Mover', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae75863932b11eea0b90a0027000102', 2538772, 'PM014-UBN007R', 'TEEPU', 'UBN007R', '2023', '2638S', 'Beiben', 'Prime Mover', NULL, 'Active', 'https://d8g9nhlfs6lwh.cloudfront.net/pIuugnSS5yHKm1sa11Wm?signature=dbe01ec5c96320b800c5c65816e1b044257a0153d6a8c0177474afa1bf733f49&policy=eyJoYW5kbGUiOiJwSXV1Z25TUzV5SEttMXNhMTFXbSIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae75b5b932b11eea0b90a0027000102', 2538775, 'PM015-UBN008R', 'TEEPU', 'UBN008R', '2023', '2638S', 'Beiben', 'Prime Mover', NULL, 'Active', 'https://d8g9nhlfs6lwh.cloudfront.net/fc8yZ9dlR0yBt2aZyejZ?signature=c2abad88f0583ead1b9475ac477d988150e64f98322e177b6f609638dbf87df0&policy=eyJoYW5kbGUiOiJmYzh5WjlkbFIweUJ0MmFaeWVqWiIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae75e44932b11eea0b90a0027000102', 2538776, 'PM016-UBN009R', 'TEEPU', 'UBN009R', '2023', '2638S', 'Beiben', 'Prime Mover', NULL, 'Active', 'https://d8g9nhlfs6lwh.cloudfront.net/QTBx8r5RS1KVSpiqagvr?signature=1d153be3a1ba80463d951341f87f2ebf95d756154a4f47477738cc953a1bd44f&policy=eyJoYW5kbGUiOiJRVEJ4OHI1UlMxS1ZTcGlxYWd2ciIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae7610a932b11eea0b90a0027000102', 2296230, 'PU001-UBM227X', 'TEEPU', 'UBM227X', '202', 'JX-1033TSER', 'JMC', 'Pick-up', NULL, 'Mobilized', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae76414932b11eea0b90a0027000102', 2296231, 'PU002-UBM235X', 'TEEPU', 'UBM235X', '202', 'JX-1033TSER', 'JMC', 'Pick-up', NULL, 'Mobilized', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae7675f932b11eea0b90a0027000102', 2296232, 'PU003-UBM236X', 'TEEPU', 'UBM236X', '202', 'JX-1033TSER', 'JMC', 'Pick-up', NULL, 'Mobilized', 'https://d8g9nhlfs6lwh.cloudfront.net/CnQ39j2QQZu0ee0oX10N?signature=16129756149d52b055d0a66236ff93153d5661d432f84885df8fbeddef73e52c&policy=eyJoYW5kbGUiOiJDblEzOWoyUVFadTBlZTBvWDEwTiIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae76a71932b11eea0b90a0027000102', 2296233, 'PU004-UBM237X', 'TEEPU', 'UBM237X', '202', 'JX-1033TSER', 'JMC', 'Pick-up', NULL, 'Mobilized', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae76dc9932b11eea0b90a0027000102', 2516335, 'RS45-001-UBN600J', 'TEEPU', 'UBN600J', '202', 'DRU450-62S5', 'Kalmar', 'Reach Stacker', NULL, 'Inactive', 'https://d8g9nhlfs6lwh.cloudfront.net/pkUH4FvjQuWSQH7VRSgg?signature=b488edde24dc7fe6206fca2265a7378e10ec4b1d76a81b3e00d22fce08a3f116&policy=eyJoYW5kbGUiOiJwa1VINEZ2alF1V1NRSDdWUlNnZyIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae77151932b11eea0b90a0027000102', 2627214, 'TH04-001-UBN599J', 'CNOOC', 'UBN599J', '2019', 'MT-X1840', 'Manitou', 'Telehandler', NULL, 'Active', 'https://d8g9nhlfs6lwh.cloudfront.net/SGNJELJeQleYGGq52ds6?signature=70170ee512682c4f60219d4b6b1eee01eebce7d459bd2d8bce3ec6499caa0806&policy=eyJoYW5kbGUiOiJTR05KRUxKZVFsZVlHR3E1MmRzNiIsImV4cGlyeSI6NDUzNDk0OTM0MywiY2FsbCI6WyJyZWFkIl19', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae77444932b11eea0b90a0027000102', 2642730, 'TH04-002-UBN646W', 'CNOOC', 'UBN646W', '2023', 'HNT40-4', 'SOCMA', 'Telehandler', NULL, 'Inactive', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae77760932b11eea0b90a0027000102', 2642731, 'TH04-003-UBN649W', 'SLB', 'UBN649W', '2023', 'HNT40-4', 'SOCMA', 'Telehandler', NULL, 'Inactive', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae77a7d932b11eea0b90a0027000102', 2642732, 'TH16-001-UBN980W', 'TEEPU', 'UBN980W', '2023', 'HNTC160', 'SOCMA', 'Telehandler', NULL, 'Inactive', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae77da9932b11eea0b90a0027000102', 2296266, 'UAS 281Q', 'Kampala', 'UAS 281Q', '2012', '2636S', 'Beiben', 'Prime Mover', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae780d8932b11eea0b90a0027000102', 2689806, 'UAS907L', 'Kampala', 'UAS907L', '2012', 'ELF TRUCK', 'Isuzu', 'Truck', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae783ff932b11eea0b90a0027000102', 2689814, 'UAS916L', 'Kampala', 'UAS916L', '2012', 'ELF TRUCK', 'Isuzu', 'Truck', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae78704932b11eea0b90a0027000102', 2689804, 'UAT264W', 'Kampala', 'UAT264W', '2013', 'ELF TRUCK', 'Isuzu', 'Truck', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae78a1e932b11eea0b90a0027000102', 2296267, 'UAT 647L', 'Kampala', 'UAT 647L', '2013', NULL, 'Bhachu', 'Flatbed trailer', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae78d27932b11eea0b90a0027000102', 2689803, 'UAT681A', 'Kampala', 'UAT681A', '2012', 'ELF TRUCK', 'Isuzu', 'Truck', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae79042932b11eea0b90a0027000102', 2689805, 'UAV909A', 'Kampala', 'UAV909A', '2013', NULL, 'Isuzu', 'Truck', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae793bb932b11eea0b90a0027000102', 2689815, 'UAV948A', 'Kampala', 'UAV948A', '2012', 'ELF TRUCK', 'Isuzu', 'Truck', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae79718932b11eea0b90a0027000102', 2611557, 'UBM771M', 'Technical', 'UBM771M', NULL, 'NP300', 'Nissan', 'Pick-up', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae79a1d932b11eea0b90a0027000102', 2611558, 'UBM772M', 'Technical', 'UBM772M', NULL, 'NP300', 'Nissan', 'Pick-up', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae79d3c932b11eea0b90a0027000102', 2627310, 'UBM789Q', 'Kampala', 'UBM789Q', '2022', 'Navara', 'Nissan', 'Pick-up', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae7a048932b11eea0b90a0027000102', 2614385, 'UBM791Q', 'CNOOC', 'UBM791Q', NULL, 'NP300', 'Nissan', 'Pick-up', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:15.000000', '5ae7a35d932b11eea0b90a0027000102', 2614392, 'UBM792Q', 'CNOOC', 'UBM792Q', NULL, 'NP300', 'Nissan', 'Pick-up', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-26 13:48:37.000000', '2023-09-08 15:50:14.000000', '5ae7a675932b11eea0b90a0027000102', 2689994, 'BB05-001-UBN270J', 'Kampala', 'UBN270J', '2019', 'N SERIES 4.20M', 'Isuzu', 'Truck', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-28 12:59:04.000000', '2023-09-08 15:50:15.000000', '5ae7ced2932b11eea0b90a0027000102', 2701461, 'FT15c-001-UBN379H', 'TEEPU', 'UBN379H', '2017', 'G410', 'Scania', 'Truck', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-07-28 12:59:04.000000', '2023-09-08 15:50:15.000000', '5ae7d1a1932b11eea0b90a0027000102', 2701460, 'FT20c-001-UBN043J', 'TEEPU', 'UBN043J', '2017', 'G410', 'Scania', 'Truck', NULL, 'Inactive', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-08-28 06:40:01.000000', '2023-09-08 15:50:14.000000', '5ae7d3aa932b11eea0b90a0027000102', 2754333, 'CR110-001-UBN679Y', 'CNOOC', 'UBN679Y', '2022', 'STC1100T6.', 'Sany', 'Crane', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-08-28 06:40:01.000000', '2023-09-08 15:50:15.000000', '5ae7d5ab932b11eea0b90a0027000102', 2754412, 'HT08-002-UBN038Z', 'TEEPU', 'UBN038Z', '2023', '2638 CRANE', 'Beiben /XCMG', 'Hiab Truck', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-08-28 06:40:12.000000', '2023-09-08 15:50:15.000000', '5ae7d7ad932b11eea0b90a0027000102', 2709016, 'UAQ117N', 'All Sites', 'UAQ117N', NULL, 'QY50V', 'Zoomlion', 'Crane', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-08-28 06:40:12.000000', '2023-09-08 15:50:15.000000', '5ae7d9ab932b11eea0b90a0027000102', 2709017, 'UAQ239N', 'All Sites', 'UAQ239N', NULL, 'QY70V', 'Zoomlion', 'Crane', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-09-08 15:50:15.000000', '2023-09-08 15:50:15.000000', '5ae7dbc6932b11eea0b90a0027000102', 2772279, 'FL15-001-UBP080D', 'TEEPU', 'UBP080D', '2023', 'CPCD150-CU', 'HELI', 'Forklift', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-09-08 15:50:15.000000', '2023-09-08 15:50:15.000000', '5ae7ddc1932b11eea0b90a0027000102', 2772285, 'FL15-002-UBP081D', 'TEEPU', 'UBP081D	', '2023', 'CPCD150-CU', 'HELI', 'Forklift', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-09-08 15:50:15.000000', '2023-09-08 15:50:15.000000', '5ae7dfad932b11eea0b90a0027000102', 2772293, 'FL15-003-UBP045E', 'TEEPU', 'UBP045E', '2023', 'CPCD150-CU', 'HELI', 'Forklift', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-09-08 15:50:15.000000', '2023-09-08 15:50:15.000000', '5ae7e192932b11eea0b90a0027000102', 2777556, 'FL15-004-UBP949E', 'TEEPU', 'UBP949E', '2023', NULL, 'Heli', 'Forklift', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-09-08 15:50:15.000000', '2023-09-08 15:50:15.000000', '5ae7e3e8932b11eea0b90a0027000102', 2771450, 'LB55-001-UBN378H', 'All Sites', 'UBN378H', '2016', NULL, 'HENRED FRUEHAUF', 'Lowbed - 55T (3 Axle)', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-09-08 15:50:15.000000', '2023-09-08 15:50:15.000000', '5ae7e5c8932b11eea0b90a0027000102', 2771417, 'VT20C-001-UBN989W', 'TEEPU', 'UBN989W', '2023', 'ZZ1257V5247B1R', 'SINOTRUK(HOWO)', 'Vacuum Truck', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2023-09-08 15:50:15.000000', '2023-09-08 15:50:15.000000', '5ae7e7be932b11eea0b90a0027000102', 2766636, 'WT20C-001-UBN201X', 'TEEPU', 'UBN201X ', '2023', 'ZZ1257V4647B1R', 'SINOTRUK(HOWO)', 'Water Truck', NULL, 'Active', NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `aix_ast`
--

CREATE TABLE `aix_ast` (
  `nm` varchar(100) DEFAULT NULL,
  `cls` int(11) NOT NULL,
  `id` int(11) NOT NULL,
  `mu` int(11) NOT NULL,
  `uacl` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_attachedemailmodel`
--

CREATE TABLE `aix_attachedemailmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `data` varchar(100) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_bankaccountmodel`
--

CREATE TABLE `aix_bankaccountmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `name` varchar(150) DEFAULT NULL,
  `account_number` varchar(30) DEFAULT NULL,
  `routing_number` varchar(30) DEFAULT NULL,
  `aba_number` varchar(30) DEFAULT NULL,
  `account_type` varchar(10) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `hidden` tinyint(1) NOT NULL,
  `cash_account_id` char(32) DEFAULT NULL,
  `ledger_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_benefitcalculationmodel`
--

CREATE TABLE `aix_benefitcalculationmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_benefitmodel`
--

CREATE TABLE `aix_benefitmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT NULL,
  `value` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `hidden` tinyint(1) NOT NULL,
  `additional_info` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`additional_info`)),
  `benefit_type_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `salary_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_benefittypemodel`
--

CREATE TABLE `aix_benefittypemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `polarity` int(11) NOT NULL,
  `value` longtext DEFAULT NULL,
  `algorithm` longtext DEFAULT NULL,
  `description` longtext NOT NULL,
  `is_taxed` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `benefit_calculation_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_billmodel`
--

CREATE TABLE `aix_billmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `terms` varchar(10) NOT NULL,
  `amount_due` decimal(20,2) NOT NULL,
  `amount_paid` decimal(20,2) NOT NULL,
  `amount_receivable` decimal(20,2) NOT NULL,
  `amount_unearned` decimal(20,2) NOT NULL,
  `amount_earned` decimal(20,2) NOT NULL,
  `date` date NOT NULL,
  `due_date` date NOT NULL,
  `accrue` tinyint(1) NOT NULL,
  `progress` decimal(3,2) NOT NULL,
  `markdown_notes` longtext DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `bill_number` varchar(20) NOT NULL,
  `bill_status` varchar(10) NOT NULL,
  `xref` varchar(50) DEFAULT NULL,
  `additional_info` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`additional_info`)),
  `draft_date` date DEFAULT NULL,
  `in_review_date` date DEFAULT NULL,
  `approved_date` date DEFAULT NULL,
  `paid_date` date DEFAULT NULL,
  `void_date` date DEFAULT NULL,
  `canceled_date` date DEFAULT NULL,
  `cash_account_id` char(32) DEFAULT NULL,
  `ce_model_id` char(32) DEFAULT NULL,
  `ledger_id` char(32) NOT NULL,
  `prepaid_account_id` char(32) DEFAULT NULL,
  `unearned_account_id` char(32) DEFAULT NULL,
  `vendor_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_billmodel`
--

INSERT INTO `aix_billmodel` (`created`, `updated`, `terms`, `amount_due`, `amount_paid`, `amount_receivable`, `amount_unearned`, `amount_earned`, `date`, `due_date`, `accrue`, `progress`, `markdown_notes`, `uuid`, `bill_number`, `bill_status`, `xref`, `additional_info`, `draft_date`, `in_review_date`, `approved_date`, `paid_date`, `void_date`, `canceled_date`, `cash_account_id`, `ce_model_id`, `ledger_id`, `prepaid_account_id`, `unearned_account_id`, `vendor_id`) VALUES
('2024-02-25 01:07:42.832744', '2024-02-25 01:55:12.958822', 'on_receipt', '451080.00', '202000.00', '0.00', '0.00', '202000.00', '2024-02-25', '2024-02-25', 0, '0.00', 'The fuel was bought from 2 fuel stations', '33a378ad8eeb451aab75a5c95c581b7f', 'B-8OSP8WGZ4P', 'approved', NULL, '{}', NULL, '2024-02-25', '2024-02-25', NULL, NULL, NULL, '6fe4fe62eba44a3bbf5ca23fdd2c5ae5', NULL, '838120708f9c4be88af1be7cddc17bc4', '0ddc3a9298bd4cffaa7676fc360341bb', '2a42258d8fc04a8982890d6483d7d055', 'ba5e42c965c1412fa799ae45240d7a87'),
('2024-02-27 07:59:33.889036', '2024-02-27 08:02:33.920525', 'on_receipt', '790000.00', '0.00', '0.00', '0.00', '0.00', '2024-02-27', '2024-02-27', 0, '0.00', NULL, 'd8f99b49272e401f94ceba217bd1562f', 'B-X88Q8YMPJS', 'draft', NULL, '{}', NULL, NULL, NULL, NULL, NULL, NULL, '6fe4fe62eba44a3bbf5ca23fdd2c5ae5', NULL, '1908708c1f40487fb93eb7c98370dc0a', '0ddc3a9298bd4cffaa7676fc360341bb', '2a42258d8fc04a8982890d6483d7d055', 'ba5e42c965c1412fa799ae45240d7a87');

-- --------------------------------------------------------

--
-- Table structure for table `aix_businessindustrymodel`
--

CREATE TABLE `aix_businessindustrymodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_businessindustrymodel`
--

INSERT INTO `aix_businessindustrymodel` (`created`, `updated`, `uuid`, `code`, `name`, `description`, `is_active`, `entity_id`) VALUES
('2024-02-24 16:37:13.822596', '2024-02-24 16:37:13.827132', 'f585f3c11b02422d9e2bc1aee93d085a', 'LGS', 'Logistics', 'Logistics', 1, '1980d2af5ea14ad5b1e7712771f60517');

-- --------------------------------------------------------

--
-- Table structure for table `aix_chartofaccountmodel`
--

CREATE TABLE `aix_chartofaccountmodel` (
  `slug` varchar(50) NOT NULL,
  `name` varchar(150) DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `locked` tinyint(1) NOT NULL,
  `description` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_chartofaccountmodel`
--

INSERT INTO `aix_chartofaccountmodel` (`slug`, `name`, `created`, `updated`, `uuid`, `locked`, `description`, `entity_id`) VALUES
('3ways-prh482nd-coa', 'Threeways CoA', '2024-08-28 08:29:25.527167', '2024-08-28 08:29:25.527167', '1c24aef2c85e4ab0a76583cbe141d4df', 0, NULL, '94a77b664b5d4efab801ba8560d83fc8'),
('total-uganda-z4bevxpj-coa', 'Total Uganda CoA', '2024-02-24 02:37:03.321484', '2024-02-24 02:37:03.321484', '4f29fa3345484b68bde3e5ea541de55b', 0, NULL, '1980d2af5ea14ad5b1e7712771f60517');

-- --------------------------------------------------------

--
-- Table structure for table `aix_currencymodel`
--

CREATE TABLE `aix_currencymodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_currencymodel`
--

INSERT INTO `aix_currencymodel` (`created`, `updated`, `uuid`, `code`, `name`, `is_active`, `entity_id`) VALUES
('2024-09-02 05:17:42.985579', '2024-09-02 05:17:42.987599', '15a1e0c71f0646fcb537b7598c4c41e4', 'USD', 'US Dollar', 1, '94a77b664b5d4efab801ba8560d83fc8'),
('2024-09-02 05:17:27.221602', '2024-09-02 05:17:27.230544', '8de04ee2c831426fb2de71f8ba79846d', 'UGX', 'Uganda Shillings', 1, '94a77b664b5d4efab801ba8560d83fc8'),
('2024-03-08 13:25:59.608004', '2024-03-08 13:25:59.610005', '92c576f8dc6e4d72a4ecb02665fef1e7', 'USD', 'US Dollar', 1, '1980d2af5ea14ad5b1e7712771f60517'),
('2024-02-26 06:04:07.941602', '2024-02-26 06:04:07.946101', 'd0d964fd363944fb84796f0869444082', 'UGX', 'Uganda Shillings', 1, '1980d2af5ea14ad5b1e7712771f60517');

-- --------------------------------------------------------

--
-- Table structure for table `aix_currencyratemodel`
--

CREATE TABLE `aix_currencyratemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `buying` int(11) NOT NULL,
  `selling` int(11) NOT NULL,
  `date` date NOT NULL,
  `currency_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_currencyratemodel`
--

INSERT INTO `aix_currencyratemodel` (`created`, `updated`, `uuid`, `buying`, `selling`, `date`, `currency_id`, `entity_id`) VALUES
('2024-09-02 05:51:56.899725', '2024-09-02 05:51:56.901993', '1b7a2a8cfd4544df9b9f6a30a36f981b', 3717, 3722, '2024-09-02', '15a1e0c71f0646fcb537b7598c4c41e4', '94a77b664b5d4efab801ba8560d83fc8');

-- --------------------------------------------------------

--
-- Table structure for table `aix_customerlocationmodel`
--

CREATE TABLE `aix_customerlocationmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `customer_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `is_active` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_customerlocationmodel`
--

INSERT INTO `aix_customerlocationmodel` (`created`, `updated`, `uuid`, `code`, `name`, `description`, `customer_id`, `entity_id`, `is_active`) VALUES
('2025-07-29 13:19:55.675585', '2025-07-29 13:19:55.682013', 'd5370a8957ed4f79a0bbf47e931b06d9', 'DSB', 'DSB', 'DSB', 'e69edfe356fe484683ae93a593df2fe9', '94a77b664b5d4efab801ba8560d83fc8', 1),
('2025-07-29 13:19:36.190001', '2025-07-29 13:19:36.259542', 'e01dc1e29224468fab70d1f992a160c1', 'TANGI', 'TANGI', 'TANGI', 'e69edfe356fe484683ae93a593df2fe9', '94a77b664b5d4efab801ba8560d83fc8', 1);

-- --------------------------------------------------------

--
-- Table structure for table `aix_customermodel`
--

CREATE TABLE `aix_customermodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `address_1` varchar(70) NOT NULL,
  `address_2` varchar(70) DEFAULT NULL,
  `city` varchar(70) DEFAULT NULL,
  `state` varchar(70) DEFAULT NULL,
  `zip_code` varchar(20) DEFAULT NULL,
  `country` varchar(70) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `website` varchar(200) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `customer_name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `active` tinyint(1) NOT NULL,
  `hidden` tinyint(1) NOT NULL,
  `additional_info` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`additional_info`)),
  `business_industry_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `nation_id` char(32) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_customermodel`
--

INSERT INTO `aix_customermodel` (`created`, `updated`, `address_1`, `address_2`, `city`, `state`, `zip_code`, `country`, `email`, `website`, `phone`, `uuid`, `customer_name`, `description`, `active`, `hidden`, `additional_info`, `business_industry_id`, `entity_id`, `nation_id`, `user_id`) VALUES
('2024-10-15 05:34:23.099802', '2024-10-15 06:30:57.670250', 'P.O.Box', NULL, 'Kampala', 'Kampala', '256', NULL, 'mandonpolo@gmail.com', 'http://www.google.com', '+256', '8844b93b0dee4a77afb91daa81968f61', 'Default', '', 1, 0, NULL, 'f585f3c11b02422d9e2bc1aee93d085a', '94a77b664b5d4efab801ba8560d83fc8', '0d20e8bab74e4d9cab6c3037bb415ebc', 2),
('2024-02-24 16:42:36.545821', '2024-02-25 03:06:35.549385', 'Plot 1144 Jinja Road', 'P.O.Box 1144 Kampala, Uganda', 'Kampala', 'Kampala', '256', NULL, 'info-ug@totalenergies.com', 'http://bro-group.com', '+256', 'e69edfe356fe484683ae93a593df2fe9', 'Total Energies', '', 1, 0, NULL, 'f585f3c11b02422d9e2bc1aee93d085a', '1980d2af5ea14ad5b1e7712771f60517', '0d20e8bab74e4d9cab6c3037bb415ebc', 3);

-- --------------------------------------------------------

--
-- Table structure for table `aix_departmentmodel`
--

CREATE TABLE `aix_departmentmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_departmentmodel`
--

INSERT INTO `aix_departmentmodel` (`created`, `updated`, `uuid`, `code`, `name`, `description`, `is_active`, `entity_id`) VALUES
('2024-03-22 07:48:27.601065', '2024-03-22 07:48:27.604540', '53793f4b57f74bf3ba363001fb2c7062', 'ADMIN', 'Adminstration', 'Administration', 1, '1980d2af5ea14ad5b1e7712771f60517'),
('2025-08-11 13:22:21.149877', '2025-08-11 13:22:21.157122', '951fe31763714bf1aacc15ead037e535', 'ACC', 'Accounts', 'Accounts', 1, '94a77b664b5d4efab801ba8560d83fc8'),
('2025-08-11 13:22:56.485310', '2025-08-11 13:22:56.488851', 'a17c9dfab04844e599c6bf92695a0035', 'OPS', 'Operations', 'Operations', 1, '94a77b664b5d4efab801ba8560d83fc8'),
('2025-08-11 13:22:42.496200', '2025-08-11 13:22:42.499725', 'b460516b1cbe4bf5a851c66d5b1b5c42', 'ADM', 'Administration', 'Administration', 1, '94a77b664b5d4efab801ba8560d83fc8');

-- --------------------------------------------------------

--
-- Table structure for table `aix_dependantmodel`
--

CREATE TABLE `aix_dependantmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `middle_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) NOT NULL,
  `date_of_birth` date NOT NULL,
  `gender` int(11) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `is_default` tinyint(1) NOT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `relationship_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_documentmodel`
--

CREATE TABLE `aix_documentmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `name` varchar(255) NOT NULL,
  `extension` varchar(255) NOT NULL,
  `name_on_file` varchar(255) DEFAULT NULL,
  `temp_key` varchar(255) DEFAULT NULL,
  `external_key` int(11) DEFAULT NULL,
  `mime_type` varchar(255) DEFAULT NULL,
  `size` double DEFAULT NULL,
  `description` longtext DEFAULT NULL,
  `doc_status_id` char(32) NOT NULL,
  `doc_type_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `activity_id` char(32) DEFAULT NULL,
  `task_id` char(32) DEFAULT NULL,
  `work_order_id` char(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_documentmodel`
--

INSERT INTO `aix_documentmodel` (`created`, `updated`, `uuid`, `name`, `extension`, `name_on_file`, `temp_key`, `external_key`, `mime_type`, `size`, `description`, `doc_status_id`, `doc_type_id`, `entity_id`, `activity_id`, `task_id`, `work_order_id`) VALUES
('2025-08-26 10:21:16.477994', '2025-08-26 10:21:16.477994', '01e58702fe3c4f238aec8757f3a76de3', 'ML', '', NULL, NULL, 0, NULL, NULL, 'LPN', 'd718b93cbcc048e0a7d58f6622f4f5e6', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 13:08:55.325351', '2025-08-27 13:08:55.326376', '05ae8ee6a0954c1fa1b49514f6774a05', 'Operator Cert for 20Ton crane', '', NULL, NULL, 0, NULL, NULL, 'Operator Cert for 20Ton crane', 'd718b93cbcc048e0a7d58f6622f4f5e6', '0b7bf37c1e3149a285f0ac34bb9aa6cd', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 07:41:18.458881', '2025-08-27 07:50:45.981271', '0a6bd37f0a3444feb2efde3747560941', 'Lifting Plan', 'jpg', '/media/app-server.jpg', NULL, 0, 'image/jpeg', 130479, 'Lifting Plan', '04e92c379305473abf205cf22433cf62', '0b7bf37c1e3149a285f0ac34bb9aa6cd', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, '72694865b2fc4437b21abd7c20caff19'),
('2025-08-27 06:46:41.056367', '2025-08-27 06:46:41.056367', '0f635dd05812495b9e223132822376f2', 'query1.png', 'png', '/media/query1.png', NULL, 0, 'image/png', 178803, NULL, 'd718b93cbcc048e0a7d58f6622f4f5e6', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 06:45:10.803233', '2025-08-27 06:45:10.803233', '0fbce3c763924b7f855e2bdf7da1d392', 'Operator Certificate for 1501', '', NULL, NULL, 0, NULL, NULL, 'Operator Certificate for Forklift Crane', 'd718b93cbcc048e0a7d58f6622f4f5e6', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 12:00:21.628366', '2025-08-29 07:38:36.348878', '124b3e21d5e6474c9064739284a2d6bb', 'Transport Services for Telehandler', 'pdf', '/media/Family-Membership.pdf', NULL, 0, 'application/pdf', 725687, 'Transport Services for Telehandler', 'd718b93cbcc048e0a7d58f6622f4f5e6', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, '8bbde9493eb8433098aa53734f29388f', NULL),
('2025-08-27 07:41:18.470589', '2025-08-27 07:41:18.470589', '1be2b87cd5e949c98261e29eac447cd9', 'Lifting Plan', '', NULL, NULL, 0, NULL, NULL, 'Lifting Plan for forklift\r\n- Flatbed\r\n- 10Ton Crane', '04e92c379305473abf205cf22433cf62', '0b7bf37c1e3149a285f0ac34bb9aa6cd', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-26 10:22:31.539780', '2025-08-26 10:22:31.539780', '1d2b5d8ce55749d0a44746f8bece1d91', 'MGK', '', NULL, NULL, 0, NULL, NULL, 'MKO', 'de9d8a4b81e943488c58ebe303bf9fc8', '0b7bf37c1e3149a285f0ac34bb9aa6cd', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 13:08:55.293116', '2025-08-29 07:41:35.954774', '2634fb4cb96f4428bbe2cd34c48ba8ad', 'Operator Cert for 20Ton crane', 'pdf', '/media/FSENKUMBA_230907-083809-4f.pdf', NULL, 0, 'application/pdf', 189968, 'Operator Cert for 20Ton crane\r\n- UAX 773M', 'd718b93cbcc048e0a7d58f6622f4f5e6', '0b7bf37c1e3149a285f0ac34bb9aa6cd', '94a77b664b5d4efab801ba8560d83fc8', 'eb4cf45b87034836b5b55c533dcaaba9', NULL, NULL),
('2025-08-27 08:57:55.781031', '2025-08-27 08:57:55.782032', '2aa0de8417c54bfeb526184997a0c755', 'Transport Plan for 1501', '', NULL, NULL, 0, NULL, NULL, 'Transport Plan for 1501 for 5Ton Crane', 'de9d8a4b81e943488c58ebe303bf9fc8', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 06:40:23.313067', '2025-08-27 06:40:23.314095', '2f9ebd52f9cf4b85b4dcbbf038e012a1', 'AA1pLCrZ.jpg', 'jpg', '/media/AA1pLCrZ.jpg', NULL, 0, 'image/jpeg', 262144, NULL, '04e92c379305473abf205cf22433cf62', '0b7bf37c1e3149a285f0ac34bb9aa6cd', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 06:45:10.790733', '2025-08-27 06:45:10.790733', '31766d1718824b55bb3141de908529b2', 'Desktop1.jpg', 'jpg', '/media/Desktop1.jpg', NULL, 0, 'image/jpeg', 3887889, NULL, 'd718b93cbcc048e0a7d58f6622f4f5e6', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-26 10:25:03.918022', '2025-08-26 10:25:03.918022', '3180a529699e4bf29c705c9b7f37da19', 'LPFG', '', NULL, NULL, 0, NULL, NULL, 'OPAB', 'd718b93cbcc048e0a7d58f6622f4f5e6', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 13:08:55.304600', '2025-08-29 07:42:35.799899', '365393ab71254c94a191b15c8d47a5bc', 'Operator Cert for 15Ton crane', 'jpg', '/media/IMG-20230705-WA0114-mod.jpg', NULL, 0, 'image/jpeg', 114463, 'Operator Cert for 15Ton crane\r\n- UAM 845K', 'd718b93cbcc048e0a7d58f6622f4f5e6', '0b7bf37c1e3149a285f0ac34bb9aa6cd', '94a77b664b5d4efab801ba8560d83fc8', 'eb4cf45b87034836b5b55c533dcaaba9', NULL, NULL),
('2025-08-27 06:34:58.712482', '2025-08-27 06:34:58.713980', '3aa0878657eb4763a7ff1db44984fbae', 'AA1pLCrZ.jpg', 'jpg', '/media/AA1pLCrZ.jpg', NULL, 0, 'image/jpeg', 262144, NULL, '04e92c379305473abf205cf22433cf62', '0b7bf37c1e3149a285f0ac34bb9aa6cd', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 07:41:18.465087', '2025-08-27 07:51:52.551996', '4bead3ac7f8f435c9cc3187ef53104ee', 'Lifting Plan for Crane', 'JPG', '/media/DSC_0056.JPG', NULL, 0, 'image/jpeg', 695929, 'Lifting Plan for Crane', '04e92c379305473abf205cf22433cf62', '0b7bf37c1e3149a285f0ac34bb9aa6cd', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, '72694865b2fc4437b21abd7c20caff19'),
('2025-08-27 11:57:57.095000', '2025-08-27 11:57:57.099569', '4cfcd030f61f48fc89a72d2a7896a104', 'Transl', 'pdf', '/media/Family-Membership.pdf', NULL, 0, 'application/pdf', 725687, 'Tsanl', 'd718b93cbcc048e0a7d58f6622f4f5e6', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 11:42:19.493119', '2025-08-27 11:42:19.499872', '4de60f3e6539492690e99dd299a8595b', 'Transport', 'pdf', '/media/CPP Construction_220T Crane Quotes.pdf', NULL, 0, 'application/pdf', 1631295, 'Transport', 'd718b93cbcc048e0a7d58f6622f4f5e6', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 06:46:41.065618', '2025-08-27 06:46:41.065618', '506384d2447348499bb4ac1eb18dca34', 'wet-manchester-united-poster-bav110qq6mx5avvh.jpg', 'jpg', '/media/wet-manchester-united-poster-bav110qq6mx5avvh.jpg', NULL, 0, 'image/jpeg', 339631, NULL, 'd718b93cbcc048e0a7d58f6622f4f5e6', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 08:19:10.945994', '2025-08-27 08:19:10.945994', '60956770acac4cc88c4292c444342ac4', 'Operator Cert', '', NULL, NULL, 0, NULL, NULL, 'Operator Cert', 'd718b93cbcc048e0a7d58f6622f4f5e6', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 11:51:36.717201', '2025-08-27 11:51:36.717201', '60e8cec3ba7a401d898e128579c0aa85', 'Transport', '', NULL, NULL, 0, NULL, NULL, 'Transport', 'd718b93cbcc048e0a7d58f6622f4f5e6', '0b7bf37c1e3149a285f0ac34bb9aa6cd', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 06:34:58.727012', '2025-08-27 06:34:58.727012', '6cfde4720c7f4e19853a8384b0abbb30', 'AA1pLork.jpg', 'jpg', '/media/AA1pLork.jpg', NULL, 0, 'image/jpeg', 262144, NULL, '04e92c379305473abf205cf22433cf62', '0b7bf37c1e3149a285f0ac34bb9aa6cd', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-26 10:17:16.433177', '2025-08-26 10:17:16.433177', '6f67a452e2734014ae628f0834dc7f5a', 'Lifting Plan', '', NULL, NULL, 0, NULL, NULL, 'RG Lifting Plan', '04e92c379305473abf205cf22433cf62', '0b7bf37c1e3149a285f0ac34bb9aa6cd', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 06:40:23.336187', '2025-08-27 06:40:23.337205', '7072779f04dc4bcaa73bd38c85a737f1', 'Lifting Plan', '', NULL, NULL, 0, NULL, NULL, 'Lifting Plan for Rig Move', '04e92c379305473abf205cf22433cf62', '0b7bf37c1e3149a285f0ac34bb9aa6cd', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 13:04:49.530572', '2025-08-27 13:04:49.530572', '7373d6798e8e4ac2a5943621a27859a9', 'Operator Cert for 20Ton crane', 'JPG', '/media/DSC_0047.JPG', NULL, 0, 'image/jpeg', 520531, 'Operator Cert for 20Ton crane', '04e92c379305473abf205cf22433cf62', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 12:54:53.749888', '2025-08-27 12:54:53.749888', '7c9bcf6ca5e344c4ae817a807c7623b1', 'Operator Cert for 20Ton crane', 'pdf', '/media/CPP Construction_220T Crane Quote.pdf', NULL, 0, 'application/pdf', 468070, 'Operator Cert for 20Ton crane', '04e92c379305473abf205cf22433cf62', '0b7bf37c1e3149a285f0ac34bb9aa6cd', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 11:42:56.020564', '2025-08-27 11:42:56.020564', '816a06bca0d448d296b410905e6d96da', 'Transport', '', NULL, NULL, 0, NULL, NULL, 'Transport', 'd718b93cbcc048e0a7d58f6622f4f5e6', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-26 10:19:02.941781', '2025-08-26 10:19:02.941781', '8b9a4d2fb4d0442f8a6a2cb6efb6c1e1', 'LFT', '', NULL, NULL, 0, NULL, NULL, 'LPL', 'd718b93cbcc048e0a7d58f6622f4f5e6', '0b7bf37c1e3149a285f0ac34bb9aa6cd', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 11:51:36.705545', '2025-08-27 11:51:36.710029', '8bf2430a15f84c67892750dfb04fab1e', 'Transport', 'pdf', '/media/FSENKUMBA_230907-083809-4f.pdf', NULL, 0, 'application/pdf', 189968, 'Transport', 'd718b93cbcc048e0a7d58f6622f4f5e6', '0b7bf37c1e3149a285f0ac34bb9aa6cd', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 08:19:10.943071', '2025-08-27 08:19:10.944487', '9b48c1938f2f4fd2963b6b926989a9bd', 'Operator Cert', 'JPG', '/media/DSC_0047.JPG', NULL, 0, 'image/jpeg', 520531, 'Operator Cert', 'd718b93cbcc048e0a7d58f6622f4f5e6', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, '72694865b2fc4437b21abd7c20caff19'),
('2025-08-27 11:55:15.818629', '2025-08-27 11:55:15.825238', '9da5714a8a2e40c49559114176e5663e', 'Transport', 'JPG', '/media/DSC_0047.JPG', NULL, 0, 'image/jpeg', 520531, 'Tranzi', '04e92c379305473abf205cf22433cf62', '0b7bf37c1e3149a285f0ac34bb9aa6cd', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-29 07:19:25.619692', '2025-08-29 07:19:25.619692', 'a69edbd9ca584c778a9ed43c75c2a025', 'Lifting Plan for Telehandler', '', NULL, NULL, 0, NULL, NULL, 'Lifting Plan for Telehandler', '04e92c379305473abf205cf22433cf62', '0b7bf37c1e3149a285f0ac34bb9aa6cd', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 11:42:19.506402', '2025-08-27 11:42:19.506402', 'ab0f2e6930f64cecb30b54bad196cf0b', 'Transport', '', NULL, NULL, 0, NULL, NULL, 'Transport', 'd718b93cbcc048e0a7d58f6622f4f5e6', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 06:46:41.074398', '2025-08-27 06:46:41.075666', 'ae786f95c2014d069fac8df7080b5d07', 'Operator Certificate for 1501', '', NULL, NULL, 0, NULL, NULL, 'Operator Certificate for Flatbed', 'd718b93cbcc048e0a7d58f6622f4f5e6', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 07:01:19.757670', '2025-08-27 07:01:19.763187', 'b371d042017240a8925d773cf5748d65', 'c03209023.webp', 'webp', '/media/c03209023.webp', NULL, 0, 'image/webp', 19230, NULL, '04e92c379305473abf205cf22433cf62', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, '72694865b2fc4437b21abd7c20caff19'),
('2025-08-29 07:21:36.751827', '2025-08-29 07:21:36.751827', 'b4d8800d62014b318109c9363ab476d0', 'Transport Services', '', NULL, NULL, 0, NULL, NULL, 'Transport for Staff to and from the Camp', 'd718b93cbcc048e0a7d58f6622f4f5e6', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 08:57:55.777031', '2025-08-27 08:57:55.779032', 'b6f98d3833b848f5aebb35bed6281083', 'Transport Plan for 1501', 'JPG', '/media/DSC_0047.JPG', NULL, 0, 'image/jpeg', 520531, 'Transport Plan for 1501 for 5Ton Crane', 'de9d8a4b81e943488c58ebe303bf9fc8', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 13:04:25.056273', '2025-08-27 13:04:25.057712', 'b744df20e5f747d6b04b58652b068932', 'Operator Cert for 20Ton crane', 'JPG', '/media/DSC_0047.JPG', NULL, 0, 'image/jpeg', 520531, 'Operator Cert for 20Ton crane', '04e92c379305473abf205cf22433cf62', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-26 10:24:13.906743', '2025-08-26 10:24:13.906743', 'bafe918a4b624a7aaad536b602ebd2fb', 'LYU', '', NULL, NULL, 0, NULL, NULL, 'LYU', '04e92c379305473abf205cf22433cf62', '0b7bf37c1e3149a285f0ac34bb9aa6cd', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-29 07:30:09.420250', '2025-08-29 07:30:09.420250', 'bb012e6ae3474183aad5862688179d9b', 'Transport Services for Telehandler', '', NULL, NULL, 0, NULL, NULL, 'Transport Services for Telehandler', 'd718b93cbcc048e0a7d58f6622f4f5e6', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 08:19:10.939073', '2025-08-27 08:19:10.940071', 'bcfeb197b8a1419fb2d3e7a9f33a2e85', 'Operator Cert', 'JPG', '/media/DSC_0045.JPG', NULL, 0, 'image/jpeg', 472519, 'Operator Cert', 'd718b93cbcc048e0a7d58f6622f4f5e6', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, '72694865b2fc4437b21abd7c20caff19'),
('2025-08-27 06:40:23.323631', '2025-08-27 06:40:23.323631', 'c447d227016f41f392b077bea217a8eb', 'AA1pLork.jpg', 'jpg', '/media/AA1pLork.jpg', NULL, 0, 'image/jpeg', 262144, NULL, '04e92c379305473abf205cf22433cf62', '0b7bf37c1e3149a285f0ac34bb9aa6cd', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 12:00:21.641512', '2025-08-27 12:00:21.641512', 'cb2c894d0a314372af2d3d770bd307b1', 'Transl', '', NULL, NULL, 0, NULL, NULL, 'Trans', '04e92c379305473abf205cf22433cf62', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 11:57:57.105890', '2025-08-27 11:57:57.105890', 'cf92b80c75824411bfe6b3ecdeb249a5', 'Transl', '', NULL, NULL, 0, NULL, NULL, 'Tsanl', 'd718b93cbcc048e0a7d58f6622f4f5e6', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 12:52:01.685040', '2025-08-27 12:52:01.685040', 'd8c4354b12a549d4b68f6c436179843a', 'Operator Cert for 20Ton crane', 'pdf', '/media/CPP Construction_220T Crane Quote.pdf', NULL, 0, 'application/pdf', 468070, 'Operator Cert for 20Ton crane', '04e92c379305473abf205cf22433cf62', '0b7bf37c1e3149a285f0ac34bb9aa6cd', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 12:00:21.606473', '2025-08-29 07:39:45.053603', 'dc5a40d212a14d9ea9b91408753b1413', 'Transport Services for Van', 'pdf', '/media/CPP Construction_220T Crane Quotes.pdf', NULL, 0, 'application/pdf', 1631295, 'Transport Services for Van to transport Staff from Bugungu Camp to DSB Site', 'd718b93cbcc048e0a7d58f6622f4f5e6', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, '8bbde9493eb8433098aa53734f29388f', NULL),
('2025-08-27 12:58:17.627063', '2025-08-27 12:58:17.627063', 'dd413348a0f6466cb2d0ea03dbab6a30', 'Operator Cert for 20Ton crane', 'pdf', '/media/CPP Construction_220T Crane Quote.pdf', NULL, 0, 'application/pdf', 468070, 'Operator Cert for 20Ton crane', '04e92c379305473abf205cf22433cf62', '0b7bf37c1e3149a285f0ac34bb9aa6cd', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 06:45:10.800056', '2025-08-27 06:45:10.800056', 'e38246b20d5940069f47fd5fb4577c01', 'guitars-g2a0cf4a62_1280.jpg', 'jpg', '/media/guitars-g2a0cf4a62_1280.jpg', NULL, 0, 'image/jpeg', 284408, NULL, 'd718b93cbcc048e0a7d58f6622f4f5e6', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 08:57:55.763653', '2025-08-27 08:57:55.773507', 'e902a62e11cb43109d345d6f047edada', 'Transport Plan for 1501', 'pdf', '/media/CPP Construction_220T Crane Quote.pdf', NULL, 0, 'application/pdf', 468070, 'Transport Plan for 1501 for 5Ton Crane', 'de9d8a4b81e943488c58ebe303bf9fc8', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 11:55:15.831776', '2025-08-27 11:55:15.831776', 'f34a6c55a97145b3941366ff03b7a298', 'Transport', '', NULL, NULL, 0, NULL, NULL, 'Tranzi', '04e92c379305473abf205cf22433cf62', '0b7bf37c1e3149a285f0ac34bb9aa6cd', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 11:42:56.002990', '2025-08-27 11:42:56.012957', 'f8a089a6d3a3447aa562c90fb5a25477', 'Transport', 'pdf', '/media/CPP Construction_220T Crane Quotes.pdf', NULL, 0, 'application/pdf', 1631295, 'Transport', 'd718b93cbcc048e0a7d58f6622f4f5e6', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL),
('2025-08-27 07:01:19.774211', '2025-08-27 07:01:19.774211', 'fc0b208b3bfe4e5ebb85954ef68f5b6a', 'Inspection Cert for 1501', '', NULL, NULL, 0, NULL, NULL, 'Inspection forms certificate for 1501 HSE', '04e92c379305473abf205cf22433cf62', 'fbef4ff7508b4ba29e3f915100f69325', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `aix_documentstatusmodel`
--

CREATE TABLE `aix_documentstatusmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_documentstatusmodel`
--

INSERT INTO `aix_documentstatusmodel` (`created`, `updated`, `uuid`, `code`, `name`, `description`, `entity_id`) VALUES
('2025-08-26 09:41:16.083650', '2025-08-26 09:41:16.090908', '04e92c379305473abf205cf22433cf62', 'DFT', 'DRAFT', 'DRAFT', '94a77b664b5d4efab801ba8560d83fc8'),
('2025-08-26 09:50:36.957713', '2025-08-26 09:50:36.960714', 'd718b93cbcc048e0a7d58f6622f4f5e6', 'APR', 'APPROVED', 'APPROVED', '94a77b664b5d4efab801ba8560d83fc8'),
('2025-08-26 09:26:57.712593', '2025-08-26 09:26:57.717970', 'de9d8a4b81e943488c58ebe303bf9fc8', 'IND', 'INCOMING DOCUMENT', 'INCOMING DOCUMENT', '94a77b664b5d4efab801ba8560d83fc8');

-- --------------------------------------------------------

--
-- Table structure for table `aix_documenttypemodel`
--

CREATE TABLE `aix_documenttypemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_documenttypemodel`
--

INSERT INTO `aix_documenttypemodel` (`created`, `updated`, `uuid`, `code`, `name`, `description`, `is_active`, `entity_id`) VALUES
('2025-08-26 09:25:19.289542', '2025-08-26 09:25:19.321991', '0b7bf37c1e3149a285f0ac34bb9aa6cd', 'LPL', 'LIFTING PLAN', 'LIFTING PLAN', 1, '94a77b664b5d4efab801ba8560d83fc8'),
('2025-08-26 09:25:39.275722', '2025-08-26 09:25:39.277146', 'fbef4ff7508b4ba29e3f915100f69325', 'OPC', 'OPERATOR CERTIFICATE', 'OPERATOR CERTIFICATE', 1, '94a77b664b5d4efab801ba8560d83fc8');

-- --------------------------------------------------------

--
-- Table structure for table `aix_educationmodel`
--

CREATE TABLE `aix_educationmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `specialization` varchar(255) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT NULL,
  `year_completed` date DEFAULT NULL,
  `comment` longtext DEFAULT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `qualification_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_employeeassignmentmodel`
--

CREATE TABLE `aix_employeeassignmentmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `job_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_employeeavatarmodel`
--

CREATE TABLE `aix_employeeavatarmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `name` varchar(255) NOT NULL,
  `extension` varchar(255) NOT NULL,
  `mime_type` varchar(255) NOT NULL,
  `size` double NOT NULL,
  `description` longtext DEFAULT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_employeecontractmodel`
--

CREATE TABLE `aix_employeecontractmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT NULL,
  `completed` tinyint(1) NOT NULL,
  `comment` longtext DEFAULT NULL,
  `contract_type_id` char(32) NOT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_employeecontracttypemodel`
--

CREATE TABLE `aix_employeecontracttypemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_employeefawmodel`
--

CREATE TABLE `aix_employeefawmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(50) NOT NULL,
  `faw_date` date DEFAULT NULL,
  `entity_id` char(32) NOT NULL,
  `location_id` char(32) NOT NULL,
  `work_order_id` char(32) NOT NULL,
  `faw_status` varchar(15) DEFAULT NULL,
  `approved_date` date DEFAULT NULL,
  `canceled_date` date DEFAULT NULL,
  `draft_date` date DEFAULT NULL,
  `fulfillment_date` date DEFAULT NULL,
  `in_review_date` date DEFAULT NULL,
  `void_date` date DEFAULT NULL,
  `markdown_notes` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_employeefawmodel`
--

INSERT INTO `aix_employeefawmodel` (`created`, `updated`, `uuid`, `code`, `faw_date`, `entity_id`, `location_id`, `work_order_id`, `faw_status`, `approved_date`, `canceled_date`, `draft_date`, `fulfillment_date`, `in_review_date`, `void_date`, `markdown_notes`) VALUES
('2025-08-14 11:44:46.915640', '2025-08-18 13:38:22.284347', '34b2ff0dad1f4d3ebcf8816b2201f861', 'FAWKXMR53AVG3', '2025-08-08', '94a77b664b5d4efab801ba8560d83fc8', 'd5370a8957ed4f79a0bbf47e931b06d9', '72694865b2fc4437b21abd7c20caff19', 'draft', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('2025-08-14 11:45:23.309314', '2025-08-14 11:45:23.316061', 'b62649ce6f704cf4b6a5c1094e6c0ef6', 'FAWIKQKB7YGO9', '2025-08-12', '94a77b664b5d4efab801ba8560d83fc8', 'e01dc1e29224468fab70d1f992a160c1', '72694865b2fc4437b21abd7c20caff19', 'draft', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('2025-08-14 11:43:10.557939', '2025-08-18 13:37:41.038063', 'd85d632fbc0749828eb3abe247070154', 'FAW8XEMPCRKAL', '2025-08-04', '94a77b664b5d4efab801ba8560d83fc8', 'e01dc1e29224468fab70d1f992a160c1', '72694865b2fc4437b21abd7c20caff19', 'draft', NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `aix_employeelanguagemodel`
--

CREATE TABLE `aix_employeelanguagemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `read` tinyint(1) NOT NULL,
  `write` tinyint(1) NOT NULL,
  `speak` tinyint(1) NOT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `language_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_employeelicensedetailmodel`
--

CREATE TABLE `aix_employeelicensedetailmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `issue_date` date NOT NULL,
  `expiry_date` date DEFAULT NULL,
  `valid` tinyint(1) NOT NULL,
  `comment` longtext DEFAULT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `license_type_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_employeelicensetypemodel`
--

CREATE TABLE `aix_employeelicensetypemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_employeemodel`
--

CREATE TABLE `aix_employeemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `idnumber` varchar(255) DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `designation` varchar(255) DEFAULT NULL,
  `nationality` varchar(255) DEFAULT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `dateofbirth` date DEFAULT NULL,
  `contactnumber` varchar(255) DEFAULT NULL,
  `emergencycontact` varchar(255) DEFAULT NULL,
  `contractstartdate` date DEFAULT NULL,
  `locationsite` varchar(255) DEFAULT NULL,
  `passportidno` varchar(255) DEFAULT NULL,
  `permitissuedate` date DEFAULT NULL,
  `permitexpirydate` date DEFAULT NULL,
  `medicalstartdate` date DEFAULT NULL,
  `medicalexpirydate` date DEFAULT NULL,
  `operatorstartdate` date DEFAULT NULL,
  `operatorexpirydate` date DEFAULT NULL,
  `defensivestartdate` date DEFAULT NULL,
  `defensiveexpirydate` date DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  `woStatus` varchar(50) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `imageUrl` longtext DEFAULT NULL,
  `department_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `username_id` int(11) DEFAULT NULL,
  `id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_employeemodel`
--

INSERT INTO `aix_employeemodel` (`created`, `updated`, `uuid`, `idnumber`, `name`, `designation`, `nationality`, `gender`, `dateofbirth`, `contactnumber`, `emergencycontact`, `contractstartdate`, `locationsite`, `passportidno`, `permitissuedate`, `permitexpirydate`, `medicalstartdate`, `medicalexpirydate`, `operatorstartdate`, `operatorexpirydate`, `defensivestartdate`, `defensiveexpirydate`, `category`, `woStatus`, `status`, `imageUrl`, `department_id`, `entity_id`, `username_id`, `id`) VALUES
('2024-03-22 08:15:02.267501', '2024-03-22 08:15:02.267501', '02bf25668b5d4964ad1e03d2524f1003', 'TW008', 'HATANGA EDSON', 'Crane Operator', 'National', 'Male', '1987-01-25', '788775124', '774358750', '2022-12-26', 'SLB', '', '2020-11-10', '2023-11-09', '2022-12-24', '2023-12-24', '2022-12-22', '2024-12-22', '1970-01-01', '1970-01-01', 'NULL', 'ALLOCATED', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.280053', '2024-03-22 08:15:02.280053', '0600b3bc069f4f8c9dc7263de61299a5', 'TW093', 'ODYERO TONY', 'Bus Driver', 'National', 'Male', '1974-12-25', '772420600', '782384521', '2023-05-01', 'Total-DSB', '', '2022-06-11', '2027-06-10', '2022-07-21', '2023-07-21', '2023-06-01', '2023-06-01', '2022-07-01', '2023-07-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.280053', '2024-03-22 08:15:02.280053', '06ceefa18855477e9f9b7bfc82df4055', 'TW045', 'EDRISA SSERUWAGE', 'Transport Coordinator', 'National', 'Male', '1965-01-10', '772640142', '', '2023-01-01', 'CNOOC', '', '2021-10-19', '2024-10-18', '2023-10-21', '2024-10-20', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', 1, NULL),
('2024-03-22 08:15:02.271420', '2024-03-22 08:15:02.271420', '07be9ce8d7684d85b9b934529487704d', 'TW089', 'FRANCIS AWATE', 'Materiel Handler', 'National', 'Male', '1997-03-07', '778578376', '', '2023-03-01', 'SLB', '', '2023-06-01', '2023-06-01', '2023-07-06', '2024-07-05', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.266420', '2024-03-22 08:15:02.266420', '0906b80065044e1aae322eeb0a1f8bde', 'TW011', 'PAUL EDYAU', 'Site supervisor', 'National', 'Male', '1976-05-28', '776622312', '780398929', '2022-12-13', 'Total-DSB', '', '2020-10-06', '2023-10-06', '2022-12-08', '2023-12-08', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'ALLOCATED', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.270407', '2024-03-22 08:15:02.270407', '09b71d200b574aabb815544f32645fc2', 'TW022', 'CHARLES KIRINYA', 'Light Duty Driver', 'National', 'Male', '1975-06-24', '782342661', '701773343', '2023-09-01', 'Total-DSB', '', '2022-05-27', '2025-05-26', '2022-12-24', '2023-12-24', '2023-06-01', '2023-06-01', '2023-03-08', '2024-03-07', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.267501', '2024-03-22 08:15:02.267501', '0c30e4ace3584eb8b68eefc658081359', 'TW016', 'ABDUL BWOGI ', 'Forklift & Telehandler Operator', 'National', 'Male', '1976-02-08', '776819024', '774949123', '2022-12-26', 'Total-DSB', '', '2020-12-07', '2023-12-07', '2022-12-24', '2023-12-24', '2022-12-29', '2024-12-29', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.268531', '2024-03-22 08:15:02.268531', '0c44a9f3cdd347bc9f8a6b0efb842cb1', 'TW057', 'RAYMOND KUTEGEKA ', 'Forklift & Telehandler Operator', 'National', 'Male', '1990-06-13', '788724067', '779019455', '2023-01-25', 'Total-DSB', '', '2022-09-02', '2023-09-01', '2023-03-21', '2024-03-20', '2023-01-16', '2025-01-16', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'ALLOCATED', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.268531', '2024-03-22 08:15:02.268531', '0c4f1942e6ea462b810aee80ddcf3b03', 'TW054', 'JAMES BBOMBOKKA', 'H3SE Superintendent', 'National', 'Male', '1993-01-19', '776839100', '777696091', '2023-01-01', 'CNOOC', '', '2023-06-01', '2023-06-01', '2022-12-29', '2023-12-29', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.270407', '2024-03-22 08:15:02.270407', '0f80bff7bfb44b68b47d3579982b0994', 'TW024', 'ALEX GASANA', 'Light Duty Driver', 'National', 'Male', '1968-01-01', '772602777', '772590295', '2023-12-28', 'CNOOC', '', '2022-02-17', '2025-02-16', '2022-09-10', '2023-09-10', '2023-06-01', '2023-06-01', '2022-07-01', '2023-07-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.267501', '2024-03-22 08:15:02.267501', '0f90e158f0c4473cb58078aaf92c20c3', 'TW061', 'DENISH OMENA  OKEMA', 'Crane Operator', 'National', 'Male', '1981-07-27', '776639749', '778033600', '2023-06-02', 'KARMOD BETA', '', '2022-03-21', '2025-03-20', '2023-05-26', '2024-05-25', '2021-07-05', '2023-07-05', '2023-06-01', '2023-06-01', 'NULL', 'ALLOCATED', 'ALLOCATED', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.274023', '2024-03-22 08:15:02.274023', '0fd2ab8533a846b1b4ee55224ae59635', 'TW035', 'CWINYA AL-JERRY', 'Banksman', 'National', 'Male', '1980-01-18', '782040940', '', '2023-04-14', 'Total-TGI', '', '2023-06-01', '2023-06-01', '2022-10-25', '2023-10-25', '2022-08-06', '2024-08-06', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.271420', '2024-03-22 08:15:02.271420', '1051867e6db140f48c6e7c85ae1f0409', 'TW069', 'HENRY KASWABULI ', 'Light Duty Driver', 'National', 'Male', '1984-09-15', '780927957', '782343800', '2023-06-02', 'Total-DSB', '', '2022-06-03', '2025-06-03', '2023-02-02', '2024-02-02', '2023-06-01', '2023-06-01', '2023-04-01', '2024-04-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.272919', '2024-03-22 08:15:02.272919', '132d8537c0c349b99890e33e12eeac75', 'TW033', 'SEFU MUZEI ', 'Banksman', 'National', 'Male', '1989-05-15', '782516851', '777187675', '2023-01-14', 'Total-DSB', '', '2023-06-01', '2023-06-01', '2022-10-25', '2023-10-25', '2022-08-31', '2024-08-31', '2023-06-01', '2023-06-01', 'NULL', 'ALLOCATED', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.272407', '2024-03-22 08:15:02.272407', '13a9a56aa6b44cfc88392e3835db3197', 'TW087', 'FRANK MASEMBE ', 'Materiel Handler', 'National', 'Male', '1986-02-24', '750683150', '', '2023-03-01', 'CNOOC', '', '2023-06-01', '2023-06-01', '2023-03-18', '2024-03-17', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.270407', '2024-03-22 08:15:02.270407', '13f65e09bf2e4f9f982d0f69139e6a3e', 'TW082', 'MBAGIRA VINCENT', 'Light Duty Driver', 'National', 'Male', '1984-01-03', '772077007', '784813325', '2023-02-27', 'Total-DSB', '', '2023-04-20', '2024-04-19', '2023-02-27', '2024-02-27', '2023-06-01', '2023-06-01', '2023-04-01', '2024-04-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.268531', '2024-03-22 08:15:02.268531', '178b21b7aa3b492caf5a5c7d9b39e3a8', 'TW070', 'IRAD AKATWIJUKA', 'H3SE Superintendent', 'National', 'Male', '1994-08-18', '751046929', '705969889', '2023-11-02', 'CNOOC', '', '2023-06-01', '2023-06-01', '2023-02-08', '2024-02-08', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.269405', '2024-03-22 08:15:02.269405', '1790acbfcf2d4dbc839237741271739e', 'TW041', 'RAJAB SIMBWA ', 'Heavy Duty Driver', 'National', 'Male', '1977-10-20', '772385455', '779302236', '2023-01-01', 'CNOOC', '', '2021-11-25', '2024-11-24', '2023-02-02', '2024-02-02', '2023-06-01', '2023-06-01', '2022-10-01', '2023-10-01', 'NULL', 'NULL', 'ALLOCATED', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.269405', '2024-03-22 08:15:02.269405', '1a3289abf9de4027bb4d4a67e92fbd36', 'TW044', 'SAM BARONGO ', 'Heavy Duty Driver', 'National', 'Male', '1984-05-12', '774071267', '780738419', '2023-01-01', 'CNOOC', '', '2021-09-17', '2024-09-16', '2023-05-13', '2024-05-12', '2023-06-01', '2023-06-01', '2023-04-01', '2024-04-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.278024', '2024-03-22 08:15:02.278024', '1d1bf082c0904e36a5a7149f0c1ddfb6', 'TW051', 'KENETH GILBERT MATONGO', 'Banksman', 'National', 'Male', '1986-03-23', '779077262', '', '2023-01-01', 'Total-TGI', '', '2023-06-01', '2023-06-01', '2023-06-14', '2024-06-13', '2022-05-18', '2024-05-18', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.267501', '2024-03-22 08:15:02.267501', '1d28fdad184445ecbf1f8115bb66cae2', 'TW039', 'ABASI LUZZE ', 'Crane Operator', 'National', 'Male', '1983-03-13', '787142781', '761693181', '2023-01-01', 'CNOOC', '', '2021-12-22', '2024-12-21', '2023-02-27', '2024-02-27', '2022-02-19', '2024-02-19', '2022-07-01', '2023-07-01', 'NULL', 'NULL', 'ALLOCATED', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.279033', '2024-03-22 08:15:02.279033', '1e6dbfda57d34a4087bb9a51cf3f0742', 'TW077', 'SAMUEL OLIBORIT ', 'Mechanic', 'National', 'Male', '1970-07-28', '776525686', '772332280', '2023-01-28', 'CNOOC', '', '2023-06-01', '2023-06-01', '2023-01-24', '2024-01-24', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.271420', '2024-03-22 08:15:02.272407', '1f5599906ec848f18eddade2c17a1bb6', 'TW086', 'PATRICK WANDERA', 'Materiel Handler', 'National', 'Male', '1989-04-19', '755033070', '', '2023-03-01', 'SLB', '', '2023-06-01', '2023-06-01', '2023-03-16', '2024-03-15', '2023-03-12', '2025-03-12', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.270407', '2024-03-22 08:15:02.270407', '24073ccaba5b4063ae5b1b2c03aa8e08', 'TW003', 'STEVEN BYAMUKAMA', 'Light Duty Driver', 'National', 'Male', '1974-12-12', '776600022', '774172148', '2022-12-26', 'Total-DSB', '', '2021-03-10', '2024-03-09', '2022-12-22', '2023-12-22', '2023-06-01', '2023-06-01', '2022-12-01', '2023-12-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.269405', '2024-03-22 08:15:02.269405', '270569b4d0cf474896765916182b03c0', 'TW083', 'NYANZI TOM', 'Heavy Duty Driver', 'National', 'Male', '1973-07-23', '772455119', '757081196', '2023-01-01', 'Total-TGI', '', '2022-11-05', '2023-11-04', '2023-03-14', '2024-03-13', '2023-06-01', '2023-06-01', '2023-02-01', '2024-02-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.279033', '2024-03-22 08:15:02.279033', '32e0b65d36074d45bb1d261dbc94f90c', 'TW080', 'GEOFFREY SSERUYANGE', 'Junior Mechanic', 'National', 'Male', '1972-11-26', '788407933', '', '2023-01-01', 'CNOOC', '', '2023-06-01', '2023-06-01', '2023-03-01', '2024-02-29', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.280053', '2024-03-22 08:15:02.280053', '33b26a573ed24800a84a81b4697d092d', 'TW001', 'DAVID MUWONGE', 'Transport Coordinator', 'National', 'Male', '1967-05-03', '772509954', '', '2023-12-28', 'Total-DSB', '', '2020-10-24', '2023-10-25', '2022-12-08', '2023-12-08', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.277035', '2024-03-22 08:15:02.277035', '3c4353f99fa64098ac96831a9291a212', 'TW084', 'DENIS OKOT', 'Banksman', 'National', 'Male', '1982-07-20', '774355498', '774100247', '2023-06-01', 'Total-TGI', '', '2023-06-01', '2023-06-01', '2023-03-14', '2024-03-13', '2022-11-19', '2024-11-19', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.281028', '2024-03-22 08:15:02.281028', '4180ee8205854da58d2747c1cfd720b7', '', 'OBITA MICHEAL', 'Site Lifting Specialist', 'National', 'Male', '2023-06-01', '772398755', '789655000', '2023-06-01', '', '', '2023-06-01', '2023-06-01', '2023-06-01', '2000-12-30', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.271420', '2024-03-22 08:15:02.271420', '436c683484be41adb36c3e929204c57e', 'TW068', 'RAJAB MUKUNGU ', 'Light Duty Driver', 'National', 'Male', '1987-01-02', '704343595', '704701614', '2023-05-02', 'Total-TGI', '', '2022-10-17', '2025-10-16', '2023-02-02', '2024-02-02', '2023-06-01', '2023-06-01', '2023-04-01', '2024-04-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.280053', '2024-03-22 08:15:02.280053', '474a2d71846b43f6b0e0d65415018489', 'TW048', 'TOM OBONYO', 'Site Lifting Specialist', 'National', 'Male', '1977-03-06', '772319196', '', '2023-01-01', 'SLB', '', '2023-06-01', '2023-06-01', '2023-05-15', '2024-05-14', '2022-10-04', '2024-10-04', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.267501', '2024-03-22 08:15:02.267501', '4b086fd595d04d9085cb93e440c56dce', 'TW009', 'SAM MUGISHA', 'Crane Operator', 'National', 'Male', '1974-04-04', '777106956', '784177134', '2022-12-26', 'Total-TGI', '', '2022-08-10', '2023-08-10', '2022-12-24', '2023-12-24', '2022-12-22', '2024-12-22', '2023-06-01', '2023-06-01', 'NULL', 'ALLOCATED', 'ALLOCATED', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.279033', '2024-03-22 08:15:02.279033', '4c8aa269d1294c7db0080a3191be056d', 'TW018', 'WAISWA BALUWINE', 'Mechanic', 'National', 'Male', '1959-01-12', '789089000', '784974530', '2023-01-03', 'Total-DSB', '', '2023-06-01', '2023-06-01', '2022-12-19', '2023-12-19', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'ALLOCATED', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.277035', '2024-03-22 08:15:02.277035', '4eee5a7dec794d3eb1b06e5fa8737a2c', 'TW071', 'DENIS OCIRA', 'Banksman', 'National', 'Male', '1990-06-10', '777283183', '775261645', '2023-02-16', 'KARMOD BETA', '', '2023-06-01', '2023-06-01', '2023-02-13', '2024-02-13', '2022-12-22', '2024-12-22', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.269405', '2024-03-22 08:15:02.269405', '5313e2728ed942789e84e6c88ed24780', 'TW025', 'SAMUEL LUJJUMBA ', ' Heavy Duty Driver ', ' National ', ' Male ', '1966-05-04', '774071267', '772468624', '2023-01-01', ' Total-DSB ', '', '2023-06-15', '2028-06-14', '2023-02-09', '2024-02-09', '2023-06-01', '2023-06-01', '2023-02-01', '2024-02-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.269405', '2024-03-22 08:15:02.269405', '57dcac3a6c6d45b494cdb04663478a13', 'TW073', 'RICHARD SEKYANZI', 'Heavy Duty Driver', 'National', 'Male', '1962-11-10', '760262425', '700638297', '2023-01-01', 'Total-DSB', '', '2022-06-17', '2025-06-16', '2023-01-13', '2024-01-13', '2023-06-01', '2023-06-01', '2022-12-01', '2023-12-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.269405', '2024-03-22 08:15:02.269405', '5a9599fed23b4529a5c8e8e9682ce463', 'TW043', 'FRANCIS TOKIMANYA ', 'Heavy Duty Driver', 'National', 'Male', '1958-11-26', '774806934', '760491096', '2023-01-01', 'CNOOC', '', '2020-08-18', '2023-08-17', '2022-05-21', '2023-05-21', '2023-06-01', '2023-06-01', '2022-09-01', '2023-09-01', 'NULL', 'NULL', 'ALLOCATED', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.267501', '2024-03-22 08:15:02.267501', '5cb8fadf48954c36b2e97899b53c7b7e', 'TW026', 'ERIC KIRUMIRA', 'Crane Operator', 'National', 'Male', '1976-10-12', '754696493', '752972570', '2023-01-01', 'CNOOC', '', '2022-09-14', '2025-09-13', '2023-03-18', '2024-03-17', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'ALLOCATED', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.271420', '2024-03-22 08:15:02.271420', '5d1e2d8609f1474a9791f6b43df92d94', 'TW055', 'ASUMAN KATWALO ', 'Light Duty Driver', 'National', 'Male', '1984-08-02', '775544883', '775782883', '2023-01-01', 'Total-DSB', '', '2023-06-30', '2024-06-29', '2022-10-21', '2023-10-21', '2023-06-01', '2023-06-01', '2023-04-01', '2024-04-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.275035', '2024-03-22 08:15:02.275035', '5d29813ff30f4b97ad8b21e4890dcc98', 'TW032', 'FRANCIS OKOT INNOCENT', 'Banksman', 'National', 'Male', '1983-05-14', '784779242', '784779242', '2023-01-01', 'Total-DSB', '', '2023-06-01', '2023-06-01', '2023-03-02', '2024-03-01', '2022-02-19', '2024-02-19', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.271420', '2024-03-22 08:15:02.271420', '5e24d9ee0dfe4f12aecb088c02acec3d', 'TW078', 'MOSES MUWONGE ', 'Light Duty Driver', 'National', 'Male', '1956-01-01', '702995147', '757322142', '2023-01-01', 'Total-TGI', '', '2020-10-02', '2023-10-01', '2022-12-25', '2023-12-25', '2023-06-01', '2023-06-01', '2023-04-01', '2024-04-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.281028', '2024-03-22 08:15:02.281028', '606151086c834da8bc6559243bb5bb1c', 'TW097', 'CALEB ARINAITWE ', ' Forklift & Telehandler Operator ', '', '', '2023-06-01', '', '', '2023-06-01', '', '', '2023-06-01', '2023-06-01', '2023-06-01', '2000-12-30', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.274023', '2024-03-22 08:15:02.274023', '634737625e924e22a2bf5ec09d4ba832', 'TW020', 'KARIM SSEMAMBO', 'Banksman', 'National', 'Male', '1987-07-16', '779164437', '', '2023-03-01', 'ZPEB', '', '2023-06-01', '2023-06-01', '2023-01-03', '2024-01-03', '2021-10-21', '2023-10-21', '2023-06-01', '2023-06-01', 'NULL', 'ALLOCATED', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.267501', '2024-03-22 08:15:02.267501', '641de26c55c444bfaaaf8d26e6a3b3cc', 'TW017', 'KOMAK DAN BERNIE', 'Site Operations Coordinator', 'National', 'Male', '1982-01-05', '776989188', '782229005', '2022-12-26', 'Hoima', '', '2020-10-29', '2023-10-28', '2022-12-29', '2023-12-29', '1970-01-01', '1970-01-01', '1970-01-01', '1970-01-01', 'NULL', 'NULL', 'ALLOCATED', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.281028', '2024-03-22 08:15:02.281028', '64d5cdcd20de4df8abc3b55fd4ce4161', 'TW096', 'KYEYUNE EDWARD', ' Fuel Tank Driver ', '', '', '2023-06-01', '', '', '2023-06-01', '', '', '2023-06-01', '2023-06-01', '2023-06-01', '2000-12-30', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.266420', '2024-03-22 08:15:02.266420', '66ddff523dba485b881702fae9d3ff11', 'TW014', 'JUSTINE NYAKATO ', 'Admin Clerk', 'National', 'Female', '1994-12-10', '773749679', '782951393', '2022-12-26', 'Total-DSB', '', '2023-06-01', '2023-06-01', '2022-12-08', '2023-12-08', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'ALLOCATED', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.272919', '2024-03-22 08:15:02.272919', '68032401efc9470b9faa98a21a8a7c2c', 'TW005', 'HASSAN OMARI LEMMY ', 'Banksman', 'National', 'Male', '1979-12-14', '771833598', '761894291', '2022-12-26', 'ZPEB', '', '2023-06-01', '2023-06-01', '2022-05-18', '2023-05-18', '2022-05-18', '2024-05-18', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.276031', '2024-03-22 08:15:02.276031', '6938b4e8e7294d6cb2570bb58b8cf03c', 'TW062', 'JAMES ABIGABA', 'Banksman', 'National', 'Male', '1979-05-01', '774659929', '787175966', '2023-06-02', 'CNOOC', '', '2023-06-01', '2023-06-01', '2023-02-02', '2024-02-02', '2022-01-31', '2025-01-31', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.277035', '2024-03-22 08:15:02.277035', '6c02b411bff84ebd8a93fedb1131b1bc', 'TW063', 'FRED KIZZA', 'Banksman', 'National', 'Male', '1985-01-01', '771818345', '775899784', '2023-06-02', 'CNOOC', '', '2023-06-01', '2023-06-01', '2023-02-02', '2024-02-02', '2023-01-31', '2025-01-31', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.275035', '2024-03-22 08:15:02.275035', '6c6984aa1399484285ac75262370893c', 'TW019', 'OMONY SSEBI', 'Banksman', 'National', 'Male', '1997-12-15', '779077262', '', '2023-03-01', 'Total-TGI', '', '2023-06-01', '2023-06-01', '2022-10-08', '2023-10-08', '2022-08-06', '2024-08-06', '2023-06-01', '2023-06-01', 'NULL', 'ALLOCATED', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.276031', '2024-03-22 08:15:02.276031', '6eb484f8e9434a9d8650d20ae00765cf', 'TW081', 'ASIIMWE BYARUHANGA', 'Banksman', 'National', 'Male', '1972-03-23', '788061862', '772668995', '2023-06-02', 'Total-DSB', '', '2023-06-01', '2023-06-01', '2022-10-25', '2023-10-25', '2021-10-21', '2023-10-21', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.267501', '2024-03-22 08:15:02.267501', '737b089f5965450ebf0b3bb16a6e3608', 'TW010', 'JACOB OMONDI', 'CPLO', 'Expatriate', 'Male', '1983-08-30', '779453432', '779453432', '2022-12-16', 'ZPEB', '', '2022-10-21', '2025-10-21', '2022-12-19', '2023-12-19', '1970-01-01', '1970-01-01', '1970-01-01', '1970-01-01', 'NULL', 'NULL', 'ALLOCATED', 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAMAAACahl6sAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAIGNIUk0AAG2YAABzjgAA+swAAIT6AAB5gQAA/RMAADBtAAASKQ0eJk4AAAMAUExURevr7Jydn5manJucnuPj5JiZm9vb3PT09MvLzMLCw5GSlPr6+qeoqdXV1tHR0rW1trW2uKusrbi4urO0tLq6vKiqq7e4uLW2tqGipLm6ury8vr6+vr+/wLu8vM7OztDQ0cjJytjY2dTU1aipqqqrrMXGxqanqKmqq6Wmp9LT062usKSlprS0ta2trra2t6ytrqWmqK2ur66vsK6ur7CwsbOztK+vsK+wsbKys7GxsqOkpqOkpZ6foampq6qqrJ2eoKenqaysraKjpZqbnbi4uaKjpKSlp5eYmqioqqurrKChory8vKGio6amqKCho7Gys7CxsrGysrKzs5+gop+gobS1tbq6u7e3uLCxsbKztLi4uJWWmJaXmba3t7i5ub29vZWXmZSWmLq6upOVl5SVl7m5up6foLq7u7u7vJqcnZOUlpeZm5aYmpKUlry8vZKTlpGTlZCRlJCRk6ytr9bX197e3q+vsb2+v8DAweDh4bOztebm5ujp6e/v756eoP///4CAgIGBgYKCgoODg4SEhIWFhYaGhoeHh4iIiImJiYqKiouLi4yMjI2NjY6Ojo+Pj5CQkJGRkZKSkpOTk5SUlJWVlZaWlpeXl5iYmJmZmZqampubm5ycnJ2dnZ6enp+fn6CgoKGhoaKioqOjo6SkpKWlpaampqenp6ioqKmpqaqqqqurq6ysrK2tra6urq+vr7CwsLGxsbKysrOzs7S0tLW1tba2tre3t7i4uLm5ubq6uru7u7y8vL29vb6+vr+/v8DAwMHBwcLCwsPDw8TExMXFxcbGxsfHx8jIyMnJycrKysvLy8zMzM3Nzc7Ozs/Pz9DQ0NHR0dLS0tPT09TU1NXV1dbW1tfX19jY2NnZ2dra2tvb29zc3N3d3d7e3t/f3+Dg4OHh4eLi4uPj4+Tk5OXl5ebm5ufn5+jo6Onp6erq6uvr6+zs7O3t7e7u7u/v7/Dw8PHx8fLy8vPz8/T09PX19fb29vf39/j4+Pn5+fr6+vv7+/z8/P39/f7+/v///zfARREAAAeqSURBVHja7N3xVxJZFMBxQAQVilzPSTslBxcDdwdtBQRBDQUFBYNMDTcoNLAMM7QD23JozvvX94cJZBhQZ+bdO2/26F/Q59wv8K48JwP5n/wY7iH3kHvIPYT6D89bLBazfiF8Y+T09PT09MOHzc3Nd+8yeoTwb99+/PjkSbfj8eN83qYPSCOTOTs7O3veEP69UkcegEIdMpPJCI6zz5/f9p9HPp9//97KMsTwLZO5o2Nh4RmrkHrpmxzHwsICzyLEWSq1IXd1TE6aWYNYSqVSqSRzHpOTDsdDliC2ksBQ4HA4zOxA6iURRJ7DccizAbE9fVpyNXhlXTkcjsNDHxMQKyGEWBV35Tg89Pl8rKTVUtHVoc/n89mYgPBK3686Dt8EIcQwMzOjKUTF+1XHMbG0tLT095s3y8vL77WCqHq/Ehy+Lsdybm9aC4irRKGrLkcut7cXiUTQIS1588jfPo/cXiQSibxGhtTpdyU4kCElyq/zXMdx9AwT0qI+j1zbEQwiQmyUX+fXXR0Fg0EXGsQK1dXRUTAYDIbRIJBdBYNhNIgFsqtgOBx2IkFguwqHQyEcSAu2q3AICwLcVSjEh1oYEPCuQgbix4A4obsK+QmPAwHtKhTy+3+gvEacsF2F/H5/wIAIAevK7/cHAhgQgPNuzzwCgcAiFgSoK3/bgQWhuUdJuwosYkGgu1pcnDdgQCju5wPmMY8CAeyqPY/5+To8BKErPAjY50fb8QIHAnIu6Z7HCxwI0Lmk24ECge8KB4LQ1YuNDYS3X4SuNjbGESAIXW2M40DAuxofH0c4ayF0hQNB6AoJAt8VDgShq/GdHQwIYFfteezMIkCgzrsiBwZkhPp+LulqFgXyB/X9XDoPFEgTviscCE99P+/+/PjlwIAQ6vu5dB4vX2JAALvaaTu8OBCoc0m7q5deHAjYuaQzD68fAwJ3Luk4vC4MyAh4V17vAwxIE7orr9fLY0AIdFde7xpBg8B09cuBCAHtyrvmxoLAdrXm/h0DUgfvas3tdvPQEBdCV2632+3eHgWFwL9ftR12+yYg5CfIfi7pyu3ettvtdkAI2B4lnYfdbndBQiD28wGO9XUwiAFmP5e8zu0CxGOFgrgQu1pf93hcUJA84HlX/DoXIDkoCNB+3r8rj8fjgYIA7ef9u4KGoHXl8XheAUKAzyXdXXlezcFBwM8lXV29moODoHY1BwfB7QoSgtoVIARuj+rXFTAEtCvxPJKPoCBm1K6SyZ9gx3jorrodc0kObh/B7CrJzQJCELviZA1EJsQAtp9LuwKFENA9SjwPbhoSYgbbzwVGl0PeQGT/gg5sP+/tipuFhRCkruQORD5kFPa8qzAsJb/Ehj3v/uqKM8NDSANmPxd11cD5fgS8K5Q/3yOE2L7l9vYWALpKPuI4jsP7M3DhB+JcovyBbmoeJ0K/K45oASG0u0py09pAND7v0oM0qe7nSU4zCKG7R2kJofw5yGsFcVLcz1UOROXztah2pSWE6vkqatUO0qS2n3McFyXaQYiP2h6l0qH6qYCU9nMuGmUBon6P4qLRh9pCrJS6UjsQ9Q+cXKKwR3HRaPQfrSGESlfRFaI5pK7284OKg8aDiyl0tcIEpKV4j6LooPIoaYParlZ4NiBE2X5+7fiXMAIh6rpaIcxAeDVdUXHQem78A/n7ecfRYAlCphXsURTnQfG/JJC/RwkO9iCy9yjBEWcNoqyrlTiTEPldxZmEKOgqHt9iDyL782MlHo9vsQeRtZ9fO5iDyNyjOg72IIq62tqaYg0ib4+6drAJkd3VFJMQBV1NTe2yC5HTFZOQO+9R3fPYZQ4iu6spwcEq5PY9StTV7m6WLYjtVFlXu9nsCDMQi9+ruKtsNptOp9N/WTWHmJ/I2s8l88im0+n0/v7+Qc6mHcSiZI8a4Dg4OFhdVXGnRjHks9I9StpVx7G6uvrpU8yJCHmudD+/cR6CIxaLxR5gQJT/3ufOjljMaDQ6ASHN18q+P5fRVcdhNBqNQ9tWAEhL+ffnCuZhNBqNQ0NDQ0N+qpCmyu85lTu+fEkkEnYLDcio6u/PFXbVcSQSiYTJ5FQFeU7le0518xAcJpPJNKMMUqL0/Tk1h2l4eHh4RB6kPkHlHvKA827HsS/bMXx+nvqtdUcItfvt9OcxfH6eSqVSqa8/boU06d2/AnR8LRaLN0Pq9O6339aVckfqa7FYLB7fBKF0DxlhHsXj42PjQEgIqqspCEehUBgA8dG5347S1fFxoVAo2PpCWrrqqlAoFE5OWn0gBr11VTg5Oan0gdC63w45j1Svo2KVQujdQ8bq6qRSqVQkkAlq95DxuqpUKmUJhNb9dsyuKpVyeVQC0WNX5XK52gOx6LKrcrlabYghE5Tut+N2VS5Xq3YxhNo9ZNyuqtXqhQhipXS/HburavVCDKkzvUcN7qp60QPZ1GtXFxc1EYTV/fwaMmgetV4Iu/v5jV3VarW6CML2fj64q1qt9mc3hPX9fPA8ape9ED3sUX3mcXl5KYboY4/q5xgTQdjfz/t31QvRb1djYz0QvXYlhbC/n/ftqgeinz1KMo8eiG72KKlDBNHPHtXbVT+ILrsaG7vqgei0q6ur770QfXZ19V2A/DcAHpmC7NcZ4/wAAAAASUVORK5CYII=', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.280053', '2024-03-22 08:15:02.280053', '74fd2a1c7a224969b60d7c593c7fb4a0', 'TW056', 'RAYMOND KASUA', 'Site Lifting Specialist', 'National', 'Male', '1986-12-05', '783428358', '', '2023-01-24', 'ZPEB', '', '2023-06-01', '2023-06-01', '2022-09-20', '2023-09-20', '2023-01-06', '2025-01-06', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.272919', '2024-03-22 08:15:02.272919', '7886599a38824c7493b9f3663c624eb2', 'TW021', 'GEOFREY OJOK', 'Banksman', 'National', 'Male', '1997-06-26', '781783998', '773937328', '2023-03-01', 'ZPEB', '', '2023-06-01', '2023-06-01', '2022-10-25', '2023-10-25', '2022-08-06', '2024-08-06', '2023-06-01', '2023-06-01', 'NULL', 'ALLOCATED', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.271420', '2024-03-22 08:15:02.271420', '7f424640424f4cfda9af61fda97a0034', 'TW092', 'JIMMY TABU', 'Materiel Handler', 'National', 'Male', '1987-10-18', '780746882', '', '2023-03-01', 'CNOOC', '', '2023-06-01', '2023-06-01', '2023-06-01', '2000-12-30', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.275035', '2024-03-22 08:15:02.275035', '845c9e8dcd12427892ba8551f7788256', 'TW030', 'DAVID KAKEETO', 'Banksman', 'National', 'Male', '1981-02-12', '785168985', '', '2023-01-01', 'CNOOC', '', '2023-06-01', '2023-06-01', '2023-02-27', '2024-02-27', '2022-02-19', '2024-02-19', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.274023', '2024-03-22 08:15:02.274023', '847cae41d16b48ddb3f024348fac0dba', 'TW037', 'DENISH ORYEMA ', 'Banksman', 'National', 'Male', '1986-01-11', '779397995', '771224087', '2023-01-15', 'Total-DSB', '', '2023-06-01', '2023-06-01', '2022-10-25', '2023-10-25', '2021-10-17', '2023-10-17', '2023-06-01', '2023-06-01', 'NULL', 'ALLOCATED', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.281028', '2024-03-22 08:15:02.281028', '89ef25176e53432e83a713fcf083b6f6', '', 'ABDUL R DEWO', 'Site supervisor', 'National', 'Male', '2023-06-01', '772411666', '752005230', '2023-06-01', '', '', '2023-06-01', '2023-06-01', '2023-06-01', '2000-12-30', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.280053', '2024-03-22 08:15:02.280053', '8e108d9d251c4b5b834f8af7fa4b4ccb', 'TW027', 'GEOFFREY TUMUSIIME ', 'Site Lifting Specialist', 'National', 'Male', '1984-11-14', '774456865', '', '2023-01-01', 'Total-TGI', '', '2023-06-01', '2023-06-01', '2022-11-09', '2023-11-09', '2022-06-13', '2024-06-13', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.271420', '2024-03-22 08:15:02.271420', '9196958532e445f5a4feefd4564717ce', 'TW090', 'GODFREY LUTALO', 'Materiel Handler', 'National', 'Male', '1986-10-09', '777886905', '777234910', '2023-03-01', 'CNOOC', '', '2023-06-01', '2023-06-01', '2023-06-01', '2000-12-30', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.278024', '2024-03-22 08:15:02.278024', '92411c10cab44b9f9cd407516ce16499', 'TW034', 'GERALD ANKWASA', 'Banksman', 'National', 'Male', '1998-07-07', '760271001', '', '2023-01-01', 'SLB', '', '2023-06-01', '2023-06-01', '2022-10-25', '2023-10-25', '2022-08-06', '2024-08-06', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.277035', '2024-03-22 08:15:02.277035', '9b2202cb5a604fb8a7579fb5df6b2f23', 'TW072', 'DENIS TWESIGYE SANDE', 'Banksman', 'National', 'Male', '1980-02-10', '784066055', '755195697', '2023-02-15', 'KARMOD BETA', '', '2023-06-01', '2023-06-01', '2022-11-24', '2023-11-24', '2023-01-13', '2025-01-13', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.267501', '2024-03-22 08:15:02.267501', '9bd813fb84b540dea9a2fc83251b1c68', 'TW028', 'STEPHEN OCHIENG', 'Crane Operator', 'National', 'Male', '1977-02-02', '782385295', '', '2023-01-02', 'Total-DSB', '', '2022-08-19', '2025-08-18', '2023-03-22', '2024-03-21', '2022-03-15', '2024-03-15', '2023-06-01', '2023-06-01', 'NULL', 'ALLOCATED', 'ALLOCATED', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.268531', '2024-03-22 08:15:02.268531', '9e65a5c6993c44dd8dccca9c4ee19a7a', 'TW047', 'RICHARD SSEMWANGA', 'Forklift & Telehandler Operator', 'National', 'Male', '1981-02-20', '774698740', '776345813', '2023-01-01', 'CNOOC', '', '2021-03-25', '2024-03-25', '2023-04-03', '2024-04-02', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.269405', '2024-03-22 08:15:02.269405', '9f8a061981e8479a973df634938d5ceb', 'TW094', 'MATHEW NDIKUBWINDANA', 'Heavy Duty Driver', 'National', 'Male', '1954-01-01', '779802359', '', '2023-05-16', 'Total-DSB', '', '2021-11-03', '2024-11-02', '2023-01-12', '2024-01-12', '2023-06-01', '2023-06-01', '2023-04-20', '2023-05-04', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.279033', '2024-03-22 08:15:02.279033', 'a344da21b19549fdacaae2a66f8cbd89', 'TW059', 'PETER MUSIKO', 'Electrician', 'National', 'Male', '1973-03-12', '774189644', '', '2023-01-01', 'BULIISA', '', '2023-06-01', '2023-06-01', '2023-06-01', '2000-12-30', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.275035', '2024-03-22 08:15:02.275035', 'a730bf8297d7470b975a471fe72b5638', 'TW031', 'JULIUS TAYEBWA', 'Banksman', 'National', 'Male', '1985-07-31', '784541805', '782429086', '2023-01-01', 'CNOOC', '', '2023-06-01', '2023-06-01', '2023-03-02', '2024-03-01', '2022-02-19', '2024-02-19', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.278024', '2024-03-22 08:15:02.278024', 'a8dedbed868544619d308f6196217ce7', 'TW074', 'ALEX MUGISHA', 'Banksman', 'National', 'Male', '1988-12-14', '786660416', '761182506', '2023-02-15', 'Total-DSB', '', '2023-06-01', '2023-06-01', '2023-02-02', '2024-02-02', '2023-01-21', '2025-01-21', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.279033', '2024-03-22 08:15:02.279033', 'ab419c0d6bed4cc0bea7f9df3fd283ae', 'TW049', 'MOSES BIRUNGI ELVIS', 'Banksman', 'National', 'Male', '1981-03-05', '776097659', '', '2023-01-01', 'Total-TGI', '', '2023-06-01', '2023-06-01', '2023-03-21', '2024-03-20', '2022-03-15', '2024-03-15', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.274023', '2024-03-22 08:15:02.274023', 'ac9ffbdf44894147b8e36943f84903b3', 'TW006', 'TOM PETER KAKOOZA ', 'Banksman', 'National', 'Male', '1972-03-23', '774586612', '782874135', '2022-01-27', 'Total-DSB', '', '2023-06-01', '2023-06-01', '2022-05-18', '2023-05-18', '2022-05-18', '2024-05-18', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.269405', '2024-03-22 08:15:02.269405', 'b196059db96f4eadb202596e34cb0d4b', 'TW058', 'MUHAMUD SSEKABEMBE KIGULI', 'Heavy Duty Driver', 'National', 'Male', '1995-05-10', '772168094', '774519948', '2023-01-15', 'SLB', '', '2022-01-27', '2027-01-26', '2023-01-14', '2024-01-14', '2023-06-01', '2023-06-01', '2023-02-01', '2024-02-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.269405', '2024-03-22 08:15:02.269405', 'b21c951153ac4e61a9e0f48082fce05e', 'TW079', 'KIKOOBA ANDREW', 'Heavy Duty Driver', 'National', 'Male', '1980-01-01', '761798104', '781457662', '2023-01-01', 'Total-DSB', '', '2022-08-30', '2027-08-29', '2023-02-02', '2024-02-02', '2023-06-01', '2023-06-01', '2023-04-01', '2024-04-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.267501', '2024-03-22 08:15:02.267501', 'c0a46fb80fe8470c81a9c5627f4c57fc', 'TW066', 'SAMUEL KOMOLLO ', 'Crane Operator', 'National', 'Male', '1978-12-12', '783122887', '772398734', '2023-05-02', 'ZPEB', '', '2022-02-21', '2025-02-20', '2023-01-19', '2024-01-19', '2022-12-22', '2024-12-22', '2023-06-01', '2023-06-01', 'NULL', 'ALLOCATED', 'ALLOCATED', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.268531', '2024-03-22 08:15:02.268531', 'c2ddcea255bd42b093d74fb77a75e61f', 'TW053', 'MUSA OBORE ', 'Hiab Operator', 'National', 'Male', '1977-10-15', '777090041', '772404807', '2023-01-18', 'KARMOD BETA', '', '2022-10-11', '2024-10-11', '2022-12-24', '2023-12-24', '2023-06-01', '2023-06-01', '2022-10-01', '2023-10-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.268531', '2024-03-22 08:15:02.268531', 'c8cfd4f1ecb84e8594443f4fd2ad4bd2', 'TW065', 'UNUSU MUBIRU ', 'Forklift & Telehandler Operator', 'National', 'Male', '1988-05-25', '779909626', '754387875', '2023-05-02', 'Total-TGI', '', '2022-12-01', '2025-12-01', '2022-12-25', '2023-12-25', '2023-01-16', '2025-01-16', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'ALLOCATED', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.266420', '2024-03-22 08:15:02.266420', 'c9dfd29d0e5f45879016960041e33909', 'TW060', 'SAMAHA RAMADHAN', 'Admin Clerk', 'National', 'Female', '1986-02-24', '775819446', '772608814', '2023-02-04', 'Total-DSB', '', '2023-06-01', '2023-06-01', '2023-01-24', '2024-01-24', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.268531', '2024-03-22 08:15:02.268531', 'd4aa95c1d00240b9a819c89a56d1d35c', 'TW013', 'PROSCOVIA KUSIIMA ', 'H3SE Superintendent', 'National', 'Female', '1986-01-14', '773679439', '781444842', '2023-01-01', 'Total-DSB', '', '2023-06-01', '2023-06-01', '2022-12-08', '2023-12-08', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.278024', '2024-03-22 08:15:02.278024', 'd93bfa07c6734a44a8a97d66bc82eea9', 'TW075', 'ASUMAN KAKOOZA', 'Banksman', 'National', 'Male', '1988-03-23', '700655433', '709697665', '2023-02-17', 'Total-TGI', '', '2023-06-01', '2023-06-01', '2023-02-02', '2024-02-02', '2023-01-31', '2025-01-31', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.269405', '2024-03-22 08:15:02.269405', 'dee3290cc5bc41749e635ba62d71c5de', 'TW004', 'RAPHAEL SSEBULIBA ', 'Light Duty Driver', 'National', 'Male', '1976-11-20', '772157527', '773233441', '2022-12-26', 'Total-DSB', '', '2021-11-27', '2024-11-26', '2022-12-22', '2023-12-22', '2023-06-01', '2023-06-01', '2022-12-01', '2023-12-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.267501', '2024-03-22 08:15:02.267501', 'dfd758c75aaf423d921f7d753ecbcb27', 'TW038', 'JOHNSON KALYANGO', 'Crane Operator', 'National', 'Male', '1980-02-17', '785248424', '784131799', '2023-01-01', 'Total-TGI', '', '2021-01-27', '2024-01-26', '2023-05-26', '2024-05-25', '2022-12-10', '2024-12-10', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'ALLOCATED', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.279033', '2024-03-22 08:15:02.279033', 'e1d9c31a1e1b455d8fcaa272242ae052', 'TW050', 'CHRIS BYARUHANGA', 'Banksman', 'National', 'Male', '1979-07-11', '779738720', '', '2023-01-01', 'CNOOC', '', '2023-06-01', '2023-06-01', '2023-05-18', '2024-05-17', '2022-03-15', '2024-03-15', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.278024', '2024-03-22 08:15:02.278024', 'e285f4b5359f4088a9c2e1872e9ed2bd', 'TW036', 'BROLINE MAKUMBI', 'Banksman', 'National', 'Male', '1992-07-07', '789125076', '', '2023-01-01', 'SLB', '', '2023-06-01', '2023-06-01', '2022-10-25', '2023-10-25', '2021-10-17', '2023-10-17', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.281028', '2024-03-22 08:15:02.281028', 'e45ee00b1a9b4ca0947d71b04d1d3277', 'TW076', 'LANGTON BYARUHANGA', 'Forklift & Telehandler Operator', 'National', 'Male', '1984-10-10', '774810134', '', '2023-01-01', 'CNOOC', '', '2022-08-17', '2025-08-16', '2023-06-01', '2000-12-30', '2022-10-25', '2024-10-25', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.281028', '2024-03-22 08:35:50.366889', 'ed2a2aa3429f4e818122c2fdb5b1345d', 'TW095', 'KWAGALA EDDIE EDWARD', 'Reach Stacker Operator', NULL, NULL, '2023-06-01', NULL, NULL, '2023-06-01', NULL, NULL, '2023-06-01', '2023-06-01', '2023-06-01', '2000-12-30', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.270407', '2024-03-22 08:15:02.270407', 'edac33d087f04ac4867c8dcb6102f9d6', 'TW023', 'SADDAM SEMBAJWE ', 'Light Duty Driver', 'National', 'Male', '1972-07-08', '772780247', '700558112', '2023-01-14', 'Total-DSB', '', '2020-12-30', '2023-12-29', '2023-01-13', '2024-01-13', '2023-06-01', '2023-06-01', '2023-03-08', '2024-03-07', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.271420', '2024-03-22 08:15:02.271420', 'ef11c0bf2cb94157a1eb81af0e8b1ff7', 'TW091', 'GEOFREY AKENA ', 'Materiel Handler', 'National', 'Male', '1992-04-04', '762738092', '', '2023-03-01', 'CNOOC', '', '2023-06-01', '2023-06-01', '2023-06-01', '2000-12-30', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.272919', '2024-03-22 08:15:02.272919', 'f23403e3876747379a38f8078758c00a', 'TW085', 'HENRY SSENYONDO ', 'Materiel Handler', 'National', 'Male', '1983-01-15', '754317888', '756439437', '2023-03-01', 'CNOOC', '', '2023-06-01', '2023-06-01', '2023-03-17', '2024-03-16', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.279033', '2024-03-22 08:15:02.279033', 'f33fccd39b7d4e26a47d6c29eb7f95c9', 'TW029', 'DAN KASIGAZI TUMUTEGYEREZE', 'Banksman', 'National', 'Male', '1980-01-01', '779151399', '', '2023-01-01', 'CNOOC', '', '2023-06-01', '2023-06-01', '2023-03-21', '2024-03-20', '2021-10-21', '2023-10-21', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.268531', '2024-03-22 08:15:02.268531', 'f47fd977cf21493eb209ac5183f9a6f2', 'TW052', 'CHARLES GAHWERA', 'Heavy Duty Driver', 'National', 'Male', '1956-01-20', '774640970', '777696091', '2023-01-24', 'KARMOD BETA', '', '2023-06-07', '2028-06-06', '2022-12-30', '2023-12-30', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.280053', '2024-03-22 08:15:02.280053', 'f908bd6e914f4ec6bf43abfaca9d9c42', 'TW046', 'JOSEPH KIGGUNDU ', 'Transport Coordinator', 'National', 'Male', '1974-10-10', '782157923', '772398734', '2023-01-01', 'BULIISAC', '', '2022-04-06', '2025-04-05', '2023-02-02', '2024-02-02', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.272407', '2024-03-22 08:15:02.272407', 'f996be5a66d34fae81682a7ff4273d2d', 'TW088', 'SAMUEL ODAKA ', 'Materiel Handler', 'National', 'Male', '1968-12-12', '753111148', '', '2023-03-01', 'SLB', '', '2023-06-01', '2023-06-01', '2023-03-16', '2024-03-15', '2023-03-12', '2025-03-12', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.270407', '2024-03-22 08:15:02.270407', 'fb58c091dd64431c8eac7d7eac5263fd', 'TW002', 'MUHAMMED KAMYA ', 'Light Duty Driver', 'National', 'Male', '1983-02-13', '789811911', '704280887', '2022-12-26', 'Total-TGI', '', '2023-01-07', '2026-01-06', '2022-12-22', '2023-12-22', '2023-06-01', '2023-06-01', '2022-12-01', '2023-12-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.268531', '2024-03-22 08:15:02.268531', 'fc4b9e38815349df8a1de226e248e991', 'TW040', 'JIMMY MUHEREZA', 'Forklift & Telehandler Operator', 'National', 'Male', '1983-04-22', '785959244', '759533687', '2023-01-01', 'CNOOC', '', '2021-09-03', '2024-09-03', '2023-06-01', '2000-12-30', '2022-06-02', '2024-06-02', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'ALLOCATED', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.278024', '2024-03-22 08:15:02.278024', 'fc9bff6b71c241f4ae1391d9b208f552', 'TW012', 'SWALEH OKULE', 'Banksman', 'National', 'Male', '1976-10-23', '782967327', '761528019', '2022-12-27', 'CNOOC', '', '2023-06-01', '2023-06-01', '2022-12-19', '2023-12-19', '2023-01-31', '2025-01-31', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.276031', '2024-03-22 08:15:02.276031', 'fd6e1542515e4e89a81999b58504be17', 'TW015', 'DERICK TUKAMWESIGA ', 'Banksman', 'National', 'Male', '2001-02-28', '741048545', '755866391', '2022-12-28', 'KARMOD BETA', '', '2023-06-01', '2023-06-01', '2022-10-08', '2023-10-08', '2022-08-06', '2024-08-06', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.269405', '2024-03-22 08:15:02.269405', 'fd8826cbf4044e16a82b5eb5174df972', 'TW042', 'STEVEN KIGONGO ', 'Heavy Duty Driver', 'National', 'Male', '1964-11-30', '774772003', '772190056', '2023-01-01', 'Total-TGI', '', '2021-03-10', '2024-03-10', '2023-06-01', '2024-05-31', '2023-06-01', '2023-06-01', '2022-10-01', '2023-10-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL),
('2024-03-22 08:15:02.276031', '2024-03-22 08:15:02.276031', 'fe315711a0ad4b398807a67f054b1400', 'TW007', 'ROBERT KUGONZA', 'Banksman', 'National', 'Male', '1980-12-16', '785449779', '777063884', '2022-12-26', 'CNOOC', '', '2023-06-01', '2023-06-01', '2023-06-02', '2024-06-01', '2022-03-15', '2024-03-15', '2023-06-01', '2023-06-01', 'NULL', 'NULL', 'NULL', 'NULL', '53793f4b57f74bf3ba363001fb2c7062', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `aix_employeeoftheweekmodel`
--

CREATE TABLE `aix_employeeoftheweekmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `week_number` int(11) NOT NULL,
  `year` int(11) NOT NULL,
  `count` int(11) NOT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_employeepayrollbenefitmodel`
--

CREATE TABLE `aix_employeepayrollbenefitmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `polarity` int(11) DEFAULT NULL,
  `is_taxed` int(11) NOT NULL,
  `amount` longtext NOT NULL,
  `benefit_type_id` char(32) NOT NULL,
  `employee_payroll_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_employeepayrollmodel`
--

CREATE TABLE `aix_employeepayrollmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT NULL,
  `gross_pay` double NOT NULL,
  `net_pay` double NOT NULL,
  `paid` tinyint(1) NOT NULL,
  `done_by` int(11) NOT NULL,
  `currency_id` char(32) NOT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_employeetransactionmodel`
--

CREATE TABLE `aix_employeetransactionmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `account_name` varchar(255) NOT NULL,
  `account_number` varchar(255) DEFAULT NULL,
  `account_code` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `preferred` int(11) NOT NULL,
  `description` longtext DEFAULT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `payment_mode_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_entitymanagementmodel`
--

CREATE TABLE `aix_entitymanagementmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `permission_level` varchar(10) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_entitymanagementmodel`
--

INSERT INTO `aix_entitymanagementmodel` (`created`, `updated`, `uuid`, `permission_level`, `entity_id`, `user_id`) VALUES
('2024-03-22 07:52:36.897169', '2024-03-22 07:52:36.897169', '104de248e065406788578a889efe4676', 'write', '1980d2af5ea14ad5b1e7712771f60517', 2),
('2024-02-24 02:40:16.504368', '2024-02-24 02:40:16.504368', '109cc05a40404a3b87624ebfc8970a6f', 'write', '1980d2af5ea14ad5b1e7712771f60517', 3),
('2024-03-18 12:26:47.347472', '2024-03-18 12:26:47.347472', '13c648b654c74f8cb5bae8f642e52aee', 'write', '1980d2af5ea14ad5b1e7712771f60517', 6),
('2024-03-18 12:27:02.090360', '2024-03-18 12:27:02.090360', '5a4633b0cfb84ac7be253ae732440e87', 'write', '1980d2af5ea14ad5b1e7712771f60517', 5),
('2024-03-10 01:38:42.201414', '2024-03-10 01:38:42.202409', 'aba5cfbd675e414bacb342a0f353ceb2', 'write', '1980d2af5ea14ad5b1e7712771f60517', 4),
('2025-03-31 06:12:05.491839', '2025-03-31 06:12:05.491839', 'b809460ed8494d2c9edd46987b94d57e', 'read', '94a77b664b5d4efab801ba8560d83fc8', 1),
('2024-08-28 08:29:57.650416', '2024-08-28 08:29:57.650416', 'd283079e1fc14aa19c7f7130ce218557', 'read', '94a77b664b5d4efab801ba8560d83fc8', 2),
('2024-03-18 12:27:14.197296', '2024-03-18 12:27:14.197296', 'f782bfef96a347dc825c2ee1d239e2f9', 'write', '1980d2af5ea14ad5b1e7712771f60517', 7);

-- --------------------------------------------------------

--
-- Table structure for table `aix_entitymodel`
--

CREATE TABLE `aix_entitymodel` (
  `slug` varchar(50) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `address_1` varchar(70) NOT NULL,
  `address_2` varchar(70) DEFAULT NULL,
  `city` varchar(70) DEFAULT NULL,
  `state` varchar(70) DEFAULT NULL,
  `zip_code` varchar(20) DEFAULT NULL,
  `country` varchar(70) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `website` varchar(200) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `name` varchar(150) DEFAULT NULL,
  `hidden` tinyint(1) NOT NULL,
  `fy_start_month` int(11) NOT NULL,
  `picture` longtext DEFAULT NULL,
  `admin_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_entitymodel`
--

INSERT INTO `aix_entitymodel` (`slug`, `created`, `updated`, `address_1`, `address_2`, `city`, `state`, `zip_code`, `country`, `email`, `website`, `phone`, `uuid`, `name`, `hidden`, `fy_start_month`, `picture`, `admin_id`) VALUES
('total-uganda-z4bevxpj', '2024-02-24 02:37:03.317638', '2024-02-25 03:10:12.123932', 'Plot 1144 Jinja Road', 'P.O.Box 1144 Kampala, Uganda', 'Kampala', 'Kampala', '256', 'Uganda', 'info-ug@dna.com', 'http://dna.com', '+256', '1980d2af5ea14ad5b1e7712771f60517', 'DNA Uganda', 0, 1, NULL, 2),
('3ways-prh482nd', '2024-08-28 08:29:25.514372', '2024-08-28 08:29:25.568257', 'P.O.Box 125 Kla', 'Namuwongo', 'Kampala', 'Kampala', '+256', 'Uganda', 'teneten@3ways.mando', 'http://3ways.mando', '+256 000 000 000', '94a77b664b5d4efab801ba8560d83fc8', 'Threeways', 0, 1, NULL, 2);

-- --------------------------------------------------------

--
-- Table structure for table `aix_entityunitmodel`
--

CREATE TABLE `aix_entityunitmodel` (
  `name` varchar(150) DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `hidden` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `parent_id` char(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_entityunitmodel`
--

INSERT INTO `aix_entityunitmodel` (`name`, `created`, `updated`, `uuid`, `slug`, `active`, `hidden`, `entity_id`, `parent_id`) VALUES
('Main Office', '2024-02-25 13:15:49.490072', '2024-02-25 13:15:49.493075', '06c455e12a7f4d019f2bd779aee9a655', 'main-office-8gks4', 1, 0, '1980d2af5ea14ad5b1e7712771f60517', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `aix_equipmentassignmentmodel`
--

CREATE TABLE `aix_equipmentassignmentmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `address_1` varchar(70) NOT NULL,
  `address_2` varchar(70) DEFAULT NULL,
  `city` varchar(70) DEFAULT NULL,
  `state` varchar(70) DEFAULT NULL,
  `zip_code` varchar(20) DEFAULT NULL,
  `country` varchar(70) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `website` varchar(200) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `date` date DEFAULT NULL,
  `is_supervisor` tinyint(1) NOT NULL,
  `is_assistant` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `equipment_id` char(32) NOT NULL,
  `operator_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_equipmentaxlemodel`
--

CREATE TABLE `aix_equipmentaxlemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_equipmentfetmodel`
--

CREATE TABLE `aix_equipmentfetmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `markdown_notes` longtext DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(50) NOT NULL,
  `fet_date` date DEFAULT NULL,
  `fet_status` varchar(15) DEFAULT NULL,
  `draft_date` date DEFAULT NULL,
  `in_review_date` date DEFAULT NULL,
  `approved_date` date DEFAULT NULL,
  `void_date` date DEFAULT NULL,
  `fulfillment_date` date DEFAULT NULL,
  `canceled_date` date DEFAULT NULL,
  `entity_id` char(32) NOT NULL,
  `location_id` char(32) NOT NULL,
  `work_order_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_equipmentfetmodel`
--

INSERT INTO `aix_equipmentfetmodel` (`created`, `updated`, `markdown_notes`, `uuid`, `code`, `fet_date`, `fet_status`, `draft_date`, `in_review_date`, `approved_date`, `void_date`, `fulfillment_date`, `canceled_date`, `entity_id`, `location_id`, `work_order_id`) VALUES
('2025-08-04 11:42:02.222967', '2025-08-04 11:42:38.880754', NULL, '31f5c393f39e42a388ede5017eedb469', 'FET7UREYIPJ75', NULL, 'draft', NULL, NULL, NULL, NULL, NULL, NULL, '94a77b664b5d4efab801ba8560d83fc8', 'd5370a8957ed4f79a0bbf47e931b06d9', '72694865b2fc4437b21abd7c20caff19'),
('2025-07-31 09:45:50.055137', '2025-08-18 07:51:44.806510', NULL, '9fc83648fb2148459c0f49fc29f20d59', 'FETGV9EANH4PN', '2025-08-01', 'draft', NULL, NULL, NULL, NULL, NULL, NULL, '94a77b664b5d4efab801ba8560d83fc8', 'd5370a8957ed4f79a0bbf47e931b06d9', '72694865b2fc4437b21abd7c20caff19'),
('2025-08-04 12:22:25.650188', '2025-08-04 12:23:48.812012', NULL, 'c5b477ca8c2f4db69ba5612570f381e1', 'FET3OMA1TBYEM', NULL, 'draft', NULL, NULL, NULL, NULL, NULL, NULL, '94a77b664b5d4efab801ba8560d83fc8', 'd5370a8957ed4f79a0bbf47e931b06d9', '72694865b2fc4437b21abd7c20caff19');

-- --------------------------------------------------------

--
-- Table structure for table `aix_equipmentfuelmodel`
--

CREATE TABLE `aix_equipmentfuelmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(50) NOT NULL,
  `fuel_date` date DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `start_mileage` double DEFAULT NULL,
  `end_mileage` double DEFAULT NULL,
  `fuel_qty` double DEFAULT NULL,
  `fuel_price` double DEFAULT NULL,
  `fuel_cost` double DEFAULT NULL,
  `fuel_tank` double DEFAULT NULL,
  `kms_covered` double DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `EndLocation` char(32) DEFAULT NULL,
  `entity_id` char(32) NOT NULL,
  `equipment_id` char(32) NOT NULL,
  `fuel_reciept_id` char(32) DEFAULT NULL,
  `StartLocation` char(32) DEFAULT NULL,
  `work_order_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_equipmentfuelmodel`
--

INSERT INTO `aix_equipmentfuelmodel` (`created`, `updated`, `uuid`, `code`, `fuel_date`, `description`, `start_mileage`, `end_mileage`, `fuel_qty`, `fuel_price`, `fuel_cost`, `fuel_tank`, `kms_covered`, `status`, `EndLocation`, `entity_id`, `equipment_id`, `fuel_reciept_id`, `StartLocation`, `work_order_id`) VALUES
('2025-07-23 06:50:48.814907', '2025-07-24 12:07:33.195396', '5a7965cda3d549de90f5426bf161b095', 'FLFU4RBF3FN4', '2024-10-03', 'NA', 47893, 47933, 80, 4177, NULL, 65, 40, 'NEW', '42b82d8bb7b44e969f712b237990d96a', '94a77b664b5d4efab801ba8560d83fc8', '506e2a5b16f04e3b956063fbaa65b04e', NULL, '33eaad0f5e8940248adf7ce633019be8', '72694865b2fc4437b21abd7c20caff19'),
('2025-07-22 09:23:36.378871', '2025-07-22 11:56:46.617662', '810cf37ddc664d17a58d7f2de7ef9eb4', 'FLFHBYDDFOXV', '2024-10-01', 'Transport the Spreader Beam', 123809, 123845, 100, 4090, NULL, 125, 50, 'NEW', 'cceb53cedd2146eab161e6e6d7021d49', '94a77b664b5d4efab801ba8560d83fc8', '44e8d3f6b2ba4ff2a4f00fe4fdf58127', NULL, 'ac92dd81559745f59624539ca6fad402', '72694865b2fc4437b21abd7c20caff19');

-- --------------------------------------------------------

--
-- Table structure for table `aix_equipmenthandovermodel`
--

CREATE TABLE `aix_equipmenthandovermodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `address_1` varchar(70) NOT NULL,
  `address_2` varchar(70) DEFAULT NULL,
  `city` varchar(70) DEFAULT NULL,
  `state` varchar(70) DEFAULT NULL,
  `zip_code` varchar(20) DEFAULT NULL,
  `country` varchar(70) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `website` varchar(200) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `ho_date` date DEFAULT NULL,
  `ho_time` time(6) NOT NULL,
  `project` varchar(100) NOT NULL,
  `dho` longtext DEFAULT NULL,
  `condition` varchar(100) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `equipment_id` char(32) NOT NULL,
  `handover_by_id` char(32) NOT NULL,
  `location_id` char(32) NOT NULL,
  `received_by_id` char(32) NOT NULL,
  `approved_by_hr_id` char(32) DEFAULT NULL,
  `approved_by_ict_id` char(32) DEFAULT NULL,
  `approved_date_hr` date DEFAULT NULL,
  `approved_date_ict` date DEFAULT NULL,
  `return_date` date DEFAULT NULL,
  `purpose` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_equipmentjoinmodel`
--

CREATE TABLE `aix_equipmentjoinmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `address_1` varchar(70) NOT NULL,
  `address_2` varchar(70) DEFAULT NULL,
  `city` varchar(70) DEFAULT NULL,
  `state` varchar(70) DEFAULT NULL,
  `zip_code` varchar(20) DEFAULT NULL,
  `country` varchar(70) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `website` varchar(200) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `date` date DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `eq_primary_id` char(32) NOT NULL,
  `eq_secondary_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_equipmentmanufacturermodel`
--

CREATE TABLE `aix_equipmentmanufacturermodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_equipmentmanufacturermodel`
--

INSERT INTO `aix_equipmentmanufacturermodel` (`created`, `updated`, `uuid`, `code`, `name`, `description`, `entity_id`) VALUES
('2025-03-31 11:33:03.365792', '2025-03-31 11:33:03.366794', '051dc1d8d0ac44aa9b0513cbf08c9a61', 'LEN', 'LENOVO', 'LENOVO', '94a77b664b5d4efab801ba8560d83fc8'),
('2025-04-11 05:24:36.144240', '2025-04-11 05:24:36.145747', '34b82e356fe646a09f9fc089943eaef5', 'NKIA', 'NOKIA', 'Nokia Smart Phone', '94a77b664b5d4efab801ba8560d83fc8'),
('2025-04-11 05:58:59.994895', '2025-04-11 05:58:59.995883', '44f1ddd202ae46ec9a4e1ea2ed96bee7', 'MTN', 'MTN UGANDA', 'MTN UGANDA', '94a77b664b5d4efab801ba8560d83fc8'),
('2025-03-31 07:54:19.233791', '2025-03-31 07:54:19.237682', '501561d2d26d4ae3bed168b8388ef1af', 'HP', 'Hewlett Parckard', 'Hewlett Parckard', '94a77b664b5d4efab801ba8560d83fc8'),
('2025-04-03 09:28:21.617495', '2025-04-03 09:28:21.620012', 'a9b52f492231484f94500042350b5dad', 'ZKT', 'ZKTeco', 'ZKTeco Time and Attendance Machine', '94a77b664b5d4efab801ba8560d83fc8'),
('2025-03-31 07:56:22.585080', '2025-03-31 11:35:51.523336', 'fa431a12b04a431d8a87f2a6f14cae91', 'DELL', 'DELL', 'Dell', '94a77b664b5d4efab801ba8560d83fc8');

-- --------------------------------------------------------

--
-- Table structure for table `aix_equipmentmodel`
--

CREATE TABLE `aix_equipmentmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `address_1` varchar(70) NOT NULL,
  `address_2` varchar(70) DEFAULT NULL,
  `city` varchar(70) DEFAULT NULL,
  `state` varchar(70) DEFAULT NULL,
  `zip_code` varchar(20) DEFAULT NULL,
  `country` varchar(70) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `website` varchar(200) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `reg_no` varchar(255) DEFAULT NULL,
  `yom` int(11) DEFAULT NULL,
  `model` varchar(255) NOT NULL,
  `status` varchar(255) DEFAULT NULL,
  `details` longtext DEFAULT NULL,
  `active` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `eq_manufacturer_id` char(32) NOT NULL,
  `eq_type_id` char(32) NOT NULL,
  `serial` varchar(255) NOT NULL,
  `code` varchar(255) NOT NULL,
  `asset_id` char(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_equipmentmodel`
--

INSERT INTO `aix_equipmentmodel` (`created`, `updated`, `address_1`, `address_2`, `city`, `state`, `zip_code`, `country`, `email`, `website`, `phone`, `uuid`, `reg_no`, `yom`, `model`, `status`, `details`, `active`, `entity_id`, `eq_manufacturer_id`, `eq_type_id`, `serial`, `code`, `asset_id`) VALUES
('2025-04-11 06:38:52.138341', '2025-04-11 06:38:52.140045', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '44e8d3f6b2ba4ff2a4f00fe4fdf58127', '5CD33044WP', 2023, 'HP Probook 450 G10', NULL, '', 1, '94a77b664b5d4efab801ba8560d83fc8', '501561d2d26d4ae3bed168b8388ef1af', '253ab78f548041b7aa830f0c549b0bc6', '5CD33044WP', 'EQKSERTIGZCX', NULL),
('2025-04-11 05:58:13.943138', '2025-04-11 05:58:13.944139', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '4b11b6e55fe64304a0adedf383fe4335', '762583063', 2025, 'SIM CARD', NULL, 'MTN SIM CARD', 1, '94a77b664b5d4efab801ba8560d83fc8', '34b82e356fe646a09f9fc089943eaef5', '7987fab285b64b3f81ca867e0e5d7f51', '762583063', 'EQJEPML87V8D', NULL),
('2025-04-11 05:54:57.226792', '2025-04-11 05:55:23.750909', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '506e2a5b16f04e3b956063fbaa65b04e', '359979217337239', 2023, 'NOKIA C32', NULL, 'NOKIA C32 TA-1534 50MP CAM, HDD 64GB, MEM 4GB', 1, '94a77b664b5d4efab801ba8560d83fc8', '34b82e356fe646a09f9fc089943eaef5', '7987fab285b64b3f81ca867e0e5d7f51', '359979217337247', 'EQDFV8P1J148', NULL),
('2025-04-11 06:06:58.879366', '2025-04-11 06:06:58.880358', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '50830ce3b2734293b82c266a13623fda', '860945062498170', 2025, 'MIFI', NULL, 'MF935 LTE Ufi 4G 2.4Ghz 2000mAh RB', 1, '94a77b664b5d4efab801ba8560d83fc8', '44f1ddd202ae46ec9a4e1ea2ed96bee7', '79758f2194694323a62c54a8d76bb01e', '0394706340', 'EQV8Z6OQDK6R', NULL),
('2025-04-11 06:37:49.624473', '2025-04-11 06:37:49.626381', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '6fd0a166b96c4f10aaf836788eec0dc2', '5CD33044VX', 2023, 'HP Probook 450 G10', NULL, '', 1, '94a77b664b5d4efab801ba8560d83fc8', '501561d2d26d4ae3bed168b8388ef1af', '253ab78f548041b7aa830f0c549b0bc6', '5CD33044VX', 'EQEYR4KZJZHB', NULL),
('2025-04-11 05:59:54.030536', '2025-04-11 05:59:54.032061', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '7c85b63257434aafb07ce42328f38297', '762583062', 2025, 'SIM CARD', NULL, 'MTN SIM CARD', 1, '94a77b664b5d4efab801ba8560d83fc8', '44f1ddd202ae46ec9a4e1ea2ed96bee7', '9f6841f247f04c468c1b0765776cad7a', '762583062', 'EQ6UXU0G4Y6D', NULL),
('2025-04-11 06:04:41.686503', '2025-04-11 06:05:55.495821', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '83afb1eaaad441d5b2070d6b5546b1a4', '860945062553834', 2025, 'MIFI', NULL, 'MF935 LTE Ufi 4G 2.4Ghz 2000mAh RB', 1, '94a77b664b5d4efab801ba8560d83fc8', '44f1ddd202ae46ec9a4e1ea2ed96bee7', '79758f2194694323a62c54a8d76bb01e', '0394706342', 'EQXQWEN38S82', NULL),
('2025-04-11 06:39:21.823275', '2025-07-29 13:07:42.692017', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '8e1b463e7bac4d1592321e9307eab99a', '5CD33044TW', 2023, 'HP Probook 450 G10', NULL, 'NA', 1, '94a77b664b5d4efab801ba8560d83fc8', '501561d2d26d4ae3bed168b8388ef1af', '253ab78f548041b7aa830f0c549b0bc6', '5CD33044TW', 'EQKWH5377TQ3', '5ae669f7932b11eea0b90a0027000102'),
('2025-04-11 06:38:25.182413', '2025-04-11 06:38:25.184128', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '9b9e3c62f9294201a74b2a78dfe5b604', '5CD33044SX', 2023, 'HP Probook 450 G10', NULL, '', 1, '94a77b664b5d4efab801ba8560d83fc8', '501561d2d26d4ae3bed168b8388ef1af', '253ab78f548041b7aa830f0c549b0bc6', '5CD33044SX', 'EQ5IOO7DF339', NULL),
('2025-04-11 05:25:30.190005', '2025-04-11 05:42:16.413773', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '9cf96042fa7f4571b282af3eb7105195', '3599792173384419', 2023, 'NOKIA C32', NULL, 'NOKIA C32 TA-1534\r\n50MP CAM, HDD 64GB, MEM 4GB', 1, '94a77b664b5d4efab801ba8560d83fc8', '34b82e356fe646a09f9fc089943eaef5', '7987fab285b64b3f81ca867e0e5d7f51', '359979217338427', '', NULL),
('2025-07-31 09:36:11.895692', '2025-08-14 07:36:59.403479', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '9d567b728c2745d49603a94ffdca509d', 'UAS 482M', 2004, 'Truck', NULL, 'Trunck for Hire', 1, '94a77b664b5d4efab801ba8560d83fc8', 'fa431a12b04a431d8a87f2a6f14cae91', 'efc80a66b94f412684dcd71527a1bc9a', 'UAS482M', 'EQOY665VYQEU', '5ae58936932b11eea0b90a0027000102'),
('2025-03-31 08:13:06.333533', '2025-03-31 11:45:19.879292', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'a69093194e474800b01c2237c136e7ea', 'XMDJDK74HK', 2004, 'HP G10', NULL, 'HP Probook', 1, '94a77b664b5d4efab801ba8560d83fc8', '501561d2d26d4ae3bed168b8388ef1af', '3f6cac757d704906be4532a96b145800', 'XCD362HK9', '0', NULL),
('2025-04-11 06:02:42.588927', '2025-04-11 06:07:37.304716', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'a73bc37cfb0149e6b8732df72204bb21', '860945062544064', 2025, 'MIFI', NULL, 'MF935 LTE Ufi 4G 2.4Ghz 2000mAh RB', 1, '94a77b664b5d4efab801ba8560d83fc8', '44f1ddd202ae46ec9a4e1ea2ed96bee7', '9f6841f247f04c468c1b0765776cad7a', '0394706339', 'EQWHQIMDJ4HC', NULL),
('2025-07-31 09:30:23.351310', '2025-08-14 07:38:44.455045', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'a7d931a9c19e4f00abd95a27eca43f07', 'UAT 794P', 2000, 'Truck', NULL, 'For Tansport', 1, '94a77b664b5d4efab801ba8560d83fc8', 'fa431a12b04a431d8a87f2a6f14cae91', 'efc80a66b94f412684dcd71527a1bc9a', 'UAT794P', 'EQ587BP09BKN', '5ae67bae932b11eea0b90a0027000102'),
('2025-04-11 05:53:04.883191', '2025-04-11 05:55:36.023956', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'b612169a057b4f0e8b94def32e78849f', '359979217332990', 2023, 'NOKIA C32', NULL, 'NOKIA C32 TA-1534 50MP CAM, HDD 64GB, MEM 4GB', 1, '94a77b664b5d4efab801ba8560d83fc8', '34b82e356fe646a09f9fc089943eaef5', '7987fab285b64b3f81ca867e0e5d7f51', '359979217333006', 'EQ6QZ75K5O9D', NULL),
('2025-04-11 06:36:44.767557', '2025-04-11 06:36:44.768557', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'c970b05a3dde4f66a85baa17e2b23fa0', '5CD33044S5', 2023, 'HP Probook 450 G10', NULL, 'i5 13Gn, 8GB Ram, 512GB HDD', 1, '94a77b664b5d4efab801ba8560d83fc8', '501561d2d26d4ae3bed168b8388ef1af', '253ab78f548041b7aa830f0c549b0bc6', '5CD33044S5', 'EQV0NK7694CQ', NULL),
('2025-04-11 06:37:15.735833', '2025-04-11 06:37:15.737919', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'd90186157dec46aeb64551810289c773', '5CD33044L4', 2023, 'HP Probook 450 G10', NULL, '', 1, '94a77b664b5d4efab801ba8560d83fc8', '501561d2d26d4ae3bed168b8388ef1af', '253ab78f548041b7aa830f0c549b0bc6', '5CD33044L4', 'EQ7QEI2PZ7ZJ', NULL),
('2025-04-11 05:54:22.975911', '2025-04-11 05:55:30.386509', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'deadd9e934ca4826adbaf38b1b39994b', '359979217333014', 2023, 'NOKIA C32', NULL, 'NOKIA C32 TA-1534 50MP CAM, HDD 64GB, MEM 4GB', 1, '94a77b664b5d4efab801ba8560d83fc8', '34b82e356fe646a09f9fc089943eaef5', '7987fab285b64b3f81ca867e0e5d7f51', '359979217333022', 'EQ89UWIXEPOL', NULL),
('2025-04-11 06:00:59.337399', '2025-04-11 06:02:01.701219', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'ecb8f075541f41579661820b2759f87b', '762583065', 2025, 'SIM CARD', NULL, 'MTN SIM CARD', 1, '94a77b664b5d4efab801ba8560d83fc8', '44f1ddd202ae46ec9a4e1ea2ed96bee7', '9f6841f247f04c468c1b0765776cad7a', '762583065', 'EQBVPR0JTL3C', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `aix_equipmenttypemodel`
--

CREATE TABLE `aix_equipmenttypemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_equipmenttypemodel`
--

INSERT INTO `aix_equipmenttypemodel` (`created`, `updated`, `uuid`, `code`, `name`, `description`, `entity_id`) VALUES
('2025-04-03 09:30:20.900589', '2025-04-03 09:30:20.902597', '04f3db9b630a4abba628fed1be5fa621', 'EQT7R5XUXJRJ1', 'Access Control Machine', 'Access Control Machine for Time and Attendance Machine', '94a77b664b5d4efab801ba8560d83fc8'),
('2025-07-31 09:28:26.142329', '2025-07-31 09:28:26.143725', '0dbbb89edab7441d85c3d022d1ad4547', 'EQTRC8P4TRVPF', 'Pickup', 'Pickup', '94a77b664b5d4efab801ba8560d83fc8'),
('2025-03-31 11:38:30.498969', '2025-03-31 11:38:30.499922', '253ab78f548041b7aa830f0c549b0bc6', 'EQTITYLNOQ9AU', 'Laptops', 'Laptops', '94a77b664b5d4efab801ba8560d83fc8'),
('2025-03-28 12:03:30.964526', '2025-03-31 11:36:55.775977', '3f6cac757d704906be4532a96b145800', 'NA', 'Desktop Computers', 'Desktop Computers', '94a77b664b5d4efab801ba8560d83fc8'),
('2025-04-11 06:05:01.123842', '2025-04-11 06:05:01.124872', '79758f2194694323a62c54a8d76bb01e', 'EQT68U09UYG8M', 'MIFI', 'MIFI', '94a77b664b5d4efab801ba8560d83fc8'),
('2025-04-11 05:25:19.905912', '2025-04-11 05:25:19.907846', '7987fab285b64b3f81ca867e0e5d7f51', 'EQTRUNLE4ID4Z', 'Mobile Phone', 'Mobile Phone', '94a77b664b5d4efab801ba8560d83fc8'),
('2025-04-11 05:58:36.686934', '2025-04-11 05:58:36.687928', '9f6841f247f04c468c1b0765776cad7a', 'EQTO4HWZPR0TE', 'SIM CARD', 'SIM CARD', '94a77b664b5d4efab801ba8560d83fc8'),
('2025-07-31 09:28:44.653001', '2025-07-31 09:28:44.654526', 'e0d3055df539426580a4dc9cdecc4ce8', 'EQTR1IOGKK8BI', 'Vehicle', 'Vehicle', '94a77b664b5d4efab801ba8560d83fc8'),
('2025-07-31 09:28:13.563459', '2025-07-31 09:28:13.565762', 'efc80a66b94f412684dcd71527a1bc9a', 'EQTON4DT2WMT4', 'Truck', 'Truck', '94a77b664b5d4efab801ba8560d83fc8');

-- --------------------------------------------------------

--
-- Table structure for table `aix_estimatemodel`
--

CREATE TABLE `aix_estimatemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `markdown_notes` longtext DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `estimate_number` varchar(20) NOT NULL,
  `terms` varchar(10) NOT NULL,
  `title` varchar(250) NOT NULL,
  `status` varchar(10) NOT NULL,
  `date_draft` date DEFAULT NULL,
  `date_in_review` date DEFAULT NULL,
  `date_approved` date DEFAULT NULL,
  `date_completed` date DEFAULT NULL,
  `date_canceled` date DEFAULT NULL,
  `date_void` date DEFAULT NULL,
  `revenue_estimate` decimal(20,2) NOT NULL,
  `labor_estimate` decimal(20,2) NOT NULL,
  `material_estimate` decimal(20,2) NOT NULL,
  `equipment_estimate` decimal(20,2) NOT NULL,
  `other_estimate` decimal(20,2) NOT NULL,
  `customer_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_generalnotificationmodel`
--

CREATE TABLE `aix_generalnotificationmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `link` longtext DEFAULT NULL,
  `parameter` longtext DEFAULT NULL,
  `extra_parameter` longtext DEFAULT NULL,
  `title` longtext NOT NULL,
  `date` date NOT NULL,
  `is_read` tinyint(1) NOT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `notification_external_type_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_holidaymodel`
--

CREATE TABLE `aix_holidaymodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `date` date NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_immigrationdetailmodel`
--

CREATE TABLE `aix_immigrationdetailmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `passport_number` varchar(255) NOT NULL,
  `issue_date` date NOT NULL,
  `expiry_date` date NOT NULL,
  `citizenship` varchar(255) NOT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_importjobmodel`
--

CREATE TABLE `aix_importjobmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `description` varchar(200) NOT NULL,
  `completed` tinyint(1) NOT NULL,
  `ledger_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_incomingdocumenthandlermodel`
--

CREATE TABLE `aix_incomingdocumenthandlermodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `incoming_document_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_incomingdocumentmodel`
--

CREATE TABLE `aix_incomingdocumentmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `doc_from` varchar(255) NOT NULL,
  `subject` varchar(255) DEFAULT NULL,
  `delivered_by` varchar(255) DEFAULT NULL,
  `date_written` date DEFAULT NULL,
  `date_received` date NOT NULL,
  `comment` longtext DEFAULT NULL,
  `doc_type_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `received_by_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_incomingdocumenttypemodel`
--

CREATE TABLE `aix_incomingdocumenttypemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_insurancedetailmodel`
--

CREATE TABLE `aix_insurancedetailmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `policy_name` varchar(255) NOT NULL,
  `company_name` varchar(255) NOT NULL,
  `pin_number` varchar(255) DEFAULT NULL,
  `certificate_number` varchar(255) NOT NULL,
  `premium` int(11) NOT NULL,
  `address` varchar(255) NOT NULL,
  `issue_date` date NOT NULL,
  `expiry_date` date DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `comment` longtext DEFAULT NULL,
  `currency_id` char(32) NOT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_invoiceactionmodel`
--

CREATE TABLE `aix_invoiceactionmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `comment` longtext DEFAULT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `invoice_id` char(32) NOT NULL,
  `invoice_status_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_invoicemodel`
--

CREATE TABLE `aix_invoicemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `terms` varchar(10) NOT NULL,
  `amount_due` decimal(20,2) NOT NULL,
  `amount_paid` decimal(20,2) NOT NULL,
  `amount_receivable` decimal(20,2) NOT NULL,
  `amount_unearned` decimal(20,2) NOT NULL,
  `amount_earned` decimal(20,2) NOT NULL,
  `date` date NOT NULL,
  `due_date` date NOT NULL,
  `accrue` tinyint(1) NOT NULL,
  `progress` decimal(3,2) NOT NULL,
  `markdown_notes` longtext DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `invoice_number` varchar(20) NOT NULL,
  `invoice_status` varchar(10) NOT NULL,
  `additional_info` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`additional_info`)),
  `draft_date` date DEFAULT NULL,
  `in_review_date` date DEFAULT NULL,
  `approved_date` date DEFAULT NULL,
  `paid_date` date DEFAULT NULL,
  `void_date` date DEFAULT NULL,
  `canceled_date` date DEFAULT NULL,
  `cash_account_id` char(32) NOT NULL,
  `ce_model_id` char(32) DEFAULT NULL,
  `customer_id` char(32) NOT NULL,
  `ledger_id` char(32) NOT NULL,
  `prepaid_account_id` char(32) NOT NULL,
  `unearned_account_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_invoicemodel`
--

INSERT INTO `aix_invoicemodel` (`created`, `updated`, `terms`, `amount_due`, `amount_paid`, `amount_receivable`, `amount_unearned`, `amount_earned`, `date`, `due_date`, `accrue`, `progress`, `markdown_notes`, `uuid`, `invoice_number`, `invoice_status`, `additional_info`, `draft_date`, `in_review_date`, `approved_date`, `paid_date`, `void_date`, `canceled_date`, `cash_account_id`, `ce_model_id`, `customer_id`, `ledger_id`, `prepaid_account_id`, `unearned_account_id`) VALUES
('2024-02-25 02:56:34.143067', '2024-02-27 06:05:53.076702', 'on_receipt', '17150000.00', '17150000.00', '0.00', '0.00', '17150000.00', '2024-02-25', '2024-02-25', 0, '1.00', 'initial payment made 15/01/2024', '12721303ac0c47f4b244c9f486b4eecc', 'I-VW7IR91G6X', 'paid', NULL, NULL, '2024-02-25', '2024-02-25', '2024-02-27', NULL, NULL, '6fe4fe62eba44a3bbf5ca23fdd2c5ae5', NULL, 'e69edfe356fe484683ae93a593df2fe9', 'f10a1fb314cf40a5a4d364b151b7a42b', '0ddc3a9298bd4cffaa7676fc360341bb', '2a42258d8fc04a8982890d6483d7d055'),
('2024-02-25 02:49:00.414556', '2024-02-25 02:49:00.414556', 'on_receipt', '0.00', '0.00', '0.00', '0.00', '0.00', '2024-02-25', '2024-02-25', 0, '0.00', NULL, '5739a5ffffe5436c967e2d09f8461f7a', 'I-G9K09K5VF1', 'draft', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '6fe4fe62eba44a3bbf5ca23fdd2c5ae5', NULL, 'e69edfe356fe484683ae93a593df2fe9', '38f899c22d4b4b4da4274db9b394f16a', '0ddc3a9298bd4cffaa7676fc360341bb', '2a42258d8fc04a8982890d6483d7d055'),
('2025-08-19 12:06:42.997221', '2025-08-19 12:10:28.218005', 'on_receipt', '440.00', '370.00', '0.00', '0.00', '370.00', '2025-08-19', '2025-08-19', 0, '0.00', 'First Payment', '78eeae0158fe42c8b6a06d5d98a87a0b', 'I-4MLEIX9X6V', 'approved', NULL, NULL, '2025-08-19', '2025-08-19', NULL, NULL, NULL, '4e69855b236b4795a4eb06c5670dfae4', NULL, '8844b93b0dee4a77afb91daa81968f61', '34f5c61f4abf44c5b64a4ea96435e4d0', 'de3785e25bbc490483b39843f47113ff', '40beb5f8c5b6460799003d3d9b87b7ca'),
('2024-02-25 02:51:49.331262', '2024-02-25 02:51:49.331262', 'on_receipt', '0.00', '0.00', '0.00', '0.00', '0.00', '2024-02-25', '2024-02-25', 0, '0.00', NULL, 'c98b0c8c09cb4b9495509531fe44d316', 'I-L40W8I13HP', 'draft', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '6fe4fe62eba44a3bbf5ca23fdd2c5ae5', NULL, 'e69edfe356fe484683ae93a593df2fe9', '834f115c310f43cdbc84c579b04cca95', '0ddc3a9298bd4cffaa7676fc360341bb', '2a42258d8fc04a8982890d6483d7d055'),
('2024-02-25 02:55:53.778890', '2024-02-25 15:42:14.293803', 'on_receipt', '372750.00', '70000.00', '0.00', '0.00', '70000.00', '2024-02-25', '2024-02-25', 0, '0.00', 'There is pending JMP to be approved for full payment to be made', 'e24b8156118346e2abb52f70ecb6112e', 'I-RZQKJBF110', 'approved', NULL, NULL, '2024-02-25', '2024-02-25', NULL, NULL, NULL, '6fe4fe62eba44a3bbf5ca23fdd2c5ae5', NULL, 'e69edfe356fe484683ae93a593df2fe9', '26d0795227444e7fbdc6b8d8ad272a2f', '0ddc3a9298bd4cffaa7676fc360341bb', '2a42258d8fc04a8982890d6483d7d055');

-- --------------------------------------------------------

--
-- Table structure for table `aix_invoicestatusmodel`
--

CREATE TABLE `aix_invoicestatusmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_invoicetypemodel`
--

CREATE TABLE `aix_invoicetypemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_itemfawmodel`
--

CREATE TABLE `aix_itemfawmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `attendance_code` varchar(10) DEFAULT NULL,
  `attendance_date` date NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_itemfawthroughmodel`
--

CREATE TABLE `aix_itemfawthroughmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `attendance_code` varchar(10) DEFAULT NULL,
  `attendance_date` date DEFAULT NULL,
  `faw_item_status` varchar(15) DEFAULT NULL,
  `entity_unit_id` char(32) DEFAULT NULL,
  `faw_model_id` char(32) DEFAULT NULL,
  `parent_id` char(32) DEFAULT NULL,
  `employee_model_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_itemfawthroughmodel`
--

INSERT INTO `aix_itemfawthroughmodel` (`created`, `updated`, `uuid`, `attendance_code`, `attendance_date`, `faw_item_status`, `entity_unit_id`, `faw_model_id`, `parent_id`, `employee_model_id`) VALUES
('2025-08-14 11:45:23.312061', '2025-08-14 11:45:23.312061', '111b3c92142d442782fa7b5d8443aab5', 'A', '2025-08-12', 'draft', NULL, 'b62649ce6f704cf4b6a5c1094e6c0ef6', NULL, '641de26c55c444bfaaaf8d26e6a3b3cc'),
('2025-08-14 11:45:23.315061', '2025-08-14 11:45:23.315061', '219a4402f1094e50a32b1a111291305d', 'A', '2025-08-12', 'draft', NULL, 'b62649ce6f704cf4b6a5c1094e6c0ef6', NULL, '89ef25176e53432e83a713fcf083b6f6'),
('2025-08-14 11:43:10.565477', '2025-08-14 11:43:10.565477', '21adbb3fb25b40bb8d946b6138041bde', 'A', '2025-08-01', 'draft', NULL, 'd85d632fbc0749828eb3abe247070154', NULL, '89ef25176e53432e83a713fcf083b6f6'),
('2025-08-14 11:44:46.929603', '2025-08-18 13:38:06.745496', '26c3a31b27104e73b35f7713ce0884d1', 'L', '2025-08-08', 'draft', NULL, '34b2ff0dad1f4d3ebcf8816b2201f861', NULL, '89ef25176e53432e83a713fcf083b6f6'),
('2025-08-14 11:43:10.563478', '2025-08-18 13:37:20.691332', '2e82a2fdcf384ee89e81577264587c81', 'S', '2025-08-01', 'draft', NULL, 'd85d632fbc0749828eb3abe247070154', NULL, '06ceefa18855477e9f9b7bfc82df4055'),
('2025-08-14 11:44:46.923607', '2025-08-18 13:38:06.747494', '9e3afff29593408886da59eb6dd8e8ec', 'DMB', '2025-08-08', 'draft', NULL, '34b2ff0dad1f4d3ebcf8816b2201f861', NULL, '641de26c55c444bfaaaf8d26e6a3b3cc'),
('2025-08-14 11:44:46.927614', '2025-08-18 13:38:06.748808', 'da680551303449a79b8d697a7d7b78a1', 'P', '2025-08-08', 'draft', NULL, '34b2ff0dad1f4d3ebcf8816b2201f861', NULL, '06ceefa18855477e9f9b7bfc82df4055'),
('2025-08-14 11:45:23.314106', '2025-08-14 11:45:23.314106', 'f482686ee9234ea68a9455b31468fbea', 'A', '2025-08-12', 'draft', NULL, 'b62649ce6f704cf4b6a5c1094e6c0ef6', NULL, '06ceefa18855477e9f9b7bfc82df4055'),
('2025-08-14 11:43:10.561570', '2025-08-18 13:37:20.694700', 'fd8bc6211b9945f586d24e3da9ce5aa7', 'MOB', '2025-08-01', 'draft', NULL, 'd85d632fbc0749828eb3abe247070154', NULL, '641de26c55c444bfaaaf8d26e6a3b3cc');

-- --------------------------------------------------------

--
-- Table structure for table `aix_itemfetmodel`
--

CREATE TABLE `aix_itemfetmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `attendance_code` varchar(10) DEFAULT NULL,
  `attendance_date` date NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_itemfetthroughmodel`
--

CREATE TABLE `aix_itemfetthroughmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `attendance_code` varchar(10) DEFAULT NULL,
  `attendance_date` date DEFAULT NULL,
  `fet_item_status` varchar(15) DEFAULT NULL,
  `entity_unit_id` char(32) DEFAULT NULL,
  `equipment_model_id` char(32) NOT NULL,
  `fet_model_id` char(32) DEFAULT NULL,
  `parent_id` char(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_itemfetthroughmodel`
--

INSERT INTO `aix_itemfetthroughmodel` (`created`, `updated`, `uuid`, `attendance_code`, `attendance_date`, `fet_item_status`, `entity_unit_id`, `equipment_model_id`, `fet_model_id`, `parent_id`) VALUES
('2025-08-04 12:22:25.662954', '2025-08-04 12:23:48.810006', '477dd0c9eef1461b8123f85fe416b394', 'R', '2025-08-02', 'draft', NULL, '9d567b728c2745d49603a94ffdca509d', 'c5b477ca8c2f4db69ba5612570f381e1', NULL),
('2025-08-04 11:42:02.233609', '2025-08-04 11:42:38.877740', '9c228d87c25c4a57b1716945b38ee100', 'DMB', '2025-08-04', 'draft', NULL, '9d567b728c2745d49603a94ffdca509d', '31f5c393f39e42a388ede5017eedb469', NULL),
('2025-07-31 09:45:50.068588', '2025-08-18 07:51:36.719364', 'b0f0b275f459488c862ba4239ea9dfe6', 'OPS', '2025-08-01', 'draft', NULL, 'a7d931a9c19e4f00abd95a27eca43f07', '9fc83648fb2148459c0f49fc29f20d59', NULL),
('2025-07-31 10:12:23.817618', '2025-08-18 07:51:21.704659', 'f593a1f70ab645528eb0da4424128d0b', 'NOS', '2025-08-01', 'draft', NULL, '9d567b728c2745d49603a94ffdca509d', '9fc83648fb2148459c0f49fc29f20d59', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `aix_itemmodel`
--

CREATE TABLE `aix_itemmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `name` varchar(100) NOT NULL,
  `item_type` varchar(1) DEFAULT NULL,
  `sku` varchar(50) DEFAULT NULL,
  `upc` varchar(50) DEFAULT NULL,
  `item_id` varchar(50) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `default_amount` decimal(20,2) NOT NULL,
  `for_inventory` tinyint(1) NOT NULL,
  `is_product_or_service` tinyint(1) NOT NULL,
  `sold_as_unit` tinyint(1) NOT NULL,
  `inventory_received` decimal(20,3) DEFAULT NULL,
  `inventory_received_value` decimal(20,2) DEFAULT NULL,
  `additional_info` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`additional_info`)),
  `cogs_account_id` char(32) DEFAULT NULL,
  `earnings_account_id` char(32) DEFAULT NULL,
  `entity_id` char(32) NOT NULL,
  `expense_account_id` char(32) DEFAULT NULL,
  `inventory_account_id` char(32) DEFAULT NULL,
  `uom_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_itemmodel`
--

INSERT INTO `aix_itemmodel` (`created`, `updated`, `uuid`, `name`, `item_type`, `sku`, `upc`, `item_id`, `is_active`, `default_amount`, `for_inventory`, `is_product_or_service`, `sold_as_unit`, `inventory_received`, `inventory_received_value`, `additional_info`, `cogs_account_id`, `earnings_account_id`, `entity_id`, `expense_account_id`, `inventory_account_id`, `uom_id`) VALUES
('2024-02-23 23:24:02.254561', '2024-02-26 05:54:55.405124', '05951a6584a04897b2467cf2714294bf', 'Transport Only', 'L', NULL, NULL, NULL, 1, '0.00', 0, 1, 0, NULL, NULL, NULL, NULL, '07600d5fb68449ba8571f451e21f58e6', '1980d2af5ea14ad5b1e7712771f60517', NULL, NULL, 'ff373e75455341ee967c633bf6f51945'),
('2024-02-24 17:18:04.373564', '2024-02-24 17:18:04.378554', '1d6166199b274ba4be282d2f3c6d740a', 'Diesel', 'F', NULL, NULL, NULL, 1, '3550.00', 1, 0, 0, NULL, NULL, NULL, 'ccbf1dda6f6847cca5c308dbd3e85b12', NULL, '1980d2af5ea14ad5b1e7712771f60517', NULL, '100846fca4c34f5684593663d3c530ea', '829569dcbb8343bf9ccdcf7b31054c61'),
('2024-02-23 23:25:37.708800', '2024-02-23 23:25:37.711231', '2ed8dd20a78b492087d7b1e069dc74d0', 'Petrol', 'F', NULL, NULL, NULL, 1, '0.00', 0, 1, 0, NULL, NULL, NULL, NULL, NULL, '1980d2af5ea14ad5b1e7712771f60517', NULL, NULL, '829569dcbb8343bf9ccdcf7b31054c61'),
('2024-02-23 23:25:11.931758', '2024-02-23 23:25:11.934760', '4f74751c3d7241cdb8d866fa2c7fef1b', 'Diesel', 'F', NULL, NULL, NULL, 1, '0.00', 0, 1, 0, NULL, NULL, NULL, NULL, NULL, '1980d2af5ea14ad5b1e7712771f60517', NULL, NULL, '829569dcbb8343bf9ccdcf7b31054c61'),
('2024-02-27 07:54:32.432276', '2024-02-27 07:54:32.435511', '50435d676ff8407f99f073988586df48', 'Safety Boot', 'M', NULL, NULL, NULL, 1, '0.00', 1, 0, 0, NULL, NULL, NULL, 'ccbf1dda6f6847cca5c308dbd3e85b12', NULL, '1980d2af5ea14ad5b1e7712771f60517', NULL, '100846fca4c34f5684593663d3c530ea', 'dffb447d188c4415bb4720bd6f790c09'),
('2024-02-23 23:24:37.489568', '2024-02-26 05:54:42.937851', 'b238de26b9ca46f893d67dc48d1e6734', 'Transport and Lifting', 'L', NULL, NULL, NULL, 1, '0.00', 0, 1, 0, NULL, NULL, NULL, NULL, '07600d5fb68449ba8571f451e21f58e6', '1980d2af5ea14ad5b1e7712771f60517', NULL, NULL, 'ff373e75455341ee967c633bf6f51945'),
('2025-08-19 12:01:32.612915', '2025-08-19 12:01:32.622621', 'b367e42bb05d41f682254592ff0a2cdc', 'Transport Van', 'E', NULL, NULL, NULL, 1, '0.00', 0, 1, 0, NULL, NULL, NULL, NULL, '6ab36e56e4ab444bbac6895e345e459f', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, 'f7fb1df983d14f169acfb56973622237'),
('2025-08-19 12:02:12.517743', '2025-08-19 12:02:12.522288', 'ca919b4fabb64dd9ae1f51e28aa3e7a9', 'Lifting', 'E', NULL, NULL, NULL, 1, '5000.00', 0, 1, 0, NULL, NULL, NULL, NULL, '7b222c30d54a4061bea36fb0acb0edd8', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, '8875a0d1eecd4bd3b846d08d1e975592');

-- --------------------------------------------------------

--
-- Table structure for table `aix_itemthroughmodel`
--

CREATE TABLE `aix_itemthroughmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `quantity` double NOT NULL,
  `unit_cost` double NOT NULL,
  `total_amount` decimal(20,2) NOT NULL,
  `po_item_status` varchar(15) DEFAULT NULL,
  `po_quantity` double NOT NULL,
  `po_unit_cost` double DEFAULT NULL,
  `po_total_amount` decimal(20,2) NOT NULL,
  `jcd_item_status` varchar(15) DEFAULT NULL,
  `jcd_quantity` double NOT NULL,
  `jcd_unit_cost` double DEFAULT NULL,
  `jcd_total_amount` decimal(20,2) NOT NULL,
  `jcd_fuel_type` varchar(15) DEFAULT NULL,
  `ce_unit_revenue_estimate` double DEFAULT NULL,
  `ce_revenue_estimate` decimal(20,2) DEFAULT NULL,
  `bill_model_id` char(32) DEFAULT NULL,
  `ce_model_id` char(32) DEFAULT NULL,
  `entity_unit_id` char(32) DEFAULT NULL,
  `invoice_model_id` char(32) DEFAULT NULL,
  `item_model_id` char(32) NOT NULL,
  `jcd_model_id` char(32) DEFAULT NULL,
  `parent_id` char(32) DEFAULT NULL,
  `po_model_id` char(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_itemthroughmodel`
--

INSERT INTO `aix_itemthroughmodel` (`created`, `updated`, `uuid`, `quantity`, `unit_cost`, `total_amount`, `po_item_status`, `po_quantity`, `po_unit_cost`, `po_total_amount`, `jcd_item_status`, `jcd_quantity`, `jcd_unit_cost`, `jcd_total_amount`, `jcd_fuel_type`, `ce_unit_revenue_estimate`, `ce_revenue_estimate`, `bill_model_id`, `ce_model_id`, `entity_unit_id`, `invoice_model_id`, `item_model_id`, `jcd_model_id`, `parent_id`, `po_model_id`) VALUES
('2024-02-25 13:48:28.219781', '2024-02-25 13:48:28.219781', '020f6130739046be8106658d8ab80349', 35, 3550, '124250.00', NULL, 0, 0, '0.00', NULL, 0, 0, '0.00', NULL, NULL, NULL, NULL, NULL, NULL, 'e24b8156118346e2abb52f70ecb6112e', '2ed8dd20a78b492087d7b1e069dc74d0', NULL, NULL, NULL),
('2024-02-27 08:02:33.909299', '2024-02-27 08:02:33.909299', '10ddd0eb28e64473bc0867ccd36a6438', 1, 250000, '250000.00', NULL, 0, 0, '0.00', NULL, 0, 0, '0.00', NULL, NULL, NULL, 'd8f99b49272e401f94ceba217bd1562f', NULL, '06c455e12a7f4d019f2bd779aee9a655', NULL, '50435d676ff8407f99f073988586df48', NULL, NULL, NULL),
('2025-08-19 12:08:38.325142', '2025-08-19 12:08:38.325142', '1e0e124d63a44851abcecf3411a3acbb', 2, 145, '290.00', NULL, 0, 0, '0.00', NULL, 0, 0, '0.00', NULL, NULL, NULL, NULL, NULL, NULL, '78eeae0158fe42c8b6a06d5d98a87a0b', 'b367e42bb05d41f682254592ff0a2cdc', NULL, NULL, NULL),
('2024-02-25 13:17:43.286322', '2024-02-25 13:17:43.286322', '23927a6566154afcb7d3faeafed66f19', 0, 0, '0.00', NULL, 0, 0, '0.00', NULL, 1, 6300000, '6300000.00', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'b238de26b9ca46f893d67dc48d1e6734', '08a4c4fa88f8498681ced8886c89e38d', NULL, NULL),
('2024-02-27 07:55:34.451487', '2024-02-27 08:02:33.907298', '293a1d4fe75241f6a13dc2b1ad84d2af', 2, 270000, '540000.00', 'ordered', 3, 270000, '810000.00', NULL, 0, 0, '0.00', NULL, NULL, NULL, 'd8f99b49272e401f94ceba217bd1562f', NULL, '06c455e12a7f4d019f2bd779aee9a655', NULL, '50435d676ff8407f99f073988586df48', NULL, NULL, '349b75ce8086421e952b35cc05559751'),
('2024-02-25 01:13:00.456324', '2024-02-25 01:13:00.456324', '363cfe6758364e978dc1498ebdab3e81', 80, 3547, '283760.00', NULL, 0, 0, '0.00', NULL, 0, 0, '0.00', NULL, NULL, NULL, '33a378ad8eeb451aab75a5c95c581b7f', NULL, NULL, NULL, '1d6166199b274ba4be282d2f3c6d740a', NULL, NULL, NULL),
('2024-02-25 13:45:41.660869', '2024-02-25 13:45:41.660869', '56eaf0e98fcb4027b163353b721b43f9', 35, 3550, '124250.00', NULL, 0, 0, '0.00', NULL, 0, 0, '0.00', NULL, NULL, NULL, NULL, NULL, NULL, 'e24b8156118346e2abb52f70ecb6112e', '2ed8dd20a78b492087d7b1e069dc74d0', NULL, NULL, NULL),
('2024-02-25 13:46:15.241449', '2024-02-25 13:46:15.242544', '65b830a64adb404bb666a7c2b844230d', 35, 3550, '124250.00', NULL, 0, 0, '0.00', NULL, 0, 0, '0.00', NULL, NULL, NULL, NULL, NULL, NULL, 'e24b8156118346e2abb52f70ecb6112e', '2ed8dd20a78b492087d7b1e069dc74d0', NULL, NULL, NULL),
('2024-02-25 02:39:07.013441', '2024-02-25 12:26:12.358645', '6e567d4a91644b9b92e90398ebfef67c', 2, 6300000, '12600000.00', NULL, 0, 0, '0.00', 'ordered', 3, 6300000, '18900000.00', NULL, NULL, NULL, NULL, NULL, NULL, '12721303ac0c47f4b244c9f486b4eecc', 'b238de26b9ca46f893d67dc48d1e6734', '947f2c03f52b4e28841067d7508de40c', NULL, NULL),
('2024-02-24 17:19:12.818496', '2024-02-27 07:51:20.045346', 'b6ba3a92e70a42dcb897d65a747bc7e6', 47, 3560, '167320.00', 'in_transit', 127, 3550, '450850.00', NULL, 0, 0, '0.00', NULL, NULL, NULL, '33a378ad8eeb451aab75a5c95c581b7f', NULL, NULL, NULL, '1d6166199b274ba4be282d2f3c6d740a', NULL, NULL, '38da982bc8ce4d6b9f4b09d58e16a291'),
('2025-08-19 12:03:11.527891', '2025-08-19 12:07:53.335203', 'e8cc73539fbc408fa14fb573a3a5b160', 1, 150, '150.00', NULL, 0, 0, '0.00', NULL, 3, 150, '450.00', NULL, NULL, NULL, NULL, NULL, NULL, '78eeae0158fe42c8b6a06d5d98a87a0b', 'b367e42bb05d41f682254592ff0a2cdc', 'fd623ee6b7124bceb64d970716a82bf9', NULL, NULL),
('2024-02-25 02:39:07.009920', '2024-02-25 12:44:49.183500', 'f8cea86ffaeb470ea27c000fe7783bc8', 1, 4550000, '4550000.00', 'ordered', 0, 0, '0.00', 'ordered', 2, 4550000, '9100000.00', NULL, NULL, NULL, NULL, NULL, NULL, '12721303ac0c47f4b244c9f486b4eecc', '05951a6584a04897b2467cf2714294bf', '947f2c03f52b4e28841067d7508de40c', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `aix_jobapplicantmodel`
--

CREATE TABLE `aix_jobapplicantmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `address_1` varchar(70) NOT NULL,
  `address_2` varchar(70) DEFAULT NULL,
  `city` varchar(70) DEFAULT NULL,
  `state` varchar(70) DEFAULT NULL,
  `zip_code` varchar(20) DEFAULT NULL,
  `country` varchar(70) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `website` varchar(200) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `date` date DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `applicant_id` int(11) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `job_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_jobcategorymodel`
--

CREATE TABLE `aix_jobcategorymodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_jobmodel`
--

CREATE TABLE `aix_jobmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `title` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `location` varchar(300) NOT NULL,
  `job_type` varchar(1) NOT NULL,
  `salary` varchar(30) NOT NULL,
  `company_name` varchar(300) NOT NULL,
  `company_description` longtext DEFAULT NULL,
  `url` varchar(200) NOT NULL,
  `last_date` date NOT NULL,
  `is_published` tinyint(1) NOT NULL,
  `is_closed` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `category_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_journalentrymodel`
--

CREATE TABLE `aix_journalentrymodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `date` date NOT NULL,
  `description` varchar(70) DEFAULT NULL,
  `activity` varchar(5) NOT NULL,
  `origin` varchar(30) DEFAULT NULL,
  `posted` tinyint(1) NOT NULL,
  `locked` tinyint(1) NOT NULL,
  `entity_unit_id` char(32) DEFAULT NULL,
  `ledger_id` char(32) NOT NULL,
  `parent_id` char(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_journalentrymodel`
--

INSERT INTO `aix_journalentrymodel` (`created`, `updated`, `uuid`, `date`, `description`, `activity`, `origin`, `posted`, `locked`, `entity_unit_id`, `ledger_id`, `parent_id`) VALUES
('2024-02-25 03:14:45.504494', '2024-02-25 03:14:45.504494', '02702b4e07e848bbb4c98ded1b3f1fa2', '2024-02-25', 'Invoice I-VW7IR91G6X account adjustment.', 'op', 'migration', 1, 1, NULL, 'f10a1fb314cf40a5a4d364b151b7a42b', NULL),
('2024-02-25 13:45:41.677078', '2024-02-25 13:45:41.677078', '046caf612e6e47fdb0bf08946710de33', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 13:04:15.560002', '2024-02-25 13:04:15.560002', '0603f60ac9974779a3458e6f0af57f40', '2024-02-25', 'Invoice I-VW7IR91G6X account adjustment.', 'op', 'migration', 1, 1, NULL, 'f10a1fb314cf40a5a4d364b151b7a42b', NULL),
('2025-08-19 12:08:38.395241', '2025-08-19 12:08:38.395241', '1107435ca6f048ed94b0c9f1d0f60424', '2025-08-19', 'Invoice I-4MLEIX9X6V account adjustment.', 'op', 'migration', 1, 1, NULL, '34f5c61f4abf44c5b64a4ea96435e4d0', NULL),
('2024-02-25 14:02:40.662420', '2024-02-25 14:02:40.662420', '1f04739004724f43b3ca965a5affa2b9', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 13:02:49.895886', '2024-02-25 13:02:49.895886', '236592a68dde42bd984d2c2480cc460c', '2024-02-25', 'Invoice I-VW7IR91G6X account adjustment.', 'op', 'migration', 1, 1, NULL, 'f10a1fb314cf40a5a4d364b151b7a42b', NULL),
('2024-02-25 14:04:38.996618', '2024-02-25 14:04:38.996618', '2744dda946a94b069f43e2f314cdb96f', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2025-08-19 12:07:53.425903', '2025-08-19 12:07:53.425903', '2828d9d5df844126be2c4d8ba639de0c', '2025-08-19', 'Invoice I-4MLEIX9X6V account adjustment.', 'op', 'migration', 1, 1, NULL, '34f5c61f4abf44c5b64a4ea96435e4d0', NULL),
('2024-02-27 06:05:53.108764', '2024-02-27 06:05:53.108764', '2f1eb0a36bbc4885a1ba71a921a1ae4a', '2024-02-27', 'Invoice I-VW7IR91G6X account adjustment.', 'op', 'migration', 1, 1, NULL, 'f10a1fb314cf40a5a4d364b151b7a42b', NULL),
('2024-02-25 13:56:52.946936', '2024-02-25 13:56:52.946936', '3b2c38dd4006409398aba1c8c7501b11', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 13:28:21.460579', '2024-02-25 13:28:21.460579', '3e1d325d40dd447b9cf51ea530cb3d38', '2024-02-25', 'Invoice I-VW7IR91G6X account adjustment.', 'op', 'migration', 1, 1, NULL, 'f10a1fb314cf40a5a4d364b151b7a42b', NULL),
('2024-02-25 14:17:30.294726', '2024-02-25 14:17:30.294726', '440f2907c9344ea89f4e7026652ac45b', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 13:48:28.237905', '2024-02-25 13:48:28.237905', '4c9e59fd1e7842d1a2a467b9a82acb71', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 03:13:00.609053', '2024-02-25 03:13:00.609053', '4e376c5294e24c0a987732485e5809a0', '2024-02-25', 'Invoice I-VW7IR91G6X account adjustment.', 'op', 'migration', 1, 1, NULL, 'f10a1fb314cf40a5a4d364b151b7a42b', NULL),
('2024-02-25 01:55:12.957886', '2024-02-25 01:55:12.957886', '51c421747dba45b298bacbdb44dec37f', '2024-02-25', 'Bill B-8OSP8WGZ4P account adjustment.', 'op', 'migration', 1, 1, NULL, '838120708f9c4be88af1be7cddc17bc4', NULL),
('2024-02-27 08:02:33.933245', '2024-02-27 08:02:33.933245', '59f0d7ff4fdd42a682291f9e50eb1775', '2024-02-27', 'Bill B-X88Q8YMPJS account adjustment.', 'op', 'migration', 1, 1, '06c455e12a7f4d019f2bd779aee9a655', '1908708c1f40487fb93eb7c98370dc0a', NULL),
('2024-02-25 15:42:14.281805', '2024-02-25 15:42:14.281805', '5e4d577e398c40128899731181cbd8fe', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 13:20:14.694479', '2024-02-25 13:20:14.694479', '5fcc1110e16841388193a6bfb78ff08a', '2024-02-25', 'Invoice I-VW7IR91G6X account adjustment.', 'op', 'migration', 1, 1, NULL, 'f10a1fb314cf40a5a4d364b151b7a42b', NULL),
('2024-02-25 14:03:14.972675', '2024-02-25 14:03:14.972675', '60b47d200b85416f98ea6f2ce50aa37b', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 01:34:32.644880', '2024-02-25 01:34:32.644880', '62c4473ebad545f3bf418e3174f5d4ac', '2024-02-25', 'Bill B-8OSP8WGZ4P account adjustment.', 'op', 'migration', 1, 1, NULL, '838120708f9c4be88af1be7cddc17bc4', NULL),
('2024-02-25 15:00:18.297652', '2024-02-25 15:00:18.297652', '66f133858ee34270be56f0b10d030d19', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 13:30:09.553261', '2024-02-25 13:30:09.553261', '687fe0f605cf41ff8c839cc159f59434', '2024-02-25', 'Invoice I-VW7IR91G6X account adjustment.', 'op', 'migration', 1, 1, NULL, 'f10a1fb314cf40a5a4d364b151b7a42b', NULL),
('2024-02-25 13:06:06.987797', '2024-02-25 13:06:06.987797', '6c6c349ec45f4a7d9fcbfe03831f8aee', '2024-02-25', 'Invoice I-VW7IR91G6X account adjustment.', 'op', 'migration', 1, 1, NULL, 'f10a1fb314cf40a5a4d364b151b7a42b', NULL),
('2024-02-25 13:52:55.196399', '2024-02-25 13:52:55.196399', '6cb78f601ada445ba40cd4efe2858c4a', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 12:53:12.924649', '2024-02-25 12:53:12.924649', '6d32832fb9aa430d91d782924b1dbb6c', '2024-02-25', 'Invoice I-VW7IR91G6X account adjustment.', 'op', 'migration', 1, 1, NULL, 'f10a1fb314cf40a5a4d364b151b7a42b', NULL),
('2024-02-25 14:10:51.455405', '2024-02-25 14:10:51.455405', '715cf8b1d1fb4abbbeaf653f6c9acde1', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 13:22:19.952480', '2024-02-25 13:22:19.952480', '71b7b389444043d583e939fba802d1f7', '2024-02-25', 'Invoice I-VW7IR91G6X account adjustment.', 'op', 'migration', 1, 1, NULL, 'f10a1fb314cf40a5a4d364b151b7a42b', NULL),
('2024-02-25 12:50:16.804955', '2024-02-25 12:50:16.804955', '76bbe24a89bc415eaee3c7b146d84ee9', '2024-02-25', 'Invoice I-VW7IR91G6X account adjustment.', 'op', 'migration', 1, 1, NULL, 'f10a1fb314cf40a5a4d364b151b7a42b', NULL),
('2024-02-25 13:43:09.565816', '2024-02-25 13:43:09.565816', '7860890c6282428982c075695ab0063a', '2024-02-25', 'Invoice I-VW7IR91G6X account adjustment.', 'op', 'migration', 1, 1, NULL, 'f10a1fb314cf40a5a4d364b151b7a42b', NULL),
('2024-02-25 13:46:15.258783', '2024-02-25 13:46:15.258783', '7ac118eddde247dba96007cadd92adfa', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 14:21:06.250632', '2024-02-25 14:21:06.250632', '7eaa21317cc043dd989e801562b4d381', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 02:56:34.160102', '2024-02-25 02:56:34.160102', '815ea037f3a14b04bc7670f7c15d0f47', '2024-02-25', 'Invoice I-VW7IR91G6X account adjustment.', 'op', 'migration', 1, 1, NULL, 'f10a1fb314cf40a5a4d364b151b7a42b', NULL),
('2024-02-25 13:34:31.809718', '2024-02-25 13:34:31.809718', '8aed655ceea04199945d622928b92fdf', '2024-02-25', 'Invoice I-VW7IR91G6X account adjustment.', 'op', 'migration', 1, 1, NULL, 'f10a1fb314cf40a5a4d364b151b7a42b', NULL),
('2024-02-25 13:55:44.085394', '2024-02-25 13:55:44.085394', '900b78c7ec7946a189118aeae70bcd7a', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-27 07:59:33.900562', '2024-02-27 07:59:33.900562', '93deb1535f6b4a69b31b2dfde2e61cd6', '2024-02-27', 'Bill B-X88Q8YMPJS account adjustment.', 'op', 'migration', 1, 1, '06c455e12a7f4d019f2bd779aee9a655', '1908708c1f40487fb93eb7c98370dc0a', NULL),
('2024-02-25 14:12:24.569699', '2024-02-25 14:12:24.569699', '9b1987f477b843dd89c4e96cea5c3ab6', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 03:04:23.220851', '2024-02-25 03:04:23.220851', '9d4565b063534582aa171da0f4f198bd', '2024-02-25', 'Invoice I-VW7IR91G6X account adjustment.', 'op', 'migration', 1, 1, NULL, 'f10a1fb314cf40a5a4d364b151b7a42b', NULL),
('2024-02-25 14:20:09.810232', '2024-02-25 14:20:09.810232', 'a02f888d754c4e1e897207f85032d4da', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2025-08-19 12:10:28.210459', '2025-08-19 12:10:28.210459', 'a2323731ecf144b28fca49aaa08a888f', '2025-08-19', 'Invoice I-4MLEIX9X6V account adjustment.', 'op', 'migration', 1, 1, NULL, '34f5c61f4abf44c5b64a4ea96435e4d0', NULL),
('2024-02-25 14:02:12.915398', '2024-02-25 14:02:12.915398', 'a575be288cf440ed90cead66a7ef522d', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 14:13:34.936056', '2024-02-25 14:13:34.936056', 'b9c80f828bd2462b91d4d7ad91910538', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 14:04:12.328461', '2024-02-25 14:04:12.328461', 'bc47b5e77ec04adb86a006e4f3cce865', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 01:53:00.180230', '2024-02-25 01:53:00.180230', 'beae4d5e6a2f46efbf3a6eecbb31427c', '2024-02-25', 'Bill B-8OSP8WGZ4P account adjustment.', 'op', 'migration', 1, 1, NULL, '838120708f9c4be88af1be7cddc17bc4', NULL),
('2024-02-25 13:29:41.588033', '2024-02-25 13:29:41.588033', 'bfb6aeb9955b4bc88dae7f1f3ac4a61a', '2024-02-25', 'Invoice I-VW7IR91G6X account adjustment.', 'op', 'migration', 1, 1, NULL, 'f10a1fb314cf40a5a4d364b151b7a42b', NULL),
('2025-08-19 12:06:43.042846', '2025-08-19 12:06:43.042846', 'bfe1f259691a4c02be49451117fcb0de', '2025-08-19', 'Invoice I-4MLEIX9X6V account adjustment.', 'op', 'migration', 1, 1, NULL, '34f5c61f4abf44c5b64a4ea96435e4d0', NULL),
('2024-02-25 14:19:41.252533', '2024-02-25 14:19:41.252533', 'c4e09037eb6e42ee8e2276e0a8bd1da8', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 13:03:37.703600', '2024-02-25 13:03:37.703600', 'c66d37a981514c49995b8b79128fb0b3', '2024-02-25', 'Invoice I-VW7IR91G6X account adjustment.', 'op', 'migration', 1, 1, NULL, 'f10a1fb314cf40a5a4d364b151b7a42b', NULL),
('2024-02-25 14:21:44.417794', '2024-02-25 14:21:44.417794', 'c719131b17bf4759ba91d528e0f55d2b', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 13:24:46.386385', '2024-02-25 13:24:46.386385', 'd0eba4f5b0404159890b01d20177d3b7', '2024-02-25', 'Invoice I-VW7IR91G6X account adjustment.', 'op', 'migration', 1, 1, NULL, 'f10a1fb314cf40a5a4d364b151b7a42b', NULL),
('2024-02-25 01:32:40.459249', '2024-02-25 01:32:40.459249', 'd0f324e495a245a484846aad5416b4b7', '2024-02-25', 'Bill B-8OSP8WGZ4P account adjustment.', 'op', 'migration', 1, 1, NULL, '838120708f9c4be88af1be7cddc17bc4', NULL),
('2024-02-25 13:32:58.937765', '2024-02-25 13:32:58.937765', 'd2f41c488e64472fa50c11e6d59dc13a', '2024-02-25', 'Invoice I-VW7IR91G6X account adjustment.', 'op', 'migration', 1, 1, NULL, 'f10a1fb314cf40a5a4d364b151b7a42b', NULL),
('2024-02-25 13:29:05.321263', '2024-02-25 13:29:05.321263', 'd5965ea06e174e8fbbc9a9735ddd194b', '2024-02-25', 'Invoice I-VW7IR91G6X account adjustment.', 'op', 'migration', 1, 1, NULL, 'f10a1fb314cf40a5a4d364b151b7a42b', NULL),
('2024-02-25 14:07:46.266947', '2024-02-25 14:07:46.266947', 'da654e3086cd49bf8d0077f8530eb824', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 01:07:42.863996', '2024-02-25 01:07:42.863996', 'e1331b2788f640749b32610d70f46b5b', '2024-02-25', 'Bill B-8OSP8WGZ4P account adjustment.', 'op', 'migration', 1, 1, NULL, '838120708f9c4be88af1be7cddc17bc4', NULL),
('2024-02-25 13:57:39.891591', '2024-02-25 13:57:39.891591', 'e47b9b62aafd45da98c10d4b7675f1c0', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 14:07:13.078183', '2024-02-25 14:07:13.078183', 'e51aca30bd504fb19500ca4eb58d0e3a', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 13:51:18.202817', '2024-02-25 13:51:18.202817', 'e9441775cf90428f954924fcf9a7475a', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 13:22:53.469638', '2024-02-25 13:22:53.469638', 'eb2725aeda38420c939e665f6dac6e2c', '2024-02-25', 'Invoice I-VW7IR91G6X account adjustment.', 'op', 'migration', 1, 1, NULL, 'f10a1fb314cf40a5a4d364b151b7a42b', NULL),
('2024-02-25 15:04:37.474340', '2024-02-25 15:04:37.474340', 'ed595bca7bc141aea62b36c3c9f2d3b3', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 14:16:16.610628', '2024-02-25 14:16:16.610628', 'f2cbe973828f403c896d6926f743169a', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 14:19:16.639658', '2024-02-25 14:19:16.639658', 'f8d14d846abb4ce29f9196b5b1f24b33', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 13:33:36.585534', '2024-02-25 13:33:36.585534', 'f90bec833dcc4a93a5cb9d944e9bc472', '2024-02-25', 'Invoice I-VW7IR91G6X account adjustment.', 'op', 'migration', 1, 1, NULL, 'f10a1fb314cf40a5a4d364b151b7a42b', NULL),
('2024-02-25 14:08:53.101595', '2024-02-25 14:08:53.101595', 'fbc473e019d343a68b25767a1e0e114d', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 13:49:34.383130', '2024-02-25 13:49:34.383130', 'fbfe7aed8d244bbdb8bed3a7aab8634c', '2024-02-25', 'Invoice I-RZQKJBF110 account adjustment.', 'op', 'migration', 1, 1, NULL, '26d0795227444e7fbdc6b8d8ad272a2f', NULL),
('2024-02-25 01:13:00.476127', '2024-02-25 01:13:00.476127', 'fd0bdea7ea4f41c9a0f553fa36b6d448', '2024-02-25', 'Bill B-8OSP8WGZ4P account adjustment.', 'op', 'migration', 1, 1, NULL, '838120708f9c4be88af1be7cddc17bc4', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `aix_kpihsemodel`
--

CREATE TABLE `aix_kpihsemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(255) NOT NULL,
  `activity_date` date NOT NULL,
  `start_time` time(6) NOT NULL,
  `end_time` time(6) NOT NULL,
  `fat` int(11) DEFAULT NULL,
  `lti` int(11) DEFAULT NULL,
  `rwdc` int(11) DEFAULT NULL,
  `mtc` int(11) DEFAULT NULL,
  `fac` int(11) DEFAULT NULL,
  `hipo` int(11) DEFAULT NULL,
  `envdam` int(11) DEFAULT NULL,
  `nmi` int(11) DEFAULT NULL,
  `matloss` int(11) DEFAULT NULL,
  `ptw` int(11) DEFAULT NULL,
  `ptw_description` longtext DEFAULT NULL,
  `tbt` int(11) DEFAULT NULL,
  `tbt_description` longtext DEFAULT NULL,
  `hht` int(11) DEFAULT NULL,
  `hht_description` longtext DEFAULT NULL,
  `drills` int(11) DEFAULT NULL,
  `drills_description` longtext DEFAULT NULL,
  `audit` int(11) DEFAULT NULL,
  `audit_description` longtext DEFAULT NULL,
  `training_subject` varchar(255) DEFAULT NULL,
  `reporting_cards` int(11) DEFAULT NULL,
  `rc_description` varchar(255) DEFAULT NULL,
  `safety_initiative` int(11) DEFAULT NULL,
  `si_description` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `entity_id` char(32) NOT NULL,
  `id` int(11) DEFAULT NULL,
  `Equipment` int(11) DEFAULT NULL,
  `duration` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_kpihsemodel`
--

INSERT INTO `aix_kpihsemodel` (`created`, `updated`, `uuid`, `code`, `activity_date`, `start_time`, `end_time`, `fat`, `lti`, `rwdc`, `mtc`, `fac`, `hipo`, `envdam`, `nmi`, `matloss`, `ptw`, `ptw_description`, `tbt`, `tbt_description`, `hht`, `hht_description`, `drills`, `drills_description`, `audit`, `audit_description`, `training_subject`, `reporting_cards`, `rc_description`, `safety_initiative`, `si_description`, `status`, `entity_id`, `id`, `Equipment`, `duration`) VALUES
('2024-02-21 08:18:07.923654', '2024-02-21 08:18:07.926223', '45214aab8cd34db9b8e5edda4306007e', 'HSE3ZNSHZRJ4V', '2024-01-10', '07:15:00.000000', '07:45:00.000000', 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 'NA', 1, 'NA', 1, 'NA', 1, 'NA', 1, 'NA', '1', 1, 'NA', 1, 'NA', 'progress', '1980d2af5ea14ad5b1e7712771f60517', NULL, NULL, 0),
('2024-02-21 05:54:17.100384', '2024-02-21 05:54:17.101102', 'e796388a933e4bc5b28cfe16f545208d', 'HSENAOJY7FM6W', '2024-01-09', '07:00:00.000000', '19:15:00.000000', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 'NA', 1, 'NA', 1, 'NA', 1, 'NA', 1, 'NA', '1', 1, '1', 1, '1', 'mobilizing', '1980d2af5ea14ad5b1e7712771f60517', NULL, NULL, 0);

-- --------------------------------------------------------

--
-- Table structure for table `aix_kpionoffmodel`
--

CREATE TABLE `aix_kpionoffmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(255) NOT NULL,
  `activity_date` date DEFAULT NULL,
  `activity_description` longtext DEFAULT NULL,
  `on_hire` varchar(255) DEFAULT NULL,
  `off_hire` varchar(255) DEFAULT NULL,
  `maintenance` varchar(255) DEFAULT NULL,
  `allocation` varchar(255) DEFAULT NULL,
  `comments` longtext DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `asset_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `location_id` char(32) NOT NULL,
  `id` int(11) DEFAULT NULL,
  `task_id` char(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_kpionoffmodel`
--

INSERT INTO `aix_kpionoffmodel` (`created`, `updated`, `uuid`, `code`, `activity_date`, `activity_description`, `on_hire`, `off_hire`, `maintenance`, `allocation`, `comments`, `status`, `asset_id`, `entity_id`, `location_id`, `id`, `task_id`) VALUES
('2024-03-21 06:14:43.405434', '2024-03-21 06:14:43.407909', '40852d11fae84a0596ffe886af021128', 'OFE43PMU0NYHY', '2024-02-07', 'NA', '07:00', '21:00', '5000 kms', 'SN', 'NA', 'Mobilizing', '5ae47e77932b11eea0b90a0027000102', '1980d2af5ea14ad5b1e7712771f60517', '08cc8d74f3144bf2bff818aefc69b745', NULL, '144288f8325b4f66946f864e4bcbf970');

-- --------------------------------------------------------

--
-- Table structure for table `aix_kpiopsmodel`
--

CREATE TABLE `aix_kpiopsmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(255) NOT NULL,
  `activity_date` date DEFAULT NULL,
  `activity_description` longtext DEFAULT NULL,
  `trip_activity` int(11) NOT NULL,
  `trip_code` varchar(255) DEFAULT NULL,
  `etd` varchar(255) DEFAULT NULL,
  `eta` varchar(255) DEFAULT NULL,
  `atd` varchar(255) DEFAULT NULL,
  `ata` varchar(255) DEFAULT NULL,
  `activity_time` varchar(255) DEFAULT NULL,
  `kms_passed` double DEFAULT NULL,
  `consol_fuel` double DEFAULT NULL,
  `operator` double DEFAULT NULL,
  `banksman` double DEFAULT NULL,
  `rigger1` double DEFAULT NULL,
  `rigger2` double DEFAULT NULL,
  `rigger3` double DEFAULT NULL,
  `rigger4` decimal(11,0) DEFAULT NULL,
  `section2_description` varchar(255) DEFAULT NULL,
  `section2_time_taken` double DEFAULT NULL,
  `section2_ton_cargo` double DEFAULT NULL,
  `section2_number_lifts` double DEFAULT NULL,
  `section2_ton_lifts` double DEFAULT NULL,
  `no_routine` double DEFAULT NULL,
  `no_simple` double DEFAULT NULL,
  `no_complicated` double DEFAULT NULL,
  `no_complex` double DEFAULT NULL,
  `ton_routine` double DEFAULT NULL,
  `ton_simple` double DEFAULT NULL,
  `ton_complicated` double DEFAULT NULL,
  `ton_complex` double DEFAULT NULL,
  `section3_description` varchar(255) DEFAULT NULL,
  `section3_time_taken` double DEFAULT NULL,
  `section3_ton_cargo` double DEFAULT NULL,
  `section3_number_lifts` double DEFAULT NULL,
  `section3_ton_lifts` double DEFAULT NULL,
  `llt_dsb` double DEFAULT NULL,
  `llt_tgi` double DEFAULT NULL,
  `llt_rig1` double DEFAULT NULL,
  `llt_rig2` double DEFAULT NULL,
  `llt_rig3` double DEFAULT NULL,
  `llt_other` double DEFAULT NULL,
  `tlt_dsb` double DEFAULT NULL,
  `tlt_tgi` double DEFAULT NULL,
  `tlt_rig1` double DEFAULT NULL,
  `tlt_rig2` double DEFAULT NULL,
  `tlt_rig3` double DEFAULT NULL,
  `tlt_other` double DEFAULT NULL,
  `dnt_dsb` double DEFAULT NULL,
  `dnt_tgi` double DEFAULT NULL,
  `dnt_rig1` double DEFAULT NULL,
  `dnt_rig2` double DEFAULT NULL,
  `dnt_rig3` double DEFAULT NULL,
  `dnt_other` double DEFAULT NULL,
  `reason` varchar(255) DEFAULT NULL,
  `comments` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `entity_id` char(32) NOT NULL,
  `FromLocation` char(32) DEFAULT NULL,
  `task_id` char(32) NOT NULL,
  `ToLocation` char(32) DEFAULT NULL,
  `id` int(11) DEFAULT NULL,
  `equipment_id` char(32) NOT NULL,
  `atp` double DEFAULT NULL,
  `etp` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_kpiopsmodel`
--

INSERT INTO `aix_kpiopsmodel` (`created`, `updated`, `uuid`, `code`, `activity_date`, `activity_description`, `trip_activity`, `trip_code`, `etd`, `eta`, `atd`, `ata`, `activity_time`, `kms_passed`, `consol_fuel`, `operator`, `banksman`, `rigger1`, `rigger2`, `rigger3`, `rigger4`, `section2_description`, `section2_time_taken`, `section2_ton_cargo`, `section2_number_lifts`, `section2_ton_lifts`, `no_routine`, `no_simple`, `no_complicated`, `no_complex`, `ton_routine`, `ton_simple`, `ton_complicated`, `ton_complex`, `section3_description`, `section3_time_taken`, `section3_ton_cargo`, `section3_number_lifts`, `section3_ton_lifts`, `llt_dsb`, `llt_tgi`, `llt_rig1`, `llt_rig2`, `llt_rig3`, `llt_other`, `tlt_dsb`, `tlt_tgi`, `tlt_rig1`, `tlt_rig2`, `tlt_rig3`, `tlt_other`, `dnt_dsb`, `dnt_tgi`, `dnt_rig1`, `dnt_rig2`, `dnt_rig3`, `dnt_other`, `reason`, `comments`, `status`, `entity_id`, `FromLocation`, `task_id`, `ToLocation`, `id`, `equipment_id`, `atp`, `etp`) VALUES
('2025-08-20 09:08:57.995653', '2025-08-20 09:08:57.995653', '988f6eb0198f4af1a3b6caa992ff2aa5', 'OPS5ZL637V82P', '2024-10-02', 'Lift 3 Gentex 4K generators from section A to section B', 1, '8bbde949-3eb8-4330-98aa-53734f29388f', '07:00', '08:00', '07:14', '15:00', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'New', '94a77b664b5d4efab801ba8560d83fc8', 'd5370a8957ed4f79a0bbf47e931b06d9', '8bbde9493eb8433098aa53734f29388f', 'd5370a8957ed4f79a0bbf47e931b06d9', NULL, '5ae47e77932b11eea0b90a0027000102', 58440, 82800);

-- --------------------------------------------------------

--
-- Table structure for table `aix_kpipobmodel`
--

CREATE TABLE `aix_kpipobmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(255) NOT NULL,
  `activity_date` date DEFAULT NULL,
  `activity_description` longtext DEFAULT NULL,
  `category` int(11) DEFAULT NULL,
  `activity_location_id` char(32) NOT NULL,
  `allocation` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `entity_id` char(32) NOT NULL,
  `rotation1` char(32) DEFAULT NULL,
  `rotation2` char(32) DEFAULT NULL,
  `rotation3` char(32) DEFAULT NULL,
  `id` int(11) DEFAULT NULL,
  `Equipment` int(11) DEFAULT NULL,
  `group_code` varchar(100) DEFAULT NULL,
  `task_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_kpipobmodel`
--

INSERT INTO `aix_kpipobmodel` (`created`, `updated`, `uuid`, `code`, `activity_date`, `activity_description`, `category`, `activity_location_id`, `allocation`, `status`, `entity_id`, `rotation1`, `rotation2`, `rotation3`, `id`, `Equipment`, `group_code`, `task_id`) VALUES
('2024-03-21 06:52:48.331994', '2024-03-21 07:08:30.536779', '2d5aa55c87194cd5b90e5040c6bac178', 'POBUVNFNNIKKX', '2024-01-10', 'NA', NULL, '08cc8d74f3144bf2bff818aefc69b745', 'SN', 'Progress', '1980d2af5ea14ad5b1e7712771f60517', '3ec26bd94d0540348a4bfa95926bfa99', '3ec26bd94d0540348a4bfa95926bfa99', '3ec26bd94d0540348a4bfa95926bfa99', NULL, NULL, NULL, '144288f8325b4f66946f864e4bcbf970'),
('2024-03-21 07:04:27.745991', '2024-03-21 07:07:57.969114', 'f40ddbbd870045dd98a30c6a918bf666', 'POB4UO1F21MHW', '2024-02-05', 'NA', NULL, '08cc8d74f3144bf2bff818aefc69b745', 'SN', 'New', '1980d2af5ea14ad5b1e7712771f60517', '3ec26bd94d0540348a4bfa95926bfa99', '3ec26bd94d0540348a4bfa95926bfa99', '3ec26bd94d0540348a4bfa95926bfa99', NULL, NULL, NULL, '144288f8325b4f66946f864e4bcbf970');

-- --------------------------------------------------------

--
-- Table structure for table `aix_languagemodel`
--

CREATE TABLE `aix_languagemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_leavecardcarriedovermodel`
--

CREATE TABLE `aix_leavecardcarriedovermodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `days` double NOT NULL,
  `absence_type_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `leave_card_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_leavecarddetailmodel`
--

CREATE TABLE `aix_leavecarddetailmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `credit` double NOT NULL,
  `days_used` double NOT NULL,
  `days_advanced` double NOT NULL,
  `balance` double NOT NULL,
  `year` int(11) NOT NULL,
  `month` int(11) NOT NULL,
  `absence_type_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `leave_card_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_leavecardmodel`
--

CREATE TABLE `aix_leavecardmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `is_dirty` tinyint(1) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_leaverequestactionmodel`
--

CREATE TABLE `aix_leaverequestactionmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `comment` varchar(100) NOT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `leave_request_id` char(32) NOT NULL,
  `leave_request_status_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_leaverequestdetailmodel`
--

CREATE TABLE `aix_leaverequestdetailmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `total_calendar_days_requested` double NOT NULL,
  `total_work_days_requested` double NOT NULL,
  `half_day_used` longtext NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `absence_type_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `leave_request_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_leaverequestmodel`
--

CREATE TABLE `aix_leaverequestmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `number` varchar(255) NOT NULL,
  `contact_phone` varchar(255) DEFAULT NULL,
  `contact_email` varchar(255) DEFAULT NULL,
  `remarks` varchar(255) DEFAULT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `leave_request_status_id` char(32) NOT NULL,
  `supervisor_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_leaverequeststatusmodel`
--

CREATE TABLE `aix_leaverequeststatusmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_leaverequestworkflowactionmodel`
--

CREATE TABLE `aix_leaverequestworkflowactionmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `is_processed` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `entity_id` char(32) NOT NULL,
  `leave_request_action_id` char(32) NOT NULL,
  `workflow_id` char(32) NOT NULL,
  `workflow_action_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_leaverequestworkflowmodel`
--

CREATE TABLE `aix_leaverequestworkflowmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `leave_request_id` char(32) NOT NULL,
  `workflow_id` char(32) NOT NULL,
  `workflow_status_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_ledgermodel`
--

CREATE TABLE `aix_ledgermodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `name` varchar(150) DEFAULT NULL,
  `posted` tinyint(1) NOT NULL,
  `locked` tinyint(1) NOT NULL,
  `hidden` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_ledgermodel`
--

INSERT INTO `aix_ledgermodel` (`created`, `updated`, `uuid`, `name`, `posted`, `locked`, `hidden`, `entity_id`) VALUES
('2024-02-27 07:59:33.881271', '2024-02-27 07:59:33.881271', '1908708c1f40487fb93eb7c98370dc0a', 'Bill B-X88Q8YMPJS', 0, 0, 0, '1980d2af5ea14ad5b1e7712771f60517'),
('2024-02-25 02:55:53.766199', '2024-02-25 13:49:08.161619', '26d0795227444e7fbdc6b8d8ad272a2f', 'Invoice I-RZQKJBF110', 1, 0, 0, '1980d2af5ea14ad5b1e7712771f60517'),
('2025-08-19 12:06:42.975988', '2025-08-19 12:09:57.838708', '34f5c61f4abf44c5b64a4ea96435e4d0', 'Invoice I-4MLEIX9X6V', 1, 0, 0, '94a77b664b5d4efab801ba8560d83fc8'),
('2024-02-25 02:49:00.404491', '2024-02-25 02:49:00.404491', '38f899c22d4b4b4da4274db9b394f16a', 'Invoice I-G9K09K5VF1', 0, 0, 0, '1980d2af5ea14ad5b1e7712771f60517'),
('2024-02-25 02:51:49.323742', '2024-02-25 02:51:49.323742', '834f115c310f43cdbc84c579b04cca95', 'Invoice I-L40W8I13HP', 0, 0, 0, '1980d2af5ea14ad5b1e7712771f60517'),
('2024-02-25 01:07:42.823861', '2024-02-25 01:32:40.474905', '838120708f9c4be88af1be7cddc17bc4', 'Bill B-8OSP8WGZ4P', 1, 0, 0, '1980d2af5ea14ad5b1e7712771f60517'),
('2024-08-28 08:29:25.529162', '2024-08-28 08:29:25.529162', '89fccf846ef947249648d79ad0ee7ae7', 'Threeways General Ledger', 1, 0, 0, '94a77b664b5d4efab801ba8560d83fc8'),
('2024-02-24 02:37:03.323817', '2024-02-24 02:37:03.323817', 'b58cad63f1e141c49b2116ec2d9c34c4', 'Total Uganda General Ledger', 1, 0, 0, '1980d2af5ea14ad5b1e7712771f60517'),
('2024-02-25 02:56:34.135604', '2024-02-27 06:05:53.126735', 'f10a1fb314cf40a5a4d364b151b7a42b', 'Invoice I-VW7IR91G6X', 1, 1, 0, '1980d2af5ea14ad5b1e7712771f60517');

-- --------------------------------------------------------

--
-- Table structure for table `aix_locationmodel`
--

CREATE TABLE `aix_locationmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_maritalstatusmodel`
--

CREATE TABLE `aix_maritalstatusmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_nationmodel`
--

CREATE TABLE `aix_nationmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_nationmodel`
--

INSERT INTO `aix_nationmodel` (`created`, `updated`, `uuid`, `code`, `name`, `description`, `is_active`, `entity_id`) VALUES
('2024-02-24 16:37:56.968198', '2024-02-24 16:37:56.972954', '0d20e8bab74e4d9cab6c3037bb415ebc', 'UG', 'Uganda', 'Uganda', 1, '1980d2af5ea14ad5b1e7712771f60517'),
('2025-08-11 13:19:49.844322', '2025-08-11 13:19:49.860994', '5d445315e0cc4b0381005c85ed62e318', 'KE', 'Kenya', 'Kenya', 1, '94a77b664b5d4efab801ba8560d83fc8'),
('2024-02-24 16:38:14.588623', '2024-02-24 16:38:14.590641', '6b6f160cdd0e4836a05686329a198b91', 'KE', 'Kenya', 'Kenya', 1, '1980d2af5ea14ad5b1e7712771f60517'),
('2025-08-11 13:20:08.795445', '2025-08-11 13:20:08.798228', 'c32bf77ac16e4a52be88563b851bf56b', 'TZ', 'Tanzania', 'Tanzania', 1, '94a77b664b5d4efab801ba8560d83fc8'),
('2025-08-11 13:19:36.850406', '2025-08-11 13:19:36.863880', 'cf6b306ae294482e8d2410dbcdde95ff', 'UG', 'Uganda', 'Uganda', 1, '94a77b664b5d4efab801ba8560d83fc8');

-- --------------------------------------------------------

--
-- Table structure for table `aix_notificationexternaltypemodel`
--

CREATE TABLE `aix_notificationexternaltypemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_notificationmodel`
--

CREATE TABLE `aix_notificationmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `params` longtext DEFAULT NULL,
  `is_read` tinyint(1) NOT NULL,
  `is_processed` tinyint(1) NOT NULL,
  `channel` int(11) NOT NULL,
  `external_type_key` int(11) NOT NULL,
  `notify_on` date NOT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `notification_external_type_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_notificationtrackermodel`
--

CREATE TABLE `aix_notificationtrackermodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `next_notification` date NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_paymentmodemodel`
--

CREATE TABLE `aix_paymentmodemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_payrolladvancemodel`
--

CREATE TABLE `aix_payrolladvancemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `period` int(11) NOT NULL,
  `amount` longtext NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_payrolladvancerequestactionmodel`
--

CREATE TABLE `aix_payrolladvancerequestactionmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `comment` varchar(100) NOT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `pa_request_id` char(32) NOT NULL,
  `par_status_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_payrolladvancerequestdetailmodel`
--

CREATE TABLE `aix_payrolladvancerequestdetailmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `period` int(11) NOT NULL,
  `amount` longtext NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `entity_id` char(32) NOT NULL,
  `pa_request_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_payrolladvancerequestmodel`
--

CREATE TABLE `aix_payrolladvancerequestmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `number` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `remarks` varchar(255) DEFAULT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `par_status_id` char(32) NOT NULL,
  `supervisor_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_payrolladvancerequeststatusmodel`
--

CREATE TABLE `aix_payrolladvancerequeststatusmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_payrolladvancerequestworkflowactionmodel`
--

CREATE TABLE `aix_payrolladvancerequestworkflowactionmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `is_processed` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `par_action_id` char(32) NOT NULL,
  `par_workflow_id` char(32) NOT NULL,
  `workflow_action_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_payrolladvancerequestworkflowmodel`
--

CREATE TABLE `aix_payrolladvancerequestworkflowmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `pa_request_id` char(32) NOT NULL,
  `workflow_id` char(32) NOT NULL,
  `workflow_status_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_purchaseordermodel`
--

CREATE TABLE `aix_purchaseordermodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `markdown_notes` longtext DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `po_number` varchar(20) NOT NULL,
  `po_date` date DEFAULT NULL,
  `po_title` varchar(250) NOT NULL,
  `po_module` varchar(10) NOT NULL,
  `po_status` varchar(10) NOT NULL,
  `po_amount` decimal(20,2) NOT NULL,
  `po_amount_received` decimal(20,2) NOT NULL,
  `draft_date` date DEFAULT NULL,
  `in_review_date` date DEFAULT NULL,
  `approved_date` date DEFAULT NULL,
  `void_date` date DEFAULT NULL,
  `fulfillment_date` date DEFAULT NULL,
  `canceled_date` date DEFAULT NULL,
  `ce_model_id` char(32) DEFAULT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_purchaseordermodel`
--

INSERT INTO `aix_purchaseordermodel` (`created`, `updated`, `markdown_notes`, `uuid`, `po_number`, `po_date`, `po_title`, `po_module`, `po_status`, `po_amount`, `po_amount_received`, `draft_date`, `in_review_date`, `approved_date`, `void_date`, `fulfillment_date`, `canceled_date`, `ce_model_id`, `entity_id`) VALUES
('2024-02-27 07:53:29.433106', '2024-02-27 07:58:27.129034', 'For 3 personnel to be engaged in the field', '349b75ce8086421e952b35cc05559751', 'PO-4AN5WA4ZSH', '2024-02-07', 'Request for Safety Gear', '', 'approved', '810000.00', '0.00', NULL, '2024-02-27', '2024-02-27', NULL, NULL, NULL, NULL, '1980d2af5ea14ad5b1e7712771f60517'),
('2024-02-23 23:41:28.144212', '2024-02-27 07:51:20.052352', 'There is a rig move site survey at the DSB operation area. This fuel will facilitate 5 cars for this exercise.', '38da982bc8ce4d6b9f4b09d58e16a291', 'PO-E5FZQQ6BFQ', '2023-12-13', 'Facilitate Site Survey new Rig at DSB', 'fuel', 'approved', '450850.00', '0.00', NULL, '2024-02-25', '2024-02-25', NULL, NULL, NULL, NULL, '1980d2af5ea14ad5b1e7712771f60517');

-- --------------------------------------------------------

--
-- Table structure for table `aix_qualificationmodel`
--

CREATE TABLE `aix_qualificationmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_receivedemaildocumentmodel`
--

CREATE TABLE `aix_receivedemaildocumentmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `doc_from` longtext NOT NULL,
  `doc_subject` longtext NOT NULL,
  `doc_body` longtext NOT NULL,
  `processed` int(11) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_relationshipmodel`
--

CREATE TABLE `aix_relationshipmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_reportmodel`
--

CREATE TABLE `aix_reportmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `rpt_name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `sort_by` longtext DEFAULT NULL,
  `order_by` longtext DEFAULT NULL,
  `order_by_dir` longtext DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_reportmodel`
--

INSERT INTO `aix_reportmodel` (`created`, `updated`, `uuid`, `code`, `rpt_name`, `description`, `sort_by`, `order_by`, `order_by_dir`, `is_active`, `entity_id`) VALUES
('2024-01-25 12:29:05.912573', '2024-01-25 12:29:05.916153', '65bf845d90e548a6b23755c9822d88bc', 'NA', 'Main Dashboard', 'Main Dashboard', '', '', 'ASC', 1, '1980d2af5ea14ad5b1e7712771f60517');

-- --------------------------------------------------------

--
-- Table structure for table `aix_requisitionactionmodel`
--

CREATE TABLE `aix_requisitionactionmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `comment` varchar(100) NOT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `requisition_id` char(32) NOT NULL,
  `requisition_status_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_requisitioncategorymodel`
--

CREATE TABLE `aix_requisitioncategorymodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_requisitioncategorymodel`
--

INSERT INTO `aix_requisitioncategorymodel` (`created`, `updated`, `uuid`, `code`, `name`, `description`, `is_active`, `entity_id`) VALUES
('2024-09-02 06:42:31.845202', '2024-09-02 06:42:31.847201', '8b7fd3d0d51e4a57aa79ab27f8ba079e', 'NA', 'General Request', 'General Request for Items', 1, '94a77b664b5d4efab801ba8560d83fc8');

-- --------------------------------------------------------

--
-- Table structure for table `aix_requisitionflowtypemodel`
--

CREATE TABLE `aix_requisitionflowtypemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_requisitionmodel`
--

CREATE TABLE `aix_requisitionmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `date` date NOT NULL,
  `number` varchar(255) NOT NULL,
  `amount` longtext NOT NULL,
  `payout_amount` longtext NOT NULL,
  `description` longtext DEFAULT NULL,
  `currency_id` char(32) NOT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `requisition_category_id` char(32) NOT NULL,
  `requisition_status_id` char(32) NOT NULL,
  `supervisor_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_requisitionstatusmodel`
--

CREATE TABLE `aix_requisitionstatusmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_requisitionworkflowactionmodel`
--

CREATE TABLE `aix_requisitionworkflowactionmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `is_processed` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `requisition_action_id` char(32) NOT NULL,
  `workflow_id` char(32) NOT NULL,
  `workflow_action_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_requisitionworkflowmodel`
--

CREATE TABLE `aix_requisitionworkflowmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `requisition_id` char(32) NOT NULL,
  `workflow_id` char(32) NOT NULL,
  `workflow_status_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_routesurveyinfomodel`
--

CREATE TABLE `aix_routesurveyinfomodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `route_code` varchar(100) NOT NULL,
  `south_coordinate` varchar(63) NOT NULL,
  `east_coordinate` varchar(63) NOT NULL,
  `distance_start` varchar(100) NOT NULL,
  `color` varchar(50) NOT NULL,
  `koc` varchar(50) NOT NULL,
  `kfi_description` longtext DEFAULT NULL,
  `photo` varchar(100) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `route_survey_id` char(32) NOT NULL,
  `location` varchar(63) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_routesurveyinfomodel`
--

INSERT INTO `aix_routesurveyinfomodel` (`created`, `updated`, `uuid`, `code`, `route_code`, `south_coordinate`, `east_coordinate`, `distance_start`, `color`, `koc`, `kfi_description`, `photo`, `is_active`, `entity_id`, `route_survey_id`, `location`) VALUES
('2025-07-28 08:14:38.656692', '2025-07-28 08:14:38.658698', '5c49440feb6c42d0b2cce23ab51476b6', '', '1234', '2025-07-07', '2025-07-15', '30', 'RED', 'AMBER', 'NA1', 'NA2', 1, '94a77b664b5d4efab801ba8560d83fc8', '4dd48ffe656848659b70b5d719fa4f38', ''),
('2025-07-28 08:16:55.737665', '2025-07-28 08:16:55.738965', '63cbc8c5c3bf434ca7bca189deb64954', '', '12345', '2025-07-07', '2025-07-10', '27', 'GREEN', 'AMBER', 'NA', 'NA', 1, '94a77b664b5d4efab801ba8560d83fc8', '4dd48ffe656848659b70b5d719fa4f38', ''),
('2025-08-19 09:10:15.085411', '2025-08-19 09:10:15.090826', '67367836b09c4edf83c6004645d589f8', '', '0024', '-0.6701507351859187,-1.3183593750000002', '-0.14282211771737158,-0.12084960937500001', '40', 'GREEN', 'AMBER', 'NA', '', 1, '94a77b664b5d4efab801ba8560d83fc8', '12191dbe7a2643609f299e6265970630', ''),
('2025-07-29 09:43:56.123369', '2025-07-29 09:43:56.125367', '772e13d17cec411388319022dd86380f', '', '002', '2025-07-13', '2025-07-19', '100', 'RED', 'GREEN', 'ALTERNATE EXIT AT GATE 18\r\n•	The approach to the alternate exit has some features that could pose a challenge to a long load\r\n•	There are gate accesses along the alternate exit\r\n•	There is a new road being made for the new exit gate so that trucks proceed straight and don’t have to turn upwards\r\n•	The road surface shall require a lot of work to provide level and good traction', '', 1, '94a77b664b5d4efab801ba8560d83fc8', '12191dbe7a2643609f299e6265970630', ''),
('2025-07-29 09:41:03.178667', '2025-07-29 09:41:03.187673', 'fc556f71efe647f28263d7ff8ea62121', '', '002', '2025-07-07', '2025-07-12', '50', 'GREEN', 'AMBER', 'MOMBASA PORT BERTH 18 AND 19 \r\n•	Draft is 10.36 meters \r\n•	 Surface of quayside appears to be worn and damaged. May require matting all across\r\n•	Full structural Survey required', 'http://', 1, '94a77b664b5d4efab801ba8560d83fc8', '4dd48ffe656848659b70b5d719fa4f38', '');

-- --------------------------------------------------------

--
-- Table structure for table `aix_routesurveymodel`
--

CREATE TABLE `aix_routesurveymodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `start_place` varchar(200) NOT NULL,
  `via_place` varchar(200) NOT NULL,
  `end_place` varchar(200) NOT NULL,
  `start_gps` varchar(63) NOT NULL,
  `via_gps` varchar(63) NOT NULL,
  `end_gps` varchar(63) NOT NULL,
  `purpose` longtext DEFAULT NULL,
  `general_notes` longtext DEFAULT NULL,
  `bo1` longtext DEFAULT NULL,
  `bo2` longtext DEFAULT NULL,
  `bo3` longtext DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `location` varchar(63) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_routesurveymodel`
--

INSERT INTO `aix_routesurveymodel` (`created`, `updated`, `uuid`, `code`, `name`, `start_date`, `end_date`, `start_place`, `via_place`, `end_place`, `start_gps`, `via_gps`, `end_gps`, `purpose`, `general_notes`, `bo1`, `bo2`, `bo3`, `is_active`, `entity_id`, `location`) VALUES
('2025-07-28 09:46:13.754419', '2025-07-28 09:46:13.756508', '12191dbe7a2643609f299e6265970630', 'RSV9E80K', 'North Nile Valley', '2025-07-14', '2025-07-24', '0.564138900949037,-0.41198730468750006', '0.012268423940367885,1.4776611328125002', '-0.05383293283686332,-0.5438232421875001', '0.564138900949037,-0.41198730468750006', '0.012268423940367885,1.4776611328125002', '-0.05383293283686332,-0.5438232421875001', '', NULL, '', '', '', 1, '94a77b664b5d4efab801ba8560d83fc8', '-0.02252183796581134,0.8953857421875001'),
('2025-07-28 06:22:18.246600', '2025-07-28 06:22:18.261010', '4dd48ffe656848659b70b5d719fa4f38', 'RSV75PU5', 'Pakwach Strech', '2025-07-20', '2025-07-25', 'KAMPALA', 'MASAKA', 'HOIMA', '10.99583880079938,14.095458984375002', '0.6811362994451233,31.728515625000004', '1.8014609294680355,31.442871093750004', '', 'NA', '', '', '', 1, '94a77b664b5d4efab801ba8560d83fc8', '1.5818302639606454,31.');

-- --------------------------------------------------------

--
-- Table structure for table `aix_salarymodel`
--

CREATE TABLE `aix_salarymodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `basic_pay` longtext NOT NULL,
  `description` longtext DEFAULT NULL,
  `currency_id` char(32) NOT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_skillmodel`
--

CREATE TABLE `aix_skillmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `name` varchar(100) NOT NULL,
  `comment` longtext DEFAULT NULL,
  `years_of_experience` double NOT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_stagedtransactionmodel`
--

CREATE TABLE `aix_stagedtransactionmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `fitid` varchar(100) NOT NULL,
  `amount` decimal(15,2) NOT NULL,
  `date_posted` date NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `memo` varchar(200) DEFAULT NULL,
  `earnings_account_id` char(32) DEFAULT NULL,
  `import_job_id` char(32) NOT NULL,
  `tx_id` char(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_taskassigneemodel`
--

CREATE TABLE `aix_taskassigneemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `task_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_taskmodel`
--

CREATE TABLE `aix_taskmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `task_name` varchar(255) NOT NULL,
  `description` longtext DEFAULT NULL,
  `case_status` varchar(255) NOT NULL,
  `due_at` date NOT NULL,
  `end_date` date DEFAULT NULL,
  `estimated_time` varchar(255) DEFAULT NULL,
  `entity_id` char(32) NOT NULL,
  `task_status_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_taskstatusmodel`
--

CREATE TABLE `aix_taskstatusmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_taxmodel`
--

CREATE TABLE `aix_taxmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `rate` int(11) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_transactionmodel`
--

CREATE TABLE `aix_transactionmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `tx_type` varchar(10) NOT NULL,
  `amount` decimal(20,2) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `account_id` char(32) NOT NULL,
  `journal_entry_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_transactionmodel`
--

INSERT INTO `aix_transactionmodel` (`created`, `updated`, `uuid`, `tx_type`, `amount`, `description`, `account_id`, `journal_entry_id`) VALUES
('2024-02-27 08:02:33.937557', '2024-02-27 08:02:33.937557', '0a45efa8ba06484a8f908bad7ccf30bb', 'debit', '0.00', NULL, '6fe4fe62eba44a3bbf5ca23fdd2c5ae5', '59f0d7ff4fdd42a682291f9e50eb1775'),
('2024-02-25 01:53:00.183865', '2024-02-25 01:53:00.183865', '0a5a0a586c69473fb84d2df58ec4f12f', 'credit', '52000.00', 'Bill B-8OSP8WGZ4P account adjustment.', '6fe4fe62eba44a3bbf5ca23fdd2c5ae5', 'beae4d5e6a2f46efbf3a6eecbb31427c'),
('2024-02-25 01:32:40.470941', '2024-02-25 01:32:40.470941', '3bcb73ad82584f82b5f0dce19f6f6c82', 'credit', '451080.00', 'Bill B-8OSP8WGZ4P account adjustment.', '6fe4fe62eba44a3bbf5ca23fdd2c5ae5', 'd0f324e495a245a484846aad5416b4b7'),
('2024-02-25 15:42:14.287799', '2024-02-25 15:42:14.287799', '4b5b9daddd5a4251b83a35e598adbf84', 'debit', '70000.00', NULL, '6fe4fe62eba44a3bbf5ca23fdd2c5ae5', '5e4d577e398c40128899731181cbd8fe'),
('2025-08-19 12:10:28.217010', '2025-08-19 12:10:28.217010', '4fd97f08cb6a463e95c48af3e40ef3d4', 'debit', '370.00', NULL, '6fe4fe62eba44a3bbf5ca23fdd2c5ae5', 'a2323731ecf144b28fca49aaa08a888f'),
('2025-08-19 12:07:53.433059', '2025-08-19 12:07:53.433059', '5fe9f539ab7a43daa09d8c0e98f53693', 'debit', '0.00', NULL, '6fe4fe62eba44a3bbf5ca23fdd2c5ae5', '2828d9d5df844126be2c4d8ba639de0c'),
('2024-02-25 15:04:37.479323', '2024-02-25 15:04:37.479323', '69de0ba4afaf4584bf7aa58805412e66', 'debit', '50000.00', NULL, '6fe4fe62eba44a3bbf5ca23fdd2c5ae5', 'ed595bca7bc141aea62b36c3c9f2d3b3'),
('2024-02-25 01:53:00.183865', '2024-02-25 01:53:00.183865', 'a3d63e30294f4c81b1e1315d1e8295a0', 'debit', '52000.00', 'Bill B-8OSP8WGZ4P account adjustment.', '100846fca4c34f5684593663d3c530ea', 'beae4d5e6a2f46efbf3a6eecbb31427c'),
('2025-08-19 12:06:43.051921', '2025-08-19 12:06:43.051921', 'b277f6d4c9c44d5e805c55bf745b6229', 'debit', '0.00', NULL, '6fe4fe62eba44a3bbf5ca23fdd2c5ae5', 'bfe1f259691a4c02be49451117fcb0de'),
('2024-02-25 01:34:32.647403', '2024-02-25 01:34:32.647403', 'b9ac4c5a31df47aab9828f8d7da36060', 'credit', '301080.00', 'Bill B-8OSP8WGZ4P account adjustment.', '100846fca4c34f5684593663d3c530ea', '62c4473ebad545f3bf418e3174f5d4ac'),
('2024-02-25 01:34:32.647403', '2024-02-25 01:34:32.647403', 'c290aa9ba5994fbd9d6188d940ed81a8', 'debit', '301080.00', 'Bill B-8OSP8WGZ4P account adjustment.', '6fe4fe62eba44a3bbf5ca23fdd2c5ae5', '62c4473ebad545f3bf418e3174f5d4ac'),
('2025-08-19 12:08:38.399916', '2025-08-19 12:08:38.399916', 'ca17bd375a064c1bbe2d16e19d45d61c', 'debit', '0.00', NULL, '6fe4fe62eba44a3bbf5ca23fdd2c5ae5', '1107435ca6f048ed94b0c9f1d0f60424'),
('2024-02-27 06:05:53.117736', '2024-02-27 06:05:53.117736', 'de2959284e9f4416bc076f91c6af0f61', 'debit', '17150000.00', NULL, '6fe4fe62eba44a3bbf5ca23fdd2c5ae5', '2f1eb0a36bbc4885a1ba71a921a1ae4a'),
('2024-02-25 14:21:44.421321', '2024-02-25 14:21:44.421321', 'e6729a222d394f11a765aab83b9974f8', 'debit', '130000.00', NULL, '6fe4fe62eba44a3bbf5ca23fdd2c5ae5', 'c719131b17bf4759ba91d528e0f55d2b'),
('2024-02-27 07:59:33.905237', '2024-02-27 07:59:33.905237', 'f3453483acd941ef9a22ac1f2be9298a', 'debit', '0.00', NULL, '6fe4fe62eba44a3bbf5ca23fdd2c5ae5', '93deb1535f6b4a69b31b2dfde2e61cd6'),
('2024-02-25 01:32:40.470941', '2024-02-25 01:32:40.470941', 'faba3d9a522a4967a75a56243480802e', 'debit', '451080.00', 'Bill B-8OSP8WGZ4P account adjustment.', '100846fca4c34f5684593663d3c530ea', 'd0f324e495a245a484846aad5416b4b7');

-- --------------------------------------------------------

--
-- Table structure for table `aix_unitofmeasuremodel`
--

CREATE TABLE `aix_unitofmeasuremodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `name` varchar(50) NOT NULL,
  `unit_abbr` varchar(10) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_unitofmeasuremodel`
--

INSERT INTO `aix_unitofmeasuremodel` (`created`, `updated`, `uuid`, `name`, `unit_abbr`, `is_active`, `entity_id`) VALUES
('2025-08-11 13:37:59.351782', '2025-08-11 13:37:59.356309', '7cc241d06daa402da851d7d4f65935a7', 'LTR', 'Litres', 1, '94a77b664b5d4efab801ba8560d83fc8'),
('2024-02-23 23:19:44.343232', '2024-02-23 23:19:44.347291', '829569dcbb8343bf9ccdcf7b31054c61', 'Liters', 'Ltr', 1, '1980d2af5ea14ad5b1e7712771f60517'),
('2025-08-11 13:37:46.664740', '2025-08-11 13:37:46.668761', '8875a0d1eecd4bd3b846d08d1e975592', 'KG', 'Kilogram', 1, '94a77b664b5d4efab801ba8560d83fc8'),
('2024-02-23 23:19:58.918391', '2024-02-23 23:19:58.920790', 'a85e665acca5476d9f7a22197c3b1869', 'Kilogram', 'Kg', 1, '1980d2af5ea14ad5b1e7712771f60517'),
('2024-02-23 23:20:14.547491', '2024-02-23 23:20:14.550489', 'dffb447d188c4415bb4720bd6f790c09', 'Piece', 'Pc', 1, '1980d2af5ea14ad5b1e7712771f60517'),
('2025-08-11 13:38:11.484985', '2025-08-11 13:38:11.489133', 'f7fb1df983d14f169acfb56973622237', 'PCS', 'Pieces', 1, '94a77b664b5d4efab801ba8560d83fc8'),
('2024-02-23 23:20:35.307335', '2024-02-23 23:20:35.309337', 'ff373e75455341ee967c633bf6f51945', 'Unit', 'Un', 1, '1980d2af5ea14ad5b1e7712771f60517');

-- --------------------------------------------------------

--
-- Table structure for table `aix_userallocationmodel`
--

CREATE TABLE `aix_userallocationmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `task_id` char(32) DEFAULT NULL,
  `work_order_id` char(32) DEFAULT NULL,
  `allocation_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_userallocationmodel`
--

INSERT INTO `aix_userallocationmodel` (`created`, `updated`, `uuid`, `active`, `entity_id`, `task_id`, `work_order_id`, `allocation_id`) VALUES
('2024-03-09 01:28:42.941799', '2024-03-10 01:34:42.139206', '339f1af8355d46368287880d810028e8', 1, '1980d2af5ea14ad5b1e7712771f60517', '144288f8325b4f66946f864e4bcbf970', NULL, 3),
('2024-03-10 01:53:01.133925', '2024-03-10 01:53:01.133925', '4ea1bcfcf9c149be966db2806d1e9c91', 1, '1980d2af5ea14ad5b1e7712771f60517', '144288f8325b4f66946f864e4bcbf970', '01737a416327432f9b21cfade8cbb8b0', 4),
('2024-03-10 01:42:02.086477', '2024-03-10 01:42:02.086477', 'a6eca64f6d1a4e1c8c139b5f92fa8a43', 1, '1980d2af5ea14ad5b1e7712771f60517', NULL, '03c5ccf505794c65ae0a3d7dd23dcc2c', 4);

-- --------------------------------------------------------

--
-- Table structure for table `aix_vendormodel`
--

CREATE TABLE `aix_vendormodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `address_1` varchar(70) NOT NULL,
  `address_2` varchar(70) DEFAULT NULL,
  `city` varchar(70) DEFAULT NULL,
  `state` varchar(70) DEFAULT NULL,
  `zip_code` varchar(20) DEFAULT NULL,
  `country` varchar(70) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `website` varchar(200) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `vendor_name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `active` tinyint(1) NOT NULL,
  `hidden` tinyint(1) NOT NULL,
  `additional_info` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`additional_info`)),
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_vendormodel`
--

INSERT INTO `aix_vendormodel` (`created`, `updated`, `address_1`, `address_2`, `city`, `state`, `zip_code`, `country`, `email`, `website`, `phone`, `uuid`, `vendor_name`, `description`, `active`, `hidden`, `additional_info`, `entity_id`) VALUES
('2024-02-25 01:07:32.606935', '2024-02-25 01:57:15.497103', 'Plot 27 Jinja Road', '2nd Street Industrial Area', 'Kampala', 'Kampala', '256', 'Uganda', 'info@threewaysshipping.com', 'http://bro-group.com', '+256', 'ba5e42c965c1412fa799ae45240d7a87', 'Threeways Shipping Services Ltd', '', 1, 0, NULL, '1980d2af5ea14ad5b1e7712771f60517');

-- --------------------------------------------------------

--
-- Table structure for table `aix_visamodel`
--

CREATE TABLE `aix_visamodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `visa_number` varchar(255) NOT NULL,
  `issue_date` date NOT NULL,
  `expiry_date` date NOT NULL,
  `entity_id` char(32) NOT NULL,
  `immigration_detail_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_weekendmodel`
--

CREATE TABLE `aix_weekendmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_weeklyemployeemodel`
--

CREATE TABLE `aix_weeklyemployeemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `point` int(11) NOT NULL,
  `action` int(11) NOT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_weeklyemployeeprocessedmodel`
--

CREATE TABLE `aix_weeklyemployeeprocessedmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `points` int(11) NOT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_workcategorymodel`
--

CREATE TABLE `aix_workcategorymodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_workcategorymodel`
--

INSERT INTO `aix_workcategorymodel` (`created`, `updated`, `uuid`, `code`, `name`, `description`, `entity_id`) VALUES
('2024-01-22 10:59:39.331090', '2024-01-22 10:59:39.334021', '0c3a04f54bcb4a42b9b9360ff037b96a', 'COCE', 'CALL OUT ORDER FOR CALL OUT EQUIPMENT (Critical/ Emergency Situation)', 'CALL OUT ORDER FOR CALL OUT EQUIPMENT (Critical/ Emergency Situation)', '1980d2af5ea14ad5b1e7712771f60517'),
('2023-11-19 14:22:25.671253', '2024-01-22 10:56:27.771394', '2578970f14aa4686a04ef107d1024be3', 'COER', 'CALL OUT ORDER FOR CALL OUT EQUIPMENT (Rig Move)', 'CALL OUT ORDER FOR CALL OUT EQUIPMENT (Rig Move)', '1980d2af5ea14ad5b1e7712771f60517'),
('2024-01-22 10:57:24.374508', '2024-01-22 10:57:24.376519', '3561335737cb4bc3a8c0332e81bc2db0', 'COOR', 'CALL OUT ORDER FOR CALL OUT EQUIPMENT (Other Than Rig Move)', 'CALL OUT ORDER FOR CALL OUT EQUIPMENT (Other Than Rig Move)', '1980d2af5ea14ad5b1e7712771f60517'),
('2023-11-19 14:22:46.480318', '2024-01-22 10:54:44.938687', '63deb478ae464c30aa649766d2dae54f', 'COPE', 'CALL OUT ORDER FOR PERMANENT EQUIPMENT', 'CALL OUT ORDER FOR PERMANENT EQUIPMENT', '1980d2af5ea14ad5b1e7712771f60517'),
('2024-01-22 11:00:34.208773', '2024-01-22 11:00:34.210691', '8c87b52064404cd58c6fac0347e20a9e', 'COAP', 'CALL OUT ORDER FOR ADDITIONAL PERSONNEL', 'CALL OUT ORDER FOR ADDITIONAL PERSONNEL', '1980d2af5ea14ad5b1e7712771f60517');

-- --------------------------------------------------------

--
-- Table structure for table `aix_workflowactionmodel`
--

CREATE TABLE `aix_workflowactionmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `title` longtext NOT NULL,
  `document_code` varchar(100) DEFAULT NULL,
  `form_name` longtext DEFAULT NULL,
  `description` longtext DEFAULT NULL,
  `action_code` varchar(100) DEFAULT NULL,
  `is_visible` int(11) NOT NULL,
  `is_form` int(11) NOT NULL,
  `has_documents` int(11) NOT NULL,
  `stops_flow` int(11) NOT NULL,
  `permission` varchar(255) DEFAULT NULL,
  `value` int(11) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `entity_id` char(32) NOT NULL,
  `workflow_id` char(32) NOT NULL,
  `workflow_action_type_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_workflowactiontypemodel`
--

CREATE TABLE `aix_workflowactiontypemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `is_decision` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_workflowmodel`
--

CREATE TABLE `aix_workflowmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `version` varchar(255) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `description` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL,
  `workflow_type_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_workflowstatusmodel`
--

CREATE TABLE `aix_workflowstatusmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `title` longtext NOT NULL,
  `description` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL,
  `workflow_type_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_workflowtypemodel`
--

CREATE TABLE `aix_workflowtypemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_workorderactivityassetmodel`
--

CREATE TABLE `aix_workorderactivityassetmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `description` longtext DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `asset_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `activity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_workorderactivityassetmodel`
--

INSERT INTO `aix_workorderactivityassetmodel` (`created`, `updated`, `uuid`, `code`, `start_date`, `end_date`, `description`, `status`, `asset_id`, `entity_id`, `activity_id`) VALUES
('2025-08-22 12:09:31.049282', '2025-08-29 09:55:58.430208', 'edffda5209eb43ab803459454121b81c', 'KKDUZE4C08', '2025-08-01', '2025-08-07', 'Needs a transport plan for the spreader beams at Synopec', 'ACTIVE', '5ae669f7932b11eea0b90a0027000102', '94a77b664b5d4efab801ba8560d83fc8', 'eb4cf45b87034836b5b55c533dcaaba9');

-- --------------------------------------------------------

--
-- Table structure for table `aix_workorderactivitydocumentmodel`
--

CREATE TABLE `aix_workorderactivitydocumentmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `doc_date` date DEFAULT NULL,
  `description` longtext DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `activity_id` char(32) NOT NULL,
  `document_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_workorderactivityliftingmodel`
--

CREATE TABLE `aix_workorderactivityliftingmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `trip_code` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `comments` longtext DEFAULT NULL,
  `activity_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `equipment_id` char(32) NOT NULL,
  `FromLocation` char(32) DEFAULT NULL,
  `operator_id` char(32) NOT NULL,
  `supervisor_id` char(32) NOT NULL,
  `ToLocation` char(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_workorderactivityliftingmodel`
--

INSERT INTO `aix_workorderactivityliftingmodel` (`created`, `updated`, `uuid`, `code`, `trip_code`, `status`, `comments`, `activity_id`, `entity_id`, `equipment_id`, `FromLocation`, `operator_id`, `supervisor_id`, `ToLocation`) VALUES
('2025-09-02 12:38:48.777444', '2025-09-02 13:17:10.488332', '2c492909c92f4ff6bab5d0d70bd80c01', 'HFPD9IVJWS', 'OPS-TR', 'New', 'NAS', 'eb4cf45b87034836b5b55c533dcaaba9', '94a77b664b5d4efab801ba8560d83fc8', '5ae669f7932b11eea0b90a0027000102', NULL, '0c30e4ace3584eb8b68eefc658081359', '13a9a56aa6b44cfc88392e3835db3197', NULL),
('2025-09-02 12:58:04.901578', '2025-09-02 12:58:04.904356', '2fb9889068344075ba39cfc6d57d3eb1', '5ENM2HBKM6', 'OPS-TR', 'Progress', '', 'eb4cf45b87034836b5b55c533dcaaba9', '94a77b664b5d4efab801ba8560d83fc8', '5ae669f7932b11eea0b90a0027000102', NULL, '0c44a9f3cdd347bc9f8a6b0efb842cb1', '0fd2ab8533a846b1b4ee55224ae59635', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `aix_workorderactivityliftingmodel_operators`
--

CREATE TABLE `aix_workorderactivityliftingmodel_operators` (
  `id` int(11) NOT NULL,
  `workorderactivityliftingmodel_id` char(32) NOT NULL,
  `employeemodel_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_workorderactivityliftingmodel_operators`
--

INSERT INTO `aix_workorderactivityliftingmodel_operators` (`id`, `workorderactivityliftingmodel_id`, `employeemodel_id`) VALUES
(3, '2c492909c92f4ff6bab5d0d70bd80c01', '1051867e6db140f48c6e7c85ae1f0409'),
(1, '2fb9889068344075ba39cfc6d57d3eb1', '02bf25668b5d4964ad1e03d2524f1003'),
(2, '2fb9889068344075ba39cfc6d57d3eb1', '1051867e6db140f48c6e7c85ae1f0409');

-- --------------------------------------------------------

--
-- Table structure for table `aix_workorderactivitymodel`
--

CREATE TABLE `aix_workorderactivitymodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(255) NOT NULL,
  `activity_date` date DEFAULT NULL,
  `activity_description` longtext DEFAULT NULL,
  `work_code` varchar(255) DEFAULT NULL,
  `etd` varchar(255) DEFAULT NULL,
  `eta` varchar(255) DEFAULT NULL,
  `atd` varchar(255) DEFAULT NULL,
  `ata` varchar(255) DEFAULT NULL,
  `etp` double DEFAULT NULL,
  `atp` double DEFAULT NULL,
  `comments` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `is_work_location` tinyint(1) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `FromLocation` char(32) DEFAULT NULL,
  `task_id` char(32) NOT NULL,
  `ToLocation` char(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_workorderactivitymodel`
--

INSERT INTO `aix_workorderactivitymodel` (`created`, `updated`, `uuid`, `code`, `activity_date`, `activity_description`, `work_code`, `etd`, `eta`, `atd`, `ata`, `etp`, `atp`, `comments`, `status`, `is_work_location`, `entity_id`, `FromLocation`, `task_id`, `ToLocation`) VALUES
('2025-08-20 13:19:31.667746', '2025-08-21 09:48:25.637769', 'eb4cf45b87034836b5b55c533dcaaba9', 'OPSNQ6V04ERVC', '2024-10-02', 'Transport services for Lifting Crew', NULL, '06:00', '06:40', '06:12', '06:57', 84000, 83700, 'Reached safely', 'Mobilizing', 1, '94a77b664b5d4efab801ba8560d83fc8', 'd5370a8957ed4f79a0bbf47e931b06d9', '8bbde9493eb8433098aa53734f29388f', 'e01dc1e29224468fab70d1f992a160c1');

-- --------------------------------------------------------

--
-- Table structure for table `aix_workorderactivitypersonnelmodel`
--

CREATE TABLE `aix_workorderactivitypersonnelmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `wostatus` varchar(50) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `deploy_date` date NOT NULL,
  `relieve_date` date NOT NULL,
  `duties` longtext DEFAULT NULL,
  `activity_id` char(32) NOT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_workorderactivitypersonnelmodel`
--

INSERT INTO `aix_workorderactivitypersonnelmodel` (`created`, `updated`, `uuid`, `code`, `start_date`, `end_date`, `wostatus`, `status`, `deploy_date`, `relieve_date`, `duties`, `activity_id`, `employee_id`, `entity_id`) VALUES
('2025-09-02 12:37:56.827975', '2025-09-02 12:37:56.831981', '2bd4aac3b3464ebca2016b74fa583c11', 'ADN0P1EQQ0', '2025-09-01', '2025-09-05', NULL, 'ACTIVE', '2025-09-02', '2025-09-05', 'NAS', 'eb4cf45b87034836b5b55c533dcaaba9', '1051867e6db140f48c6e7c85ae1f0409', '94a77b664b5d4efab801ba8560d83fc8'),
('2025-08-22 08:01:27.785394', '2025-08-29 09:37:10.917084', '35f760467dbf4a62947ab1c3a85c68d7', 'TC409LY183', '2025-08-04', '2025-08-15', NULL, 'ACTIVE', '2025-08-05', '2025-08-12', 'On project as Banksman to Relieve Frank Masembe\r\n- rotation basis', 'eb4cf45b87034836b5b55c533dcaaba9', '02bf25668b5d4964ad1e03d2524f1003', '94a77b664b5d4efab801ba8560d83fc8');

-- --------------------------------------------------------

--
-- Table structure for table `aix_workorderactivitytransportmodel`
--

CREATE TABLE `aix_workorderactivitytransportmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `trip_code` varchar(255) DEFAULT NULL,
  `etd` varchar(255) DEFAULT NULL,
  `eta` varchar(255) DEFAULT NULL,
  `atd` varchar(255) DEFAULT NULL,
  `ata` varchar(255) DEFAULT NULL,
  `etp` double DEFAULT NULL,
  `atp` double DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `comments` longtext DEFAULT NULL,
  `activity_id` char(32) NOT NULL,
  `driver_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `FromLocation` char(32) DEFAULT NULL,
  `ToLocation` char(32) DEFAULT NULL,
  `vehicle_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_workorderactivitytransportmodel`
--

INSERT INTO `aix_workorderactivitytransportmodel` (`created`, `updated`, `uuid`, `code`, `trip_code`, `etd`, `eta`, `atd`, `ata`, `etp`, `atp`, `status`, `comments`, `activity_id`, `driver_id`, `entity_id`, `FromLocation`, `ToLocation`, `vehicle_id`) VALUES
('2025-09-03 08:09:06.328323', '2025-09-03 08:09:06.340150', '65f2a6b7308a4933a1bfb7bcba3d604d', 'U1G7IUQXX2', NULL, '08:00', '09:15', '08:10', '09:20', 0, 0, 'New', 'Move the spread beam from section 2 Rig-1503 to section 4 Rig-1503', 'eb4cf45b87034836b5b55c533dcaaba9', '02bf25668b5d4964ad1e03d2524f1003', '94a77b664b5d4efab801ba8560d83fc8', NULL, NULL, '5ae669f7932b11eea0b90a0027000102');

-- --------------------------------------------------------

--
-- Table structure for table `aix_workorderactivitytransportmodel_assistants`
--

CREATE TABLE `aix_workorderactivitytransportmodel_assistants` (
  `id` int(11) NOT NULL,
  `workorderactivitytransportmodel_id` char(32) NOT NULL,
  `employeemodel_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_workorderassetmodel`
--

CREATE TABLE `aix_workorderassetmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `woStatus` varchar(50) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `startDate` date DEFAULT NULL,
  `endDate` date DEFAULT NULL,
  `asset_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `work_order_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_workorderassetmodel`
--

INSERT INTO `aix_workorderassetmodel` (`created`, `updated`, `uuid`, `code`, `description`, `woStatus`, `status`, `startDate`, `endDate`, `asset_id`, `entity_id`, `work_order_id`) VALUES
('2025-07-31 09:22:15.302539', '2025-07-31 09:22:15.315506', '2a6fc35ef5f6461e8882f926a47a83fd', 'NA', 'For Transport', NULL, NULL, '2025-07-07', '2025-07-18', '5ae67bae932b11eea0b90a0027000102', '94a77b664b5d4efab801ba8560d83fc8', '72694865b2fc4437b21abd7c20caff19'),
('2023-12-07 06:46:06.719160', '2023-12-07 06:46:06.732981', '950d6769eddb484da046dc39b0fdf401', 'NA', 'NA', NULL, NULL, '2023-11-28', '2023-11-30', '5ae58936932b11eea0b90a0027000102', '1980d2af5ea14ad5b1e7712771f60517', '4e5aae3f0d384b6fa5d1af15668b48a5'),
('2024-10-15 08:26:03.356929', '2024-10-15 08:26:03.361292', 'ba25b2b99e6a457c9b08e742c0039bbf', 'NA', 'Crane Allocation', NULL, NULL, '2024-10-01', '2024-10-10', '5ae58936932b11eea0b90a0027000102', '94a77b664b5d4efab801ba8560d83fc8', '72694865b2fc4437b21abd7c20caff19'),
('2023-12-07 04:14:19.676581', '2023-12-07 04:14:19.679584', 'de8625f6c4ba4a03a0477ee9c7fa9929', 'NA', 'NA', NULL, NULL, '2023-12-01', '2023-12-01', '5ae47e77932b11eea0b90a0027000102', '1980d2af5ea14ad5b1e7712771f60517', '4e5aae3f0d384b6fa5d1af15668b48a5');

-- --------------------------------------------------------

--
-- Table structure for table `aix_workorderjobcardmodel`
--

CREATE TABLE `aix_workorderjobcardmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `markdown_notes` longtext DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `jcd_number` varchar(20) NOT NULL,
  `jcd_date` date DEFAULT NULL,
  `jcd_title` varchar(250) NOT NULL,
  `current_status` varchar(255) DEFAULT NULL,
  `weight` varchar(255) DEFAULT NULL,
  `distance` double DEFAULT NULL,
  `fuel` double DEFAULT NULL,
  `start_mileage` int(11) DEFAULT NULL,
  `end_mileage` int(11) DEFAULT NULL,
  `scheduled_start_date` date DEFAULT NULL,
  `actual_start_date` date DEFAULT NULL,
  `scheduled_start_time` time(6) DEFAULT NULL,
  `actual_start_time` time(6) DEFAULT NULL,
  `jcd_status` varchar(10) NOT NULL,
  `jcd_amount` decimal(20,2) NOT NULL,
  `jcd_amount_received` decimal(20,2) NOT NULL,
  `draft_date` date DEFAULT NULL,
  `in_review_date` date DEFAULT NULL,
  `approved_date` date DEFAULT NULL,
  `void_date` date DEFAULT NULL,
  `fulfillment_date` date DEFAULT NULL,
  `canceled_date` date DEFAULT NULL,
  `entity_id` char(32) NOT NULL,
  `handler_id` char(32) DEFAULT NULL,
  `work_order_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_workorderjobcardmodel`
--

INSERT INTO `aix_workorderjobcardmodel` (`created`, `updated`, `markdown_notes`, `uuid`, `jcd_number`, `jcd_date`, `jcd_title`, `current_status`, `weight`, `distance`, `fuel`, `start_mileage`, `end_mileage`, `scheduled_start_date`, `actual_start_date`, `scheduled_start_time`, `actual_start_time`, `jcd_status`, `jcd_amount`, `jcd_amount_received`, `draft_date`, `in_review_date`, `approved_date`, `void_date`, `fulfillment_date`, `canceled_date`, `entity_id`, `handler_id`, `work_order_id`) VALUES
('2023-11-19 14:57:06.000401', '2024-02-25 13:17:43.293765', 'This describes the work to be done on the rig move', '08a4c4fa88f8498681ced8886c89e38d', 'JCDX08JFTVMA0', '2023-11-07', 'Rig Move', NULL, NULL, NULL, NULL, NULL, NULL, '2023-07-27', NULL, NULL, NULL, 'draft', '6300000.00', '0.00', NULL, NULL, NULL, NULL, NULL, NULL, '1980d2af5ea14ad5b1e7712771f60517', NULL, '4e5aae3f0d384b6fa5d1af15668b48a5'),
('2024-02-23 23:35:33.833568', '2024-02-25 12:49:23.435905', 'Transfer the 40Ton Crane from the Drill site to DSB yard', '947f2c03f52b4e28841067d7508de40c', 'JCDMV80Y4ZDM1', '2024-01-15', 'Transfer Crane from Tangi - DSB', NULL, NULL, NULL, NULL, NULL, NULL, '2024-01-19', NULL, '07:00:00.000000', NULL, 'approved', '28000000.00', '0.00', NULL, '2024-02-25', '2024-02-25', NULL, NULL, NULL, '1980d2af5ea14ad5b1e7712771f60517', NULL, '4e5aae3f0d384b6fa5d1af15668b48a5'),
('2025-08-05 06:17:02.252631', '2025-08-19 12:06:02.292580', 'Rig Move 1502', 'fd623ee6b7124bceb64d970716a82bf9', 'JCDNX4MMBJ4L1', '2025-07-04', 'Rig Move 1502', NULL, NULL, NULL, NULL, NULL, NULL, '2025-08-01', NULL, '12:00:00.000000', NULL, 'approved', '450.00', '0.00', NULL, '2025-08-19', '2025-08-19', NULL, NULL, NULL, '94a77b664b5d4efab801ba8560d83fc8', NULL, '72694865b2fc4437b21abd7c20caff19');

-- --------------------------------------------------------

--
-- Table structure for table `aix_workorderjobcardstatusmodel`
--

CREATE TABLE `aix_workorderjobcardstatusmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `description` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL,
  `jobcard_id` char(32) NOT NULL,
  `status_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aix_workordermodel`
--

CREATE TABLE `aix_workordermodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `address_1` varchar(70) NOT NULL,
  `address_2` varchar(70) DEFAULT NULL,
  `city` varchar(70) DEFAULT NULL,
  `state` varchar(70) DEFAULT NULL,
  `zip_code` varchar(20) DEFAULT NULL,
  `country` varchar(70) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `website` varchar(200) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `order_no` varchar(255) NOT NULL,
  `remarks` varchar(255) DEFAULT NULL,
  `progress` int(11) DEFAULT NULL,
  `description` longtext DEFAULT NULL,
  `truck_loads` int(11) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `clientref` varchar(255) DEFAULT NULL,
  `service_type` varchar(255) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `category_id` char(32) NOT NULL,
  `currency_id` char(32) NOT NULL,
  `customer_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `wo_type_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_workordermodel`
--

INSERT INTO `aix_workordermodel` (`created`, `updated`, `address_1`, `address_2`, `city`, `state`, `zip_code`, `country`, `email`, `website`, `phone`, `uuid`, `order_no`, `remarks`, `progress`, `description`, `truck_loads`, `start_date`, `end_date`, `status`, `price`, `clientref`, `service_type`, `is_active`, `category_id`, `currency_id`, `customer_id`, `entity_id`, `wo_type_id`) VALUES
('2024-03-08 14:24:05.124018', '2024-03-08 14:24:05.124018', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '01737a416327432f9b21cfade8cbb8b0', 'WOR4BJQ72246', NULL, 0, 'Rig move\r\nPhase 2', NULL, '2024-02-19', '2024-02-22', 'NEW', NULL, NULL, 'TRANSPORT AND LIFTING', 1, '3561335737cb4bc3a8c0332e81bc2db0', '92c576f8dc6e4d72a4ecb02665fef1e7', 'e69edfe356fe484683ae93a593df2fe9', '1980d2af5ea14ad5b1e7712771f60517', 'cd090c9c3d3341f196e0a35e4d5cd992'),
('2024-03-08 14:18:07.310704', '2024-03-08 14:18:07.310704', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '03c5ccf505794c65ae0a3d7dd23dcc2c', 'WO3418ANE6W4', NULL, 0, 'Rig move\r\nPhase 2', NULL, '2024-02-19', '2024-02-22', 'NEW', NULL, NULL, 'TRANSPORT AND LIFTING', 1, '3561335737cb4bc3a8c0332e81bc2db0', '92c576f8dc6e4d72a4ecb02665fef1e7', 'e69edfe356fe484683ae93a593df2fe9', '1980d2af5ea14ad5b1e7712771f60517', 'cd090c9c3d3341f196e0a35e4d5cd992'),
('2024-03-08 14:01:44.411873', '2024-03-08 14:01:44.411873', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '1a0bbeac0f5c4d83a56d5906af50affb', 'WO3FU7DS6N7R', NULL, 0, 'Rig move\r\nPhase 2', NULL, '2024-02-19', '2024-02-22', 'NEW', NULL, NULL, 'TRANSPORT AND LIFTING', 1, '3561335737cb4bc3a8c0332e81bc2db0', '92c576f8dc6e4d72a4ecb02665fef1e7', 'e69edfe356fe484683ae93a593df2fe9', '1980d2af5ea14ad5b1e7712771f60517', 'cd090c9c3d3341f196e0a35e4d5cd992'),
('2023-11-19 14:43:18.465695', '2024-02-09 12:24:52.810212', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '4e5aae3f0d384b6fa5d1af15668b48a5', 'WOUNJESO9CCN', 'NA', 0, 'Some Activity', NULL, '2023-11-01', '2023-11-07', 'NEW', NULL, NULL, 'TRANSPORT AND LIFTING', 1, '2578970f14aa4686a04ef107d1024be3', 'ace592b3fbad4837815b118a04f9f1cb', 'e69edfe356fe484683ae93a593df2fe9', '1980d2af5ea14ad5b1e7712771f60517', '314e5436889647a7a0f1ef8e3af58aef'),
('2024-02-28 13:06:16.661314', '2024-02-28 13:06:16.668281', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '596a72a0d456482e87b578c24e9917af', 'WOV5J6XTU3EL', 'NA', 0, 'Rig move final stages', NULL, '2024-01-01', '2024-02-15', 'NEW', NULL, NULL, 'TRANSPORT AND LIFTING', 1, '63deb478ae464c30aa649766d2dae54f', 'd0d964fd363944fb84796f0869444082', 'e69edfe356fe484683ae93a593df2fe9', '1980d2af5ea14ad5b1e7712771f60517', '314e5436889647a7a0f1ef8e3af58aef'),
('2024-03-08 14:26:10.417051', '2024-03-08 14:26:13.833512', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '608183a1ad1d470682e83b408f8bbab2', 'WOLNOQ4HKLKN', NULL, 0, 'Rig move\r\nPhase 2 personnel', NULL, '2024-02-19', '2024-02-22', 'NEW', NULL, NULL, 'TRANSPORT AND LIFTING', 1, '8c87b52064404cd58c6fac0347e20a9e', '92c576f8dc6e4d72a4ecb02665fef1e7', 'e69edfe356fe484683ae93a593df2fe9', '1980d2af5ea14ad5b1e7712771f60517', 'cd090c9c3d3341f196e0a35e4d5cd992'),
('2024-03-27 11:17:18.473700', '2024-03-27 11:17:22.899875', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '66c9b0f172774b52a752f059d88bba24', 'WOB8D0M0RXC4', 'NA', 0, 'NA', NULL, '2024-03-01', '2024-03-01', 'NEW', NULL, NULL, 'LIFTING ONLY', 1, '3561335737cb4bc3a8c0332e81bc2db0', 'd0d964fd363944fb84796f0869444082', 'e69edfe356fe484683ae93a593df2fe9', '1980d2af5ea14ad5b1e7712771f60517', '891b977ac94643358ea5e2c369160e55'),
('2024-03-08 11:27:50.260452', '2024-03-08 11:27:50.260452', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '685cec26695d4604b55f5d90b8a626d8', 'WOMLUSJS3SXG', 'DSB', 0, 'TANGI', NULL, '2024-02-05', '2024-03-06', 'NEW', NULL, NULL, 'TRANSPORT ONLY', 1, '0c3a04f54bcb4a42b9b9360ff037b96a', 'd0d964fd363944fb84796f0869444082', 'e69edfe356fe484683ae93a593df2fe9', '1980d2af5ea14ad5b1e7712771f60517', '15c73a543a7a4aa6afe732d961807d3f'),
('2024-03-08 13:38:07.387659', '2024-03-08 13:38:07.387659', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '6c24d8c38893423e81f41811b78fd73e', 'WODA1G7OMP8D', 'Rig move equipment', 0, 'Rig move equipment\r\nPahse One', NULL, '2024-02-12', '2024-02-22', 'NEW', NULL, NULL, 'TRANSPORT ONLY', 1, '63deb478ae464c30aa649766d2dae54f', '92c576f8dc6e4d72a4ecb02665fef1e7', 'e69edfe356fe484683ae93a593df2fe9', '1980d2af5ea14ad5b1e7712771f60517', '891b977ac94643358ea5e2c369160e55'),
('2024-10-15 06:44:44.979046', '2024-10-15 06:44:48.535735', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '72694865b2fc4437b21abd7c20caff19', 'WORR59JWM8EG', 'Rig Move 1502', 0, 'Rig Move 1502 \r\nTangi - Tilenga Project', NULL, '2024-10-01', '2024-10-30', 'NEW', NULL, 'ABC', 'TRANSPORT AND LIFTING', 1, '2578970f14aa4686a04ef107d1024be3', '15a1e0c71f0646fcb537b7598c4c41e4', '8844b93b0dee4a77afb91daa81968f61', '94a77b664b5d4efab801ba8560d83fc8', '15c73a543a7a4aa6afe732d961807d3f'),
('2024-03-08 13:39:39.223633', '2024-03-08 13:39:42.057667', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '83f3c885398246e3aee71ebf64f39733', 'WOEODONM4M7D', NULL, 0, 'Rig move\r\nPhase 2', NULL, '2024-02-19', '2024-02-22', 'NEW', NULL, NULL, 'TRANSPORT AND LIFTING', 1, '3561335737cb4bc3a8c0332e81bc2db0', '92c576f8dc6e4d72a4ecb02665fef1e7', 'e69edfe356fe484683ae93a593df2fe9', '1980d2af5ea14ad5b1e7712771f60517', 'cd090c9c3d3341f196e0a35e4d5cd992'),
('2024-03-08 11:25:47.968186', '2024-03-08 11:25:47.968186', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '8c0aceaa9a8240c79ed649d839298997', 'WOVLHS4TY2KS', 'NA', 0, 'NA', NULL, '2024-02-01', '2024-02-08', 'NEW', NULL, NULL, 'LIFTING ONLY', 1, '0c3a04f54bcb4a42b9b9360ff037b96a', 'd0d964fd363944fb84796f0869444082', 'e69edfe356fe484683ae93a593df2fe9', '1980d2af5ea14ad5b1e7712771f60517', '15c73a543a7a4aa6afe732d961807d3f'),
('2024-02-29 08:35:33.916389', '2024-02-29 08:50:33.469179', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'a12fbcef0b6c418d9004e34fb7bf66c8', 'WO9IA8NIMZCY', NULL, 0, '220Ton crane for lifting', NULL, '2024-02-01', '2024-02-29', 'NEW', NULL, NULL, 'TRANSPORT AND LIFTING', 1, '2578970f14aa4686a04ef107d1024be3', 'd0d964fd363944fb84796f0869444082', 'e69edfe356fe484683ae93a593df2fe9', '1980d2af5ea14ad5b1e7712771f60517', '314e5436889647a7a0f1ef8e3af58aef'),
('2024-03-08 14:11:19.100249', '2024-03-08 14:11:19.100249', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'ae5e74dcd7404e049c7ae8956015cbec', 'WOF55UCGHUY2', NULL, 0, 'Rig move\r\nPhase 2', NULL, '2024-02-19', '2024-02-22', 'NEW', NULL, NULL, 'TRANSPORT AND LIFTING', 1, '3561335737cb4bc3a8c0332e81bc2db0', '92c576f8dc6e4d72a4ecb02665fef1e7', 'e69edfe356fe484683ae93a593df2fe9', '1980d2af5ea14ad5b1e7712771f60517', 'cd090c9c3d3341f196e0a35e4d5cd992'),
('2024-03-08 13:30:47.609896', '2024-03-08 13:30:47.609896', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'bfc34c132a8a481ea409c56348a49fd8', 'WOWG2R2990W1', 'Rig move equipment', 0, 'Rig move equipment\r\nPahse One', NULL, '2024-02-12', '2024-02-22', 'NEW', NULL, NULL, 'TRANSPORT ONLY', 1, '63deb478ae464c30aa649766d2dae54f', '92c576f8dc6e4d72a4ecb02665fef1e7', 'e69edfe356fe484683ae93a593df2fe9', '1980d2af5ea14ad5b1e7712771f60517', '891b977ac94643358ea5e2c369160e55'),
('2024-03-08 12:30:18.494164', '2024-03-08 12:30:18.494164', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'c115b33565f54d8e9b64315457346c6b', 'WOFFJZSKIG66', 'DSB', 0, 'TANGI', NULL, '2024-02-05', '2024-03-06', 'NEW', NULL, NULL, 'TRANSPORT ONLY', 1, '0c3a04f54bcb4a42b9b9360ff037b96a', 'd0d964fd363944fb84796f0869444082', 'e69edfe356fe484683ae93a593df2fe9', '1980d2af5ea14ad5b1e7712771f60517', '15c73a543a7a4aa6afe732d961807d3f'),
('2023-12-11 13:46:06.732193', '2024-02-09 12:24:19.183532', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'c3144d71d7f64589b9718044b9725281', 'WOIGQP2TL3LX', 'NA', 0, 'NA', NULL, '2023-10-30', '2023-11-30', 'IN PROGRESS', NULL, NULL, 'LIFTING ONLY', 1, '63deb478ae464c30aa649766d2dae54f', '89dd1b47c8e543708da18c8bb26ac8ae', 'e69edfe356fe484683ae93a593df2fe9', '1980d2af5ea14ad5b1e7712771f60517', '314e5436889647a7a0f1ef8e3af58aef'),
('2024-03-08 14:19:59.325601', '2024-03-08 14:19:59.325601', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'cb9095e2b60044acbb6fff5ac6467e79', 'WO2H11J3WSJF', NULL, 0, 'Rig move\r\nPhase 2', NULL, '2024-02-19', '2024-02-22', 'NEW', NULL, NULL, 'TRANSPORT AND LIFTING', 1, '3561335737cb4bc3a8c0332e81bc2db0', '92c576f8dc6e4d72a4ecb02665fef1e7', 'e69edfe356fe484683ae93a593df2fe9', '1980d2af5ea14ad5b1e7712771f60517', 'cd090c9c3d3341f196e0a35e4d5cd992'),
('2024-03-08 14:03:55.721896', '2024-03-08 14:03:55.721896', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'cc83baa59a9c4f3d83d47b2ab45d56c0', 'WOBNMOF1HYNO', NULL, 0, 'Rig move\r\nPhase 2', NULL, '2024-02-19', '2024-02-22', 'NEW', NULL, NULL, 'TRANSPORT AND LIFTING', 1, '3561335737cb4bc3a8c0332e81bc2db0', '92c576f8dc6e4d72a4ecb02665fef1e7', 'e69edfe356fe484683ae93a593df2fe9', '1980d2af5ea14ad5b1e7712771f60517', 'cd090c9c3d3341f196e0a35e4d5cd992'),
('2024-03-08 11:26:17.729327', '2024-03-08 11:26:17.729327', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'cfaf438a7fcb409eb9ac47d17c711c55', 'WOQ78G9A7VAM', 'NA', 0, 'NA', NULL, '2024-02-01', '2024-02-08', 'NEW', NULL, NULL, 'LIFTING ONLY', 1, '0c3a04f54bcb4a42b9b9360ff037b96a', 'd0d964fd363944fb84796f0869444082', 'e69edfe356fe484683ae93a593df2fe9', '1980d2af5ea14ad5b1e7712771f60517', '15c73a543a7a4aa6afe732d961807d3f'),
('2024-03-08 11:20:23.618899', '2024-03-08 11:20:23.622897', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'd4dc6f0fc85741c584eb3a91b82ef1ed', 'WOZKGDNHU80K', 'NA', 0, 'NA', NULL, '2024-03-01', '2024-03-07', 'NEW', NULL, NULL, 'TRANSPORT AND LIFTING', 1, '0c3a04f54bcb4a42b9b9360ff037b96a', 'd0d964fd363944fb84796f0869444082', 'e69edfe356fe484683ae93a593df2fe9', '1980d2af5ea14ad5b1e7712771f60517', '15c73a543a7a4aa6afe732d961807d3f'),
('2024-03-08 11:24:17.294540', '2024-03-08 11:24:17.294540', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'dbc73d3ed7ef4d57b53746afa3c76a3e', 'WOQ432CXSS93', 'NA', 0, 'NA', NULL, '2024-02-01', '2024-02-08', 'NEW', NULL, NULL, 'LIFTING ONLY', 1, '0c3a04f54bcb4a42b9b9360ff037b96a', 'd0d964fd363944fb84796f0869444082', 'e69edfe356fe484683ae93a593df2fe9', '1980d2af5ea14ad5b1e7712771f60517', '15c73a543a7a4aa6afe732d961807d3f'),
('2024-03-08 11:23:02.809791', '2024-03-08 11:23:02.809791', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'ecd1a87415284c9bab99876b4c9fc143', 'WOQJMMVGNIDR', 'NA', 0, 'NA', NULL, '2024-02-01', '2024-02-08', 'NEW', NULL, NULL, 'LIFTING ONLY', 1, '0c3a04f54bcb4a42b9b9360ff037b96a', 'd0d964fd363944fb84796f0869444082', 'e69edfe356fe484683ae93a593df2fe9', '1980d2af5ea14ad5b1e7712771f60517', '15c73a543a7a4aa6afe732d961807d3f'),
('2024-03-08 13:43:25.357473', '2024-03-08 13:43:25.357473', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'efa7a91fc2494e74832ceec444a17c73', 'WOEEBU798DZ2', NULL, 0, 'Rig move\r\nPhase 2', NULL, '2024-02-19', '2024-02-22', 'NEW', NULL, NULL, 'TRANSPORT AND LIFTING', 1, '3561335737cb4bc3a8c0332e81bc2db0', '92c576f8dc6e4d72a4ecb02665fef1e7', 'e69edfe356fe484683ae93a593df2fe9', '1980d2af5ea14ad5b1e7712771f60517', 'cd090c9c3d3341f196e0a35e4d5cd992'),
('2024-03-08 14:12:09.365619', '2024-03-08 14:12:09.365619', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'f2dc54266bf94f3e95708bdfb5c48efc', 'WO4BH31G4H5R', NULL, 0, 'Rig move\r\nPhase 2', NULL, '2024-02-19', '2024-02-22', 'NEW', NULL, NULL, 'TRANSPORT AND LIFTING', 1, '3561335737cb4bc3a8c0332e81bc2db0', '92c576f8dc6e4d72a4ecb02665fef1e7', 'e69edfe356fe484683ae93a593df2fe9', '1980d2af5ea14ad5b1e7712771f60517', 'cd090c9c3d3341f196e0a35e4d5cd992'),
('2024-03-08 14:03:14.395369', '2024-03-08 14:03:14.395369', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'fdaac8b24bdd4441b034a2bab8ef3281', 'WOA1OOJJCVIF', NULL, 0, 'Rig move\r\nPhase 2', NULL, '2024-02-19', '2024-02-22', 'NEW', NULL, NULL, 'TRANSPORT AND LIFTING', 1, '3561335737cb4bc3a8c0332e81bc2db0', '92c576f8dc6e4d72a4ecb02665fef1e7', 'e69edfe356fe484683ae93a593df2fe9', '1980d2af5ea14ad5b1e7712771f60517', 'cd090c9c3d3341f196e0a35e4d5cd992');

-- --------------------------------------------------------

--
-- Table structure for table `aix_workorderpersonnelmodel`
--

CREATE TABLE `aix_workorderpersonnelmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `startDate` date DEFAULT NULL,
  `endDate` date DEFAULT NULL,
  `woStatus` varchar(50) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `deployDate` date NOT NULL,
  `relieveDate` date NOT NULL,
  `duties` longtext DEFAULT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `work_order_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_workorderpersonnelmodel`
--

INSERT INTO `aix_workorderpersonnelmodel` (`created`, `updated`, `uuid`, `code`, `startDate`, `endDate`, `woStatus`, `status`, `deployDate`, `relieveDate`, `duties`, `employee_id`, `entity_id`, `work_order_id`) VALUES
('2025-07-31 09:24:21.252464', '2025-07-31 09:24:21.260185', '07d86f064e8346cda6eb10ce7cfedb06', 'NA', '2025-07-14', '2025-07-25', NULL, NULL, '2025-07-14', '2025-07-25', 'For Transport Coordinator', '641de26c55c444bfaaaf8d26e6a3b3cc', '94a77b664b5d4efab801ba8560d83fc8', '72694865b2fc4437b21abd7c20caff19'),
('2023-12-07 04:59:31.057571', '2023-12-07 04:59:31.067678', '3852d909432746b1b6dcb5761d5ac2ac', 'NA', '2023-11-22', '2023-11-30', NULL, NULL, '2023-11-07', '2023-11-17', 'NA', '3ec26bd94d0540348a4bfa95926bfa99', '1980d2af5ea14ad5b1e7712771f60517', '4e5aae3f0d384b6fa5d1af15668b48a5'),
('2024-10-15 08:27:50.356094', '2024-10-15 08:27:50.358616', '4168528366a343c9931315fbb84628c9', 'NA', '2024-10-02', '2024-10-09', NULL, NULL, '2024-10-03', '2024-10-10', 'Lifing Supervisor', '06ceefa18855477e9f9b7bfc82df4055', '94a77b664b5d4efab801ba8560d83fc8', '72694865b2fc4437b21abd7c20caff19'),
('2023-12-07 07:54:26.817889', '2023-12-07 07:54:26.829070', '707ca1cdfb244b0091b857104eed7d81', 'NA', '2023-11-28', '2023-12-04', NULL, NULL, '2023-11-28', '2023-12-03', 'NA', '3ec26bd94d0540348a4bfa95926bfa99', '1980d2af5ea14ad5b1e7712771f60517', '4e5aae3f0d384b6fa5d1af15668b48a5'),
('2025-07-31 09:23:14.645109', '2025-07-31 09:23:14.648730', '93fd8b6c445d4be9a75e19ace8682d9b', 'NA', '2025-07-07', '2025-07-18', NULL, NULL, '2025-07-07', '2025-07-19', 'For Site Supervisor', '89ef25176e53432e83a713fcf083b6f6', '94a77b664b5d4efab801ba8560d83fc8', '72694865b2fc4437b21abd7c20caff19');

-- --------------------------------------------------------

--
-- Table structure for table `aix_workorderstatusmodel`
--

CREATE TABLE `aix_workorderstatusmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_workorderstatusmodel`
--

INSERT INTO `aix_workorderstatusmodel` (`created`, `updated`, `uuid`, `code`, `name`, `description`, `entity_id`) VALUES
('2023-11-19 14:32:35.651319', '2023-11-19 14:32:35.653339', '4cd00f77898d4190b5381eddbbc90f25', 'PSTND', 'POSTPONED', 'Postponed', '1980d2af5ea14ad5b1e7712771f60517'),
('2023-11-19 14:28:18.289280', '2023-11-19 14:28:18.294831', '6d39bf92c420453baf8204f7c09b3d13', 'NEW', 'New', 'New/ Created', '1980d2af5ea14ad5b1e7712771f60517'),
('2023-11-19 14:31:15.700696', '2023-11-19 14:31:15.703715', '9feaee2d086b4402be650238268b8b2c', 'INPROG', 'IN PROGRESS', 'In Progress', '1980d2af5ea14ad5b1e7712771f60517'),
('2023-11-19 14:33:19.735658', '2023-11-19 14:33:19.739812', 'aa2ce04ac87c46ea9d6c1233cd7af1b0', 'COMP', 'COMPLETED', 'Completed', '1980d2af5ea14ad5b1e7712771f60517'),
('2023-11-19 14:31:51.877492', '2023-11-19 14:31:51.880391', 'd8b2b41eb889404d88a593d7940734d6', 'DELAYED', 'DELAYED', 'Delayed', '1980d2af5ea14ad5b1e7712771f60517');

-- --------------------------------------------------------

--
-- Table structure for table `aix_workordertaskassetmodel`
--

CREATE TABLE `aix_workordertaskassetmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `startDate` date DEFAULT NULL,
  `endDate` date DEFAULT NULL,
  `description` longtext DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `asset_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `task_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_workordertaskassetmodel`
--

INSERT INTO `aix_workordertaskassetmodel` (`created`, `updated`, `uuid`, `code`, `startDate`, `endDate`, `description`, `status`, `asset_id`, `entity_id`, `task_id`) VALUES
('2024-03-18 07:30:40.435140', '2024-03-18 08:04:51.063930', '485569a2f75a41398d94cd32ef8b5fb5', 'DSJREUOH5C', '2024-02-04', '2024-02-08', 'lifting suspended container in NN', 'ACTIVE', '5ae47e77932b11eea0b90a0027000102', '1980d2af5ea14ad5b1e7712771f60517', '144288f8325b4f66946f864e4bcbf970'),
('2025-07-29 13:45:52.469190', '2025-07-29 14:02:43.379918', '654834fa01df4a8d86e03059317dd8f1', 'VDXQXSAO1E', '2025-06-02', '2025-07-25', 'To be On Hire', 'ACTIVE', '5ae669f7932b11eea0b90a0027000102', '94a77b664b5d4efab801ba8560d83fc8', '8bbde9493eb8433098aa53734f29388f'),
('2024-03-20 12:50:11.414608', '2024-03-20 12:50:11.426015', 'c112c1f96ec54b3496da7401e4074b18', 'PTS9OYJBSD', '2024-02-01', '2024-02-05', 'NA', 'ACTIVE', '5ae47e77932b11eea0b90a0027000102', '1980d2af5ea14ad5b1e7712771f60517', '902036dbff0249bfbd0bc6d2c0bd50ac'),
('2024-03-18 07:41:28.859221', '2024-03-18 07:57:57.124550', 'f98f4fe8463b42b9b69b5197b7a494e1', 'WB9MWSP8VB', '2024-02-04', '2024-02-14', 'Move sling pipes to SN SLB', 'ACTIVE', '5ae58598932b11eea0b90a0027000102', '1980d2af5ea14ad5b1e7712771f60517', '144288f8325b4f66946f864e4bcbf970');

-- --------------------------------------------------------

--
-- Table structure for table `aix_workordertaskmodel`
--

CREATE TABLE `aix_workordertaskmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `tripNo` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `currentStatus` varchar(255) DEFAULT NULL,
  `weight` double DEFAULT NULL,
  `tripDistance` double DEFAULT NULL,
  `fuel` double DEFAULT NULL,
  `startMileage` int(11) DEFAULT NULL,
  `endMileage` int(11) DEFAULT NULL,
  `statusDate` datetime(6) DEFAULT NULL,
  `startDate` date DEFAULT NULL,
  `endDate` date DEFAULT NULL,
  `EndLocation` char(32) DEFAULT NULL,
  `entity_id` char(32) NOT NULL,
  `StartLocation` char(32) DEFAULT NULL,
  `work_order_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_workordertaskmodel`
--

INSERT INTO `aix_workordertaskmodel` (`created`, `updated`, `uuid`, `tripNo`, `description`, `currentStatus`, `weight`, `tripDistance`, `fuel`, `startMileage`, `endMileage`, `statusDate`, `startDate`, `endDate`, `EndLocation`, `entity_id`, `StartLocation`, `work_order_id`) VALUES
('2024-02-06 11:43:58.344140', '2024-02-09 07:56:29.691537', '1232070d5e024fe39aa42a5e3d81bdf9', NULL, 'Tranport 40Ton Crane', 'IN PROGRESS', 40, 50, 37, NULL, NULL, NULL, '2024-01-09', '2024-02-08', 'ac92dd81559745f59624539ca6fad402', '1980d2af5ea14ad5b1e7712771f60517', '08cc8d74f3144bf2bff818aefc69b745', 'c3144d71d7f64589b9718044b9725281'),
('2023-11-30 04:53:13.734194', '2024-03-22 08:10:42.124470', '144288f8325b4f66946f864e4bcbf970', 'TSKWK378HB', NULL, 'IN PROGRESS', NULL, NULL, NULL, 1456, 1476, NULL, '2023-11-08', '2023-11-09', 'cceb53cedd2146eab161e6e6d7021d49', '1980d2af5ea14ad5b1e7712771f60517', '08cc8d74f3144bf2bff818aefc69b745', '4e5aae3f0d384b6fa5d1af15668b48a5'),
('2024-01-19 12:36:04.487656', '2024-01-19 12:36:04.494631', '57c893e37ac94b31ac4245ce39dac646', 'TSKRE33GVF', NULL, NULL, NULL, NULL, NULL, 67889, 67899, NULL, '2024-01-19', '2024-01-19', NULL, '1980d2af5ea14ad5b1e7712771f60517', NULL, '4e5aae3f0d384b6fa5d1af15668b48a5'),
('2023-11-30 04:43:31.646178', '2023-11-30 08:27:02.928331', '57e593d6bf9f48ffbc576a7459be7019', 'TSKMK38NS', NULL, NULL, NULL, NULL, NULL, 1234, 1244, NULL, '2023-11-12', '2023-11-17', NULL, '1980d2af5ea14ad5b1e7712771f60517', NULL, '4e5aae3f0d384b6fa5d1af15668b48a5'),
('2024-03-19 06:07:26.081350', '2024-03-19 06:07:26.081350', '6bb2e8726d3f4d8abf301a17108a0ab2', NULL, 'NA', 'NEW', 80, 40, 120, NULL, NULL, NULL, '2024-02-07', '2024-02-09', 'ac92dd81559745f59624539ca6fad402', '1980d2af5ea14ad5b1e7712771f60517', '08cc8d74f3144bf2bff818aefc69b745', '01737a416327432f9b21cfade8cbb8b0'),
('2024-10-15 09:53:04.075871', '2025-08-20 08:15:14.142095', '8bbde9493eb8433098aa53734f29388f', 'TRPKWGA7393J1', 'rig move\r\n- transfer pipes to JBR2\r\n- tranport shackles to JBR4\r\n- supply fuel to cranes at JBR2', 'NEW', NULL, 140, 230, NULL, NULL, NULL, '2024-10-02', '2024-10-09', 'e01dc1e29224468fab70d1f992a160c1', '94a77b664b5d4efab801ba8560d83fc8', 'd5370a8957ed4f79a0bbf47e931b06d9', '72694865b2fc4437b21abd7c20caff19'),
('2023-11-23 12:32:59.816716', '2024-01-22 11:58:17.140827', '902036dbff0249bfbd0bc6d2c0bd50ac', 'TSKSA27DS9', 'Transport services for crane', 'IN PROGRESS', 40, 14, 120, 12345, 14563, NULL, '2023-11-13', '2023-11-17', 'ce75fa4c21714c2390c6b7b57736cd93', '1980d2af5ea14ad5b1e7712771f60517', '08cc8d74f3144bf2bff818aefc69b745', '4e5aae3f0d384b6fa5d1af15668b48a5'),
('2023-11-28 10:16:52.995245', '2023-11-28 10:16:53.000251', '919f264a366d4ddc8b2697332f447f90', 'TSKK387GVF', NULL, NULL, NULL, NULL, NULL, 1209, 1308, NULL, '2023-11-07', '2023-11-14', NULL, '1980d2af5ea14ad5b1e7712771f60517', NULL, '4e5aae3f0d384b6fa5d1af15668b48a5'),
('2024-03-19 07:05:26.977889', '2024-03-19 07:10:49.079955', '960b9fbc4bbc407998dba2c968402d7b', NULL, 'NA', 'NEW', 80, 40, 120, NULL, NULL, NULL, '2024-02-07', '2024-02-09', 'cceb53cedd2146eab161e6e6d7021d49', '1980d2af5ea14ad5b1e7712771f60517', '08cc8d74f3144bf2bff818aefc69b745', '01737a416327432f9b21cfade8cbb8b0'),
('2025-08-20 08:38:01.386691', '2025-08-20 08:38:01.386691', 'dc6c06508a5b4205a18883ebc9a1778b', 'TRPZ96PPH75JU', 'Lifting work to be done;\r\n- shift generator from section A to section B', 'NEW', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'd5370a8957ed4f79a0bbf47e931b06d9', '94a77b664b5d4efab801ba8560d83fc8', 'e01dc1e29224468fab70d1f992a160c1', '72694865b2fc4437b21abd7c20caff19'),
('2025-08-20 08:41:40.704280', '2025-08-20 08:41:40.704280', 'ebbc748ac67d4eba961da9bbb0424a57', 'TRPXE7XLQZ0LJ', 'Lifting work to be done;\r\n- shift generator from section A to section B', 'NEW', NULL, NULL, NULL, NULL, NULL, NULL, '2024-10-01', '2024-10-03', 'd5370a8957ed4f79a0bbf47e931b06d9', '94a77b664b5d4efab801ba8560d83fc8', 'e01dc1e29224468fab70d1f992a160c1', '72694865b2fc4437b21abd7c20caff19');

-- --------------------------------------------------------

--
-- Table structure for table `aix_workordertaskpersonnelmodel`
--

CREATE TABLE `aix_workordertaskpersonnelmodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `startDate` date DEFAULT NULL,
  `endDate` date DEFAULT NULL,
  `woStatus` varchar(50) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `deployDate` date NOT NULL,
  `relieveDate` date NOT NULL,
  `duties` longtext DEFAULT NULL,
  `employee_id` char(32) NOT NULL,
  `entity_id` char(32) NOT NULL,
  `task_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_workordertaskpersonnelmodel`
--

INSERT INTO `aix_workordertaskpersonnelmodel` (`created`, `updated`, `uuid`, `code`, `startDate`, `endDate`, `woStatus`, `status`, `deployDate`, `relieveDate`, `duties`, `employee_id`, `entity_id`, `task_id`) VALUES
('2024-03-21 06:28:25.853821', '2024-03-21 06:28:25.858457', '0e4a3c462928490697bba1fc68866d17', 'XQ1BEUIND0', '2024-02-01', '2024-03-04', NULL, 'ACTIVE', '2024-02-07', '2024-02-14', 'NA', '3ec26bd94d0540348a4bfa95926bfa99', '1980d2af5ea14ad5b1e7712771f60517', '144288f8325b4f66946f864e4bcbf970'),
('2024-03-20 12:51:06.018227', '2024-03-20 12:51:06.024052', '0f0094b6828c4e56895a6a33d8a6d0c5', '3KTZ8UG0S9', '2024-02-01', '2024-03-01', NULL, 'ACTIVE', '2024-02-05', '2024-02-23', 'NA', '3ec26bd94d0540348a4bfa95926bfa99', '1980d2af5ea14ad5b1e7712771f60517', '902036dbff0249bfbd0bc6d2c0bd50ac'),
('2024-03-18 06:01:02.444091', '2024-03-18 07:55:39.427916', '22270495ac0e49d7887ced63f36459c9', 'V1VRW78S0O', '2024-02-01', '2024-02-15', NULL, 'ACTIVE', '2024-02-05', '2024-02-14', 'HSE Activity in SN', '3ec26bd94d0540348a4bfa95926bfa99', '1980d2af5ea14ad5b1e7712771f60517', '144288f8325b4f66946f864e4bcbf970'),
('2024-03-20 09:52:56.238814', '2024-03-20 09:52:56.248393', '9d839d64e3fb4e199fbba0e42003295a', '5D4NEESJNM', '2024-03-01', '2024-03-04', NULL, 'ACTIVE', '2024-03-05', '2024-03-07', 'NA', '3ec26bd94d0540348a4bfa95926bfa99', '1980d2af5ea14ad5b1e7712771f60517', '902036dbff0249bfbd0bc6d2c0bd50ac'),
('2024-03-18 05:48:18.903930', '2024-03-18 05:48:18.906571', 'd51586bbfad048c19142269a8da4b89b', 'NK728L4J32', '2024-03-01', '2024-01-12', NULL, 'ACTIVE', '2024-01-08', '2024-01-12', 'To work on the Rig 1501', '3ec26bd94d0540348a4bfa95926bfa99', '1980d2af5ea14ad5b1e7712771f60517', '144288f8325b4f66946f864e4bcbf970');

-- --------------------------------------------------------

--
-- Table structure for table `aix_workordertypemodel`
--

CREATE TABLE `aix_workordertypemodel` (
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `uuid` char(32) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `entity_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aix_workordertypemodel`
--

INSERT INTO `aix_workordertypemodel` (`created`, `updated`, `uuid`, `code`, `name`, `description`, `entity_id`) VALUES
('2024-01-22 10:53:19.995417', '2024-01-22 10:53:19.997134', '15c73a543a7a4aa6afe732d961807d3f', 'ONEF', 'ONE OFF', 'One Off', '1980d2af5ea14ad5b1e7712771f60517'),
('2023-11-19 14:20:29.109215', '2023-11-19 14:21:06.638502', '314e5436889647a7a0f1ef8e3af58aef', 'GNR', 'GENERAL', 'General', '1980d2af5ea14ad5b1e7712771f60517'),
('2024-01-22 10:52:35.259985', '2024-01-22 10:52:35.261006', '891b977ac94643358ea5e2c369160e55', 'SCT', 'SUB-CONTRACT', 'Sub Contract', '1980d2af5ea14ad5b1e7712771f60517'),
('2023-11-19 14:20:55.505023', '2023-11-19 14:20:55.508625', 'cd090c9c3d3341f196e0a35e4d5cd992', 'PRJ', 'PROJECT', 'Project based', '1980d2af5ea14ad5b1e7712771f60517'),
('2024-01-22 10:52:01.660743', '2024-01-22 10:52:01.665419', 'e06236e6c6e1402ab3b069f21dedee28', 'CTR', 'CONTRACT', 'Contract', '1980d2af5ea14ad5b1e7712771f60517');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'Admins'),
(3, 'Clerks'),
(4, 'OperationsManager'),
(6, 'ProjectManager'),
(2, 'Supervisor'),
(5, 'TotalProjectManager');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 1, 4),
(5, 1, 5),
(6, 1, 6),
(7, 1, 7),
(8, 1, 8),
(9, 1, 9),
(10, 1, 10),
(11, 1, 11),
(12, 1, 12),
(13, 1, 13),
(14, 1, 14),
(15, 1, 15),
(16, 1, 16),
(17, 1, 17),
(18, 1, 18),
(19, 1, 19),
(20, 1, 20),
(21, 1, 21),
(22, 1, 22),
(23, 1, 23),
(24, 1, 24),
(25, 1, 25),
(26, 1, 26),
(27, 1, 27),
(28, 1, 28),
(29, 1, 29),
(30, 1, 30),
(31, 1, 31),
(32, 1, 32),
(33, 1, 33),
(34, 1, 34),
(35, 1, 35),
(36, 1, 36),
(37, 1, 37),
(38, 1, 38),
(39, 1, 39),
(40, 1, 40),
(41, 1, 41),
(42, 1, 42),
(43, 1, 43),
(44, 1, 44),
(45, 1, 45),
(46, 1, 46),
(47, 1, 47),
(48, 1, 48),
(49, 1, 49),
(50, 1, 50),
(51, 1, 51),
(52, 1, 52),
(53, 1, 53),
(54, 1, 54),
(55, 1, 55),
(56, 1, 56),
(57, 1, 57),
(58, 1, 58),
(59, 1, 59),
(60, 1, 60),
(61, 1, 61),
(62, 1, 62),
(63, 1, 63),
(64, 1, 64),
(65, 1, 65),
(66, 1, 66),
(67, 1, 67),
(68, 1, 68),
(69, 1, 69),
(70, 1, 70),
(71, 1, 71),
(72, 1, 72),
(73, 1, 73),
(74, 1, 74),
(75, 1, 75),
(76, 1, 76),
(77, 1, 77),
(78, 1, 78),
(79, 1, 79),
(80, 1, 80),
(81, 1, 81),
(82, 1, 82),
(83, 1, 83),
(84, 1, 84),
(85, 1, 85),
(86, 1, 86),
(87, 1, 87),
(88, 1, 88),
(89, 1, 89),
(90, 1, 90),
(91, 1, 91),
(92, 1, 92),
(93, 1, 93),
(94, 1, 94),
(95, 1, 95),
(96, 1, 96),
(97, 1, 97),
(98, 1, 98),
(99, 1, 99),
(100, 1, 100),
(101, 1, 101),
(102, 1, 102),
(103, 1, 103),
(104, 1, 104),
(105, 1, 105),
(106, 1, 106),
(107, 1, 107),
(108, 1, 108),
(109, 1, 109),
(110, 1, 110),
(111, 1, 111),
(112, 1, 112),
(113, 1, 113),
(114, 1, 114),
(115, 1, 115),
(116, 1, 116),
(117, 1, 117),
(118, 1, 118),
(119, 1, 119),
(120, 1, 120),
(121, 1, 121),
(122, 1, 122),
(123, 1, 123),
(124, 1, 124),
(125, 1, 125),
(126, 1, 126),
(127, 1, 127),
(128, 1, 128),
(129, 1, 129),
(130, 1, 130),
(131, 1, 131),
(132, 1, 132),
(133, 1, 133),
(134, 1, 134),
(135, 1, 135),
(136, 1, 136),
(137, 1, 137),
(138, 1, 138),
(139, 1, 139),
(140, 1, 140),
(141, 1, 141),
(142, 1, 142),
(143, 1, 143),
(144, 1, 144),
(145, 1, 145),
(146, 1, 146),
(147, 1, 147),
(148, 1, 148),
(149, 1, 149),
(150, 1, 150),
(151, 1, 151),
(152, 1, 152),
(153, 1, 153),
(154, 1, 154),
(155, 1, 155),
(156, 1, 156),
(157, 1, 157),
(158, 1, 158),
(159, 1, 159),
(160, 1, 160),
(161, 1, 161),
(162, 1, 162),
(163, 1, 163),
(164, 1, 164),
(165, 1, 165),
(166, 1, 166),
(167, 1, 167),
(168, 1, 168),
(169, 1, 169),
(170, 1, 170),
(171, 1, 171),
(172, 1, 172),
(173, 1, 173),
(174, 1, 174),
(175, 1, 175),
(176, 1, 176),
(177, 1, 177),
(178, 1, 178),
(179, 1, 179),
(180, 1, 180),
(181, 1, 181),
(182, 1, 182),
(183, 1, 183),
(184, 1, 184),
(185, 1, 185),
(186, 1, 186),
(187, 1, 187),
(188, 1, 188),
(189, 1, 189),
(190, 1, 190),
(191, 1, 191),
(192, 1, 192),
(193, 1, 193),
(194, 1, 194),
(195, 1, 195),
(196, 1, 196),
(197, 1, 197),
(198, 1, 198),
(199, 1, 199),
(200, 1, 200),
(201, 1, 201),
(202, 1, 202),
(203, 1, 203),
(204, 1, 204),
(205, 1, 205),
(206, 1, 206),
(207, 1, 207),
(208, 1, 208),
(209, 1, 209),
(210, 1, 210),
(211, 1, 211),
(212, 1, 212),
(213, 1, 213),
(214, 1, 214),
(215, 1, 215),
(216, 1, 216),
(217, 1, 217),
(218, 1, 218),
(219, 1, 219),
(220, 1, 220),
(221, 1, 221),
(222, 1, 222),
(223, 1, 223),
(224, 1, 224),
(225, 1, 225),
(226, 1, 226),
(227, 1, 227),
(228, 1, 228),
(229, 1, 229),
(230, 1, 230),
(231, 1, 231),
(232, 1, 232),
(233, 1, 233),
(234, 1, 234),
(235, 1, 235),
(236, 1, 236),
(237, 1, 237),
(238, 1, 238),
(239, 1, 239),
(240, 1, 240),
(241, 1, 241),
(242, 1, 242),
(243, 1, 243),
(244, 1, 244),
(245, 1, 245),
(246, 1, 246),
(247, 1, 247),
(248, 1, 248),
(249, 1, 249),
(250, 1, 250),
(251, 1, 251),
(252, 1, 252),
(253, 1, 253),
(254, 1, 254),
(255, 1, 255),
(256, 1, 256),
(257, 1, 257),
(258, 1, 258),
(259, 1, 259),
(260, 1, 260),
(261, 1, 261),
(262, 1, 262),
(263, 1, 263),
(264, 1, 264),
(265, 1, 265),
(266, 1, 266),
(267, 1, 267),
(268, 1, 268),
(269, 1, 269),
(270, 1, 270),
(271, 1, 271),
(272, 1, 272),
(273, 1, 273),
(274, 1, 274),
(275, 1, 275),
(276, 1, 276),
(277, 1, 277),
(278, 1, 278),
(279, 1, 279),
(280, 1, 280),
(281, 1, 281),
(282, 1, 282),
(283, 1, 283),
(284, 1, 284),
(285, 1, 285),
(286, 1, 286),
(287, 1, 287),
(288, 1, 288),
(289, 1, 289),
(290, 1, 290),
(291, 1, 291),
(292, 1, 292),
(293, 1, 293),
(294, 1, 294),
(295, 1, 295),
(296, 1, 296),
(297, 1, 297),
(298, 1, 298),
(299, 1, 299),
(300, 1, 300),
(301, 1, 301),
(302, 1, 302),
(303, 1, 303),
(304, 1, 304),
(305, 1, 305),
(306, 1, 306),
(307, 1, 307),
(308, 1, 308),
(309, 1, 309),
(310, 1, 310),
(311, 1, 311),
(312, 1, 312),
(313, 1, 313),
(314, 1, 314),
(315, 1, 315),
(316, 1, 316),
(317, 1, 317),
(318, 1, 318),
(319, 1, 319),
(320, 1, 320),
(321, 1, 321),
(322, 1, 322),
(323, 1, 323),
(324, 1, 324),
(325, 1, 325),
(326, 1, 326),
(327, 1, 327),
(328, 1, 328),
(329, 1, 329),
(330, 1, 330),
(331, 1, 331),
(332, 1, 332),
(333, 1, 333),
(334, 1, 334),
(335, 1, 335),
(336, 1, 336),
(337, 1, 337),
(338, 1, 338),
(339, 1, 339),
(340, 1, 340),
(341, 1, 341),
(342, 1, 342),
(343, 1, 343),
(344, 1, 344),
(345, 1, 345),
(346, 1, 346),
(347, 1, 347),
(348, 1, 348),
(349, 1, 349),
(350, 1, 350),
(351, 1, 351),
(352, 1, 352),
(353, 1, 353),
(354, 1, 354),
(355, 1, 355),
(356, 1, 356),
(357, 1, 357),
(358, 1, 358),
(359, 1, 359),
(360, 1, 360),
(361, 1, 361),
(362, 1, 362),
(363, 1, 363),
(364, 1, 364),
(365, 1, 365),
(366, 1, 366),
(367, 1, 367),
(368, 1, 368),
(369, 1, 369),
(370, 1, 370),
(371, 1, 371),
(372, 1, 372),
(373, 1, 373),
(374, 1, 374),
(375, 1, 375),
(376, 1, 376),
(377, 1, 377),
(378, 1, 378),
(379, 1, 379),
(380, 1, 380),
(381, 1, 381),
(382, 1, 382),
(383, 1, 383),
(384, 1, 384),
(385, 1, 385),
(386, 1, 386),
(387, 1, 387),
(388, 1, 388),
(389, 1, 389),
(390, 1, 390),
(391, 1, 391),
(392, 1, 392),
(393, 1, 393),
(394, 1, 394),
(395, 1, 395),
(396, 1, 396),
(397, 1, 397),
(398, 1, 398),
(399, 1, 399),
(400, 1, 400),
(401, 1, 401),
(402, 1, 402),
(403, 1, 403),
(404, 1, 404),
(405, 1, 405),
(406, 1, 406),
(407, 1, 407),
(408, 1, 408),
(409, 1, 409),
(410, 1, 410),
(411, 1, 411),
(412, 1, 412),
(413, 1, 413),
(414, 1, 414),
(415, 1, 415),
(416, 1, 416),
(417, 1, 417),
(418, 1, 418),
(419, 1, 419),
(420, 1, 420),
(421, 1, 421),
(422, 1, 422),
(423, 1, 423),
(424, 1, 424),
(425, 1, 425),
(426, 1, 426),
(427, 1, 427),
(428, 1, 428),
(429, 1, 429),
(430, 1, 430),
(431, 1, 431),
(432, 1, 432),
(433, 1, 433),
(434, 1, 434),
(435, 1, 435),
(436, 1, 436),
(437, 1, 437),
(438, 1, 438),
(439, 1, 439),
(440, 1, 440),
(441, 1, 441),
(442, 1, 442),
(443, 1, 443),
(444, 1, 444),
(445, 1, 445),
(446, 1, 446),
(447, 1, 447),
(448, 1, 448),
(449, 1, 449),
(450, 1, 450),
(451, 1, 451),
(452, 1, 452),
(453, 1, 453),
(454, 1, 454),
(455, 1, 455),
(456, 1, 456),
(457, 1, 457),
(458, 1, 458),
(459, 1, 459),
(460, 1, 460),
(461, 1, 461),
(462, 1, 462),
(463, 1, 463),
(464, 1, 464),
(465, 1, 465),
(466, 1, 466),
(467, 1, 467),
(468, 1, 468),
(469, 1, 469),
(470, 1, 470),
(471, 1, 471),
(472, 1, 472),
(473, 1, 473),
(474, 1, 474),
(475, 1, 475),
(476, 1, 476),
(477, 1, 477),
(478, 1, 478),
(479, 1, 479),
(480, 1, 480),
(481, 1, 481),
(482, 1, 482),
(483, 1, 483),
(484, 1, 484),
(485, 1, 485),
(486, 1, 486),
(487, 1, 487),
(488, 1, 488),
(489, 1, 489),
(490, 1, 490),
(491, 1, 491),
(492, 1, 492),
(493, 1, 493),
(494, 1, 494),
(495, 1, 495),
(496, 1, 496),
(497, 1, 497),
(498, 1, 498),
(499, 1, 499),
(500, 1, 500),
(501, 1, 501),
(502, 1, 502),
(503, 1, 503),
(504, 1, 504),
(505, 1, 505),
(506, 1, 506),
(507, 1, 507),
(508, 1, 508),
(509, 1, 509),
(510, 1, 510),
(511, 1, 511),
(512, 1, 512),
(513, 1, 513),
(514, 1, 514),
(515, 1, 515),
(516, 1, 516),
(517, 1, 517),
(518, 1, 518),
(519, 1, 519),
(520, 1, 520),
(521, 1, 521),
(522, 1, 522),
(523, 1, 523),
(524, 1, 524),
(525, 1, 525),
(526, 1, 526),
(527, 1, 527),
(528, 1, 528),
(529, 1, 529),
(530, 1, 530),
(531, 1, 531),
(532, 1, 532),
(533, 1, 533),
(534, 1, 534),
(535, 1, 535),
(536, 1, 536),
(537, 1, 537),
(538, 1, 538),
(539, 1, 539),
(540, 1, 540),
(541, 2, 1),
(542, 2, 2),
(543, 2, 3),
(544, 2, 4),
(545, 2, 5),
(546, 2, 6),
(547, 2, 7),
(548, 2, 8),
(549, 2, 9),
(550, 2, 10),
(551, 2, 11),
(552, 2, 12),
(553, 2, 13),
(554, 2, 14),
(555, 2, 15),
(556, 2, 16),
(557, 2, 17),
(558, 2, 18),
(559, 2, 19),
(560, 2, 20),
(561, 2, 21),
(562, 2, 22),
(563, 2, 23),
(564, 2, 24),
(565, 2, 25),
(566, 2, 26),
(567, 2, 27),
(568, 2, 28),
(569, 2, 29),
(570, 2, 30),
(571, 2, 31),
(572, 2, 32),
(573, 2, 33),
(574, 2, 34),
(575, 2, 35),
(576, 2, 36),
(577, 2, 37),
(578, 2, 38),
(579, 2, 39),
(580, 2, 40),
(581, 2, 41),
(582, 2, 42),
(583, 2, 43),
(584, 2, 44),
(585, 2, 45),
(586, 2, 46),
(587, 2, 47),
(588, 2, 48),
(589, 2, 49),
(590, 2, 50),
(591, 2, 51),
(592, 2, 52),
(593, 2, 53),
(594, 2, 54),
(595, 2, 55),
(596, 2, 56),
(597, 2, 57),
(598, 2, 58),
(599, 2, 59),
(600, 2, 60),
(601, 2, 61),
(602, 2, 62),
(603, 2, 63),
(604, 2, 64),
(605, 2, 65),
(606, 2, 66),
(607, 2, 67),
(608, 2, 68),
(609, 2, 69),
(610, 2, 70),
(611, 2, 71),
(612, 2, 72),
(613, 2, 73),
(614, 2, 74),
(615, 2, 75),
(616, 2, 76),
(617, 2, 77),
(618, 2, 78),
(619, 2, 79),
(620, 2, 80),
(621, 2, 81),
(622, 2, 82),
(623, 2, 83),
(624, 2, 84),
(625, 2, 85),
(626, 2, 86),
(627, 2, 87),
(628, 2, 88),
(629, 2, 89),
(630, 2, 90),
(631, 2, 91),
(632, 2, 92),
(633, 2, 93),
(634, 2, 94),
(635, 2, 95),
(636, 2, 96),
(637, 2, 97),
(638, 2, 98),
(639, 2, 99),
(640, 2, 100),
(641, 2, 101),
(642, 2, 102),
(643, 2, 103),
(644, 2, 104),
(645, 2, 105),
(646, 2, 106),
(647, 2, 107),
(648, 2, 108),
(649, 2, 109),
(650, 2, 110),
(651, 2, 111),
(652, 2, 112),
(653, 2, 113),
(654, 2, 114),
(655, 2, 115),
(656, 2, 116),
(657, 2, 117),
(658, 2, 118),
(659, 2, 119),
(660, 2, 120),
(661, 2, 121),
(662, 2, 122),
(663, 2, 123),
(664, 2, 124),
(665, 2, 125),
(666, 2, 126),
(667, 2, 127),
(668, 2, 128),
(669, 2, 129),
(670, 2, 130),
(671, 2, 131),
(672, 2, 132),
(673, 2, 133),
(674, 2, 134),
(675, 2, 135),
(676, 2, 136),
(677, 2, 137),
(678, 2, 138),
(679, 2, 139),
(680, 2, 140),
(681, 2, 141),
(682, 2, 142),
(683, 2, 143),
(684, 2, 144),
(685, 2, 145),
(686, 2, 146),
(687, 2, 147),
(688, 2, 148),
(689, 2, 149),
(690, 2, 150),
(691, 2, 151),
(692, 2, 152),
(693, 2, 153),
(694, 2, 154),
(695, 2, 155),
(696, 2, 156),
(697, 2, 157),
(698, 2, 158),
(699, 2, 159),
(700, 2, 160),
(701, 2, 161),
(702, 2, 162),
(703, 2, 163),
(704, 2, 164),
(705, 2, 165),
(706, 2, 166),
(707, 2, 167),
(708, 2, 168),
(709, 2, 169),
(710, 2, 170),
(711, 2, 171),
(712, 2, 172),
(713, 2, 173),
(714, 2, 174),
(715, 2, 175),
(716, 2, 176),
(717, 2, 177),
(718, 2, 178),
(719, 2, 179),
(720, 2, 180),
(721, 2, 181),
(722, 2, 182),
(723, 2, 183),
(724, 2, 184),
(725, 2, 185),
(726, 2, 186),
(727, 2, 187),
(728, 2, 188),
(729, 2, 189),
(730, 2, 190),
(731, 2, 191),
(732, 2, 192),
(733, 2, 193),
(734, 2, 194),
(735, 2, 195),
(736, 2, 196),
(737, 2, 197),
(738, 2, 198),
(739, 2, 199),
(740, 2, 200),
(741, 2, 201),
(742, 2, 202),
(743, 2, 203),
(744, 2, 204),
(745, 2, 205),
(746, 2, 206),
(747, 2, 207),
(748, 2, 208),
(749, 2, 209),
(750, 2, 210),
(751, 2, 211),
(752, 2, 212),
(753, 2, 213),
(754, 2, 214),
(755, 2, 215),
(756, 2, 216),
(757, 2, 217),
(758, 2, 218),
(759, 2, 219),
(760, 2, 220),
(761, 2, 221),
(762, 2, 222),
(763, 2, 223),
(764, 2, 224),
(765, 2, 225),
(766, 2, 226),
(767, 2, 227),
(768, 2, 228),
(769, 2, 229),
(770, 2, 230),
(771, 2, 231),
(772, 2, 232),
(773, 2, 233),
(774, 2, 234),
(775, 2, 235),
(776, 2, 236),
(777, 2, 237),
(778, 2, 238),
(779, 2, 239),
(780, 2, 240),
(781, 2, 241),
(782, 2, 242),
(783, 2, 243),
(784, 2, 244),
(785, 2, 245),
(786, 2, 246),
(787, 2, 247),
(788, 2, 248),
(789, 2, 249),
(790, 2, 250),
(791, 2, 251),
(792, 2, 252),
(793, 2, 253),
(794, 2, 254),
(795, 2, 255),
(796, 2, 256),
(797, 2, 257),
(798, 2, 258),
(799, 2, 259),
(800, 2, 260),
(801, 2, 261),
(802, 2, 262),
(803, 2, 263),
(804, 2, 264),
(805, 2, 265),
(806, 2, 266),
(807, 2, 267),
(808, 2, 268),
(809, 2, 269),
(810, 2, 270),
(811, 2, 271),
(812, 2, 272),
(813, 2, 273),
(814, 2, 274),
(815, 2, 275),
(816, 2, 276),
(817, 2, 277),
(818, 2, 278),
(819, 2, 279),
(820, 2, 280),
(821, 2, 281),
(822, 2, 282),
(823, 2, 283),
(824, 2, 284),
(825, 2, 285),
(826, 2, 286),
(827, 2, 287),
(828, 2, 288),
(829, 2, 289),
(830, 2, 290),
(831, 2, 291),
(832, 2, 292),
(833, 2, 293),
(834, 2, 294),
(835, 2, 295),
(836, 2, 296),
(837, 2, 297),
(838, 2, 298),
(839, 2, 299),
(840, 2, 300),
(841, 2, 301),
(842, 2, 302),
(843, 2, 303),
(844, 2, 304),
(845, 2, 305),
(846, 2, 306),
(847, 2, 307),
(848, 2, 308),
(849, 2, 309),
(850, 2, 310),
(851, 2, 311),
(852, 2, 312),
(853, 2, 313),
(854, 2, 314),
(855, 2, 315),
(856, 2, 316),
(857, 2, 317),
(858, 2, 318),
(859, 2, 319),
(860, 2, 320),
(861, 2, 321),
(862, 2, 322),
(863, 2, 323),
(864, 2, 324),
(865, 2, 325),
(866, 2, 326),
(867, 2, 327),
(868, 2, 328),
(869, 2, 329),
(870, 2, 330),
(871, 2, 331),
(872, 2, 332),
(873, 2, 333),
(874, 2, 334),
(875, 2, 335),
(876, 2, 336),
(877, 2, 337),
(878, 2, 338),
(879, 2, 339),
(880, 2, 340),
(881, 2, 341),
(882, 2, 342),
(883, 2, 343),
(884, 2, 344),
(885, 2, 345),
(886, 2, 346),
(887, 2, 347),
(888, 2, 348),
(889, 2, 349),
(890, 2, 350),
(891, 2, 351),
(892, 2, 352),
(893, 2, 353),
(894, 2, 354),
(895, 2, 355),
(896, 2, 356),
(897, 2, 357),
(898, 2, 358),
(899, 2, 359),
(900, 2, 360),
(901, 2, 361),
(902, 2, 362),
(903, 2, 363),
(904, 2, 364),
(905, 2, 365),
(906, 2, 366),
(907, 2, 367),
(908, 2, 368),
(909, 2, 369),
(910, 2, 370),
(911, 2, 371),
(912, 2, 372),
(913, 2, 373),
(914, 2, 374),
(915, 2, 375),
(916, 2, 376),
(917, 2, 377),
(918, 2, 378),
(919, 2, 379),
(920, 2, 380),
(921, 2, 381),
(922, 2, 382),
(923, 2, 383),
(924, 2, 384),
(925, 2, 385),
(926, 2, 386),
(927, 2, 387),
(928, 2, 388),
(929, 2, 389),
(930, 2, 390),
(931, 2, 391),
(932, 2, 392),
(933, 2, 393),
(934, 2, 394),
(935, 2, 395),
(936, 2, 396),
(937, 2, 397),
(938, 2, 398),
(939, 2, 399),
(940, 2, 400),
(941, 2, 401),
(942, 2, 402),
(943, 2, 403),
(944, 2, 404),
(945, 2, 405),
(946, 2, 406),
(947, 2, 407),
(948, 2, 408),
(949, 2, 409),
(950, 2, 410),
(951, 2, 411),
(952, 2, 412),
(953, 2, 413),
(954, 2, 414),
(955, 2, 415),
(956, 2, 416),
(957, 2, 417),
(958, 2, 418),
(959, 2, 419),
(960, 2, 420),
(961, 2, 421),
(962, 2, 422),
(963, 2, 423),
(964, 2, 424),
(965, 2, 425),
(966, 2, 426),
(967, 2, 427),
(968, 2, 428),
(969, 2, 429),
(970, 2, 430),
(971, 2, 431),
(972, 2, 432),
(973, 2, 433),
(974, 2, 434),
(975, 2, 435),
(976, 2, 436),
(977, 2, 437),
(978, 2, 438),
(979, 2, 439),
(980, 2, 440),
(981, 2, 441),
(982, 2, 442),
(983, 2, 443),
(984, 2, 444),
(985, 2, 445),
(986, 2, 446),
(987, 2, 447),
(988, 2, 448),
(989, 2, 449),
(990, 2, 450),
(991, 2, 451),
(992, 2, 452),
(993, 2, 453),
(994, 2, 454),
(995, 2, 455),
(996, 2, 456),
(997, 2, 457),
(998, 2, 458),
(999, 2, 459),
(1000, 2, 460),
(1001, 2, 461),
(1002, 2, 462),
(1003, 2, 463),
(1004, 2, 464),
(1005, 2, 465),
(1006, 2, 466),
(1007, 2, 467),
(1008, 2, 468),
(1009, 2, 469),
(1010, 2, 470),
(1011, 2, 471),
(1012, 2, 472),
(1013, 2, 473),
(1014, 2, 474),
(1015, 2, 475),
(1016, 2, 476),
(1017, 2, 477),
(1018, 2, 478),
(1019, 2, 479),
(1020, 2, 480),
(1021, 2, 481),
(1022, 2, 482),
(1023, 2, 483),
(1024, 2, 484),
(1025, 2, 485),
(1026, 2, 486),
(1027, 2, 487),
(1028, 2, 488),
(1029, 2, 489),
(1030, 2, 490),
(1031, 2, 491),
(1032, 2, 492),
(1033, 2, 493),
(1034, 2, 494),
(1035, 2, 495),
(1036, 2, 496),
(1037, 2, 497),
(1038, 2, 498),
(1039, 2, 499),
(1040, 2, 500),
(1041, 2, 501),
(1042, 2, 502),
(1043, 2, 503),
(1044, 2, 504),
(1045, 2, 505),
(1046, 2, 506),
(1047, 2, 507),
(1048, 2, 508),
(1049, 2, 509),
(1050, 2, 510),
(1051, 2, 511),
(1052, 2, 512),
(1053, 2, 513),
(1054, 2, 514),
(1055, 2, 515),
(1056, 2, 516),
(1057, 2, 517),
(1058, 2, 518),
(1059, 2, 519),
(1060, 2, 520),
(1061, 2, 521),
(1062, 2, 522),
(1063, 2, 523),
(1064, 2, 524),
(1065, 2, 525),
(1066, 2, 526),
(1067, 2, 527),
(1068, 2, 528),
(1069, 2, 529),
(1070, 2, 530),
(1071, 2, 531),
(1072, 2, 532),
(1073, 2, 533),
(1074, 2, 534),
(1075, 2, 535),
(1076, 2, 536),
(1077, 2, 537),
(1078, 2, 538),
(1079, 2, 539),
(1080, 2, 540),
(1081, 3, 1),
(1082, 3, 2),
(1083, 3, 3),
(1084, 3, 4),
(1085, 3, 5),
(1086, 3, 6),
(1087, 3, 7),
(1088, 3, 8),
(1089, 3, 9),
(1090, 3, 10),
(1091, 3, 11),
(1092, 3, 12),
(1093, 3, 13),
(1094, 3, 14),
(1095, 3, 15),
(1096, 3, 16),
(1097, 3, 17),
(1098, 3, 18),
(1099, 3, 19),
(1100, 3, 20),
(1101, 3, 21),
(1102, 3, 22),
(1103, 3, 23),
(1104, 3, 24),
(1105, 3, 25),
(1106, 3, 26),
(1107, 3, 27),
(1108, 3, 28),
(1109, 3, 29),
(1110, 3, 30),
(1111, 3, 31),
(1112, 3, 32),
(1113, 3, 33),
(1114, 3, 34),
(1115, 3, 35),
(1116, 3, 36),
(1117, 3, 37),
(1118, 3, 38),
(1119, 3, 39),
(1120, 3, 40),
(1121, 3, 41),
(1122, 3, 42),
(1123, 3, 43),
(1124, 3, 44),
(1125, 3, 45),
(1126, 3, 46),
(1127, 3, 47),
(1128, 3, 48),
(1129, 3, 49),
(1130, 3, 50),
(1131, 3, 51),
(1132, 3, 52),
(1133, 3, 53),
(1134, 3, 54),
(1135, 3, 55),
(1136, 3, 56),
(1137, 3, 57),
(1138, 3, 58),
(1139, 3, 59),
(1140, 3, 60),
(1141, 3, 61),
(1142, 3, 62),
(1143, 3, 63),
(1144, 3, 64),
(1145, 3, 65),
(1146, 3, 66),
(1147, 3, 67),
(1148, 3, 68),
(1149, 3, 69),
(1150, 3, 70),
(1151, 3, 71),
(1152, 3, 72),
(1153, 3, 73),
(1154, 3, 74),
(1155, 3, 75),
(1156, 3, 76),
(1157, 3, 77),
(1158, 3, 78),
(1159, 3, 79),
(1160, 3, 80),
(1161, 3, 81),
(1162, 3, 82),
(1163, 3, 83),
(1164, 3, 84),
(1165, 3, 85),
(1166, 3, 86),
(1167, 3, 87),
(1168, 3, 88),
(1169, 3, 89),
(1170, 3, 90),
(1171, 3, 91),
(1172, 3, 92),
(1173, 3, 93),
(1174, 3, 94),
(1175, 3, 95),
(1176, 3, 96),
(1177, 3, 97),
(1178, 3, 98),
(1179, 3, 99),
(1180, 3, 100),
(1181, 3, 101),
(1182, 3, 102),
(1183, 3, 103),
(1184, 3, 104),
(1185, 3, 105),
(1186, 3, 106),
(1187, 3, 107),
(1188, 3, 108),
(1189, 3, 109),
(1190, 3, 110),
(1191, 3, 111),
(1192, 3, 112),
(1193, 3, 113),
(1194, 3, 114),
(1195, 3, 115),
(1196, 3, 116),
(1197, 3, 117),
(1198, 3, 118),
(1199, 3, 119),
(1200, 3, 120),
(1201, 3, 121),
(1202, 3, 122),
(1203, 3, 123),
(1204, 3, 124),
(1205, 3, 125),
(1206, 3, 126),
(1207, 3, 127),
(1208, 3, 128),
(1209, 3, 129),
(1210, 3, 130),
(1211, 3, 131),
(1212, 3, 132),
(1213, 3, 133),
(1214, 3, 134),
(1215, 3, 135),
(1216, 3, 136),
(1217, 3, 137),
(1218, 3, 138),
(1219, 3, 139),
(1220, 3, 140),
(1221, 3, 141),
(1222, 3, 142),
(1223, 3, 143),
(1224, 3, 144),
(1225, 3, 145),
(1226, 3, 146),
(1227, 3, 147),
(1228, 3, 148),
(1229, 3, 149),
(1230, 3, 150),
(1231, 3, 151),
(1232, 3, 152),
(1233, 3, 153),
(1234, 3, 154),
(1235, 3, 155),
(1236, 3, 156),
(1237, 3, 157),
(1238, 3, 158),
(1239, 3, 159),
(1240, 3, 160),
(1241, 3, 161),
(1242, 3, 162),
(1243, 3, 163),
(1244, 3, 164),
(1245, 3, 165),
(1246, 3, 166),
(1247, 3, 167),
(1248, 3, 168),
(1249, 3, 169),
(1250, 3, 170),
(1251, 3, 171),
(1252, 3, 172),
(1253, 3, 173),
(1254, 3, 174),
(1255, 3, 175),
(1256, 3, 176),
(1257, 3, 177),
(1258, 3, 178),
(1259, 3, 179),
(1260, 3, 180),
(1261, 3, 181),
(1262, 3, 182),
(1263, 3, 183),
(1264, 3, 184),
(1265, 3, 185),
(1266, 3, 186),
(1267, 3, 187),
(1268, 3, 188),
(1269, 3, 189),
(1270, 3, 190),
(1271, 3, 191),
(1272, 3, 192),
(1273, 3, 193),
(1274, 3, 194),
(1275, 3, 195),
(1276, 3, 196),
(1277, 3, 197),
(1278, 3, 198),
(1279, 3, 199),
(1280, 3, 200),
(1281, 3, 201),
(1282, 3, 202),
(1283, 3, 203),
(1284, 3, 204),
(1285, 3, 205),
(1286, 3, 206),
(1287, 3, 207),
(1288, 3, 208),
(1289, 3, 209),
(1290, 3, 210),
(1291, 3, 211),
(1292, 3, 212),
(1293, 3, 213),
(1294, 3, 214),
(1295, 3, 215),
(1296, 3, 216),
(1297, 3, 217),
(1298, 3, 218),
(1299, 3, 219),
(1300, 3, 220),
(1301, 3, 221),
(1302, 3, 222),
(1303, 3, 223),
(1304, 3, 224),
(1305, 3, 225),
(1306, 3, 226),
(1307, 3, 227),
(1308, 3, 228),
(1309, 3, 229),
(1310, 3, 230),
(1311, 3, 231),
(1312, 3, 232),
(1313, 3, 233),
(1314, 3, 234),
(1315, 3, 235),
(1316, 3, 236),
(1317, 3, 237),
(1318, 3, 238),
(1319, 3, 239),
(1320, 3, 240),
(1321, 3, 241),
(1322, 3, 242),
(1323, 3, 243),
(1324, 3, 244),
(1325, 3, 245),
(1326, 3, 246),
(1327, 3, 247),
(1328, 3, 248),
(1329, 3, 249),
(1330, 3, 250),
(1331, 3, 251),
(1332, 3, 252),
(1333, 3, 253),
(1334, 3, 254),
(1335, 3, 255),
(1336, 3, 256),
(1337, 3, 257),
(1338, 3, 258),
(1339, 3, 259),
(1340, 3, 260),
(1341, 3, 261),
(1342, 3, 262),
(1343, 3, 263),
(1344, 3, 264),
(1345, 3, 265),
(1346, 3, 266),
(1347, 3, 267),
(1348, 3, 268),
(1349, 3, 269),
(1350, 3, 270),
(1351, 3, 271),
(1352, 3, 272),
(1353, 3, 273),
(1354, 3, 274),
(1355, 3, 275),
(1356, 3, 276),
(1357, 3, 277),
(1358, 3, 278),
(1359, 3, 279),
(1360, 3, 280),
(1361, 3, 281),
(1362, 3, 282),
(1363, 3, 283),
(1364, 3, 284),
(1365, 3, 285),
(1366, 3, 286),
(1367, 3, 287),
(1368, 3, 288),
(1369, 3, 289),
(1370, 3, 290),
(1371, 3, 291),
(1372, 3, 292),
(1373, 3, 293),
(1374, 3, 294),
(1375, 3, 295),
(1376, 3, 296),
(1377, 3, 297),
(1378, 3, 298),
(1379, 3, 299),
(1380, 3, 300),
(1381, 3, 301),
(1382, 3, 302),
(1383, 3, 303),
(1384, 3, 304),
(1385, 3, 305),
(1386, 3, 306),
(1387, 3, 307),
(1388, 3, 308),
(1389, 3, 309),
(1390, 3, 310),
(1391, 3, 311),
(1392, 3, 312),
(1393, 3, 313),
(1394, 3, 314),
(1395, 3, 315),
(1396, 3, 316),
(1397, 3, 317),
(1398, 3, 318),
(1399, 3, 319),
(1400, 3, 320),
(1401, 3, 321),
(1402, 3, 322),
(1403, 3, 323),
(1404, 3, 324),
(1405, 3, 325),
(1406, 3, 326),
(1407, 3, 327),
(1408, 3, 328),
(1409, 3, 329),
(1410, 3, 330),
(1411, 3, 331),
(1412, 3, 332),
(1413, 3, 333),
(1414, 3, 334),
(1415, 3, 335),
(1416, 3, 336),
(1417, 3, 337),
(1418, 3, 338),
(1419, 3, 339),
(1420, 3, 340),
(1421, 3, 341),
(1422, 3, 342),
(1423, 3, 343),
(1424, 3, 344),
(1425, 3, 345),
(1426, 3, 346),
(1427, 3, 347),
(1428, 3, 348),
(1429, 3, 349),
(1430, 3, 350),
(1431, 3, 351),
(1432, 3, 352),
(1433, 3, 353),
(1434, 3, 354),
(1435, 3, 355),
(1436, 3, 356),
(1437, 3, 357),
(1438, 3, 358),
(1439, 3, 359),
(1440, 3, 360),
(1441, 3, 361),
(1442, 3, 362),
(1443, 3, 363),
(1444, 3, 364),
(1445, 3, 365),
(1446, 3, 366),
(1447, 3, 367),
(1448, 3, 368),
(1449, 3, 369),
(1450, 3, 370),
(1451, 3, 371),
(1452, 3, 372),
(1453, 3, 373),
(1454, 3, 374),
(1455, 3, 375),
(1456, 3, 376),
(1457, 3, 377),
(1458, 3, 378),
(1459, 3, 379),
(1460, 3, 380),
(1461, 3, 381),
(1462, 3, 382),
(1463, 3, 383),
(1464, 3, 384),
(1465, 3, 385),
(1466, 3, 386),
(1467, 3, 387),
(1468, 3, 388),
(1469, 3, 389),
(1470, 3, 390),
(1471, 3, 391),
(1472, 3, 392),
(1473, 3, 393),
(1474, 3, 394),
(1475, 3, 395),
(1476, 3, 396),
(1477, 3, 397),
(1478, 3, 398),
(1479, 3, 399),
(1480, 3, 400),
(1481, 3, 401),
(1482, 3, 402),
(1483, 3, 403),
(1484, 3, 404),
(1485, 3, 405),
(1486, 3, 406),
(1487, 3, 407),
(1488, 3, 408),
(1489, 3, 409),
(1490, 3, 410),
(1491, 3, 411),
(1492, 3, 412),
(1493, 3, 413),
(1494, 3, 414),
(1495, 3, 415),
(1496, 3, 416),
(1497, 3, 417),
(1498, 3, 418),
(1499, 3, 419),
(1500, 3, 420),
(1501, 3, 421),
(1502, 3, 422),
(1503, 3, 423),
(1504, 3, 424),
(1505, 3, 425),
(1506, 3, 426),
(1507, 3, 427),
(1508, 3, 428),
(1509, 3, 429),
(1510, 3, 430),
(1511, 3, 431),
(1512, 3, 432),
(1513, 3, 433),
(1514, 3, 434),
(1515, 3, 435),
(1516, 3, 436),
(1517, 3, 437),
(1518, 3, 438),
(1519, 3, 439),
(1520, 3, 440),
(1521, 3, 441),
(1522, 3, 442),
(1523, 3, 443),
(1524, 3, 444),
(1525, 3, 445),
(1526, 3, 446),
(1527, 3, 447),
(1528, 3, 448),
(1529, 3, 449),
(1530, 3, 450),
(1531, 3, 451),
(1532, 3, 452),
(1533, 3, 453),
(1534, 3, 454),
(1535, 3, 455),
(1536, 3, 456),
(1537, 3, 457),
(1538, 3, 458),
(1539, 3, 459),
(1540, 3, 460),
(1541, 3, 461),
(1542, 3, 462),
(1543, 3, 463),
(1544, 3, 464),
(1545, 3, 465),
(1546, 3, 466),
(1547, 3, 467),
(1548, 3, 468),
(1549, 3, 469),
(1550, 3, 470),
(1551, 3, 471),
(1552, 3, 472),
(1553, 3, 473),
(1554, 3, 474),
(1555, 3, 475),
(1556, 3, 476),
(1557, 3, 477),
(1558, 3, 478),
(1559, 3, 479),
(1560, 3, 480),
(1561, 3, 481),
(1562, 3, 482),
(1563, 3, 483),
(1564, 3, 484),
(1565, 3, 485),
(1566, 3, 486),
(1567, 3, 487),
(1568, 3, 488),
(1569, 3, 489),
(1570, 3, 490),
(1571, 3, 491),
(1572, 3, 492),
(1573, 3, 493),
(1574, 3, 494),
(1575, 3, 495),
(1576, 3, 496),
(1577, 3, 497),
(1578, 3, 498),
(1579, 3, 499),
(1580, 3, 500),
(1581, 3, 501),
(1582, 3, 502),
(1583, 3, 503),
(1584, 3, 504),
(1585, 3, 505),
(1586, 3, 506),
(1587, 3, 507),
(1588, 3, 508),
(1589, 3, 509),
(1590, 3, 510),
(1591, 3, 511),
(1592, 3, 512),
(1593, 3, 513),
(1594, 3, 514),
(1595, 3, 515),
(1596, 3, 516),
(1597, 3, 517),
(1598, 3, 518),
(1599, 3, 519),
(1600, 3, 520),
(1601, 3, 521),
(1602, 3, 522),
(1603, 3, 523),
(1604, 3, 524),
(1605, 3, 525),
(1606, 3, 526),
(1607, 3, 527),
(1608, 3, 528),
(1609, 3, 529),
(1610, 3, 530),
(1611, 3, 531),
(1612, 3, 532),
(1613, 3, 533),
(1614, 3, 534),
(1615, 3, 535),
(1616, 3, 536),
(1617, 3, 537),
(1618, 3, 538),
(1619, 3, 539),
(1620, 3, 540);

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add AbsenceType', 7, 'add_absencetypemodel'),
(26, 'Can change AbsenceType', 7, 'change_absencetypemodel'),
(27, 'Can delete AbsenceType', 7, 'delete_absencetypemodel'),
(28, 'Can view AbsenceType', 7, 'view_absencetypemodel'),
(29, 'Can add Account', 8, 'add_accountmodel'),
(30, 'Can change Account', 8, 'change_accountmodel'),
(31, 'Can delete Account', 8, 'delete_accountmodel'),
(32, 'Can view Account', 8, 'view_accountmodel'),
(33, 'Can add Asset', 9, 'add_assetmodel'),
(34, 'Can change Asset', 9, 'change_assetmodel'),
(35, 'Can delete Asset', 9, 'delete_assetmodel'),
(36, 'Can view Asset', 9, 'view_assetmodel'),
(37, 'Can add BenefitCalculation', 10, 'add_benefitcalculationmodel'),
(38, 'Can change BenefitCalculation', 10, 'change_benefitcalculationmodel'),
(39, 'Can delete BenefitCalculation', 10, 'delete_benefitcalculationmodel'),
(40, 'Can view BenefitCalculation', 10, 'view_benefitcalculationmodel'),
(41, 'Can add BenefitType', 11, 'add_benefittypemodel'),
(42, 'Can change BenefitType', 11, 'change_benefittypemodel'),
(43, 'Can delete BenefitType', 11, 'delete_benefittypemodel'),
(44, 'Can view BenefitType', 11, 'view_benefittypemodel'),
(45, 'Can add Bill', 12, 'add_billmodel'),
(46, 'Can change Bill', 12, 'change_billmodel'),
(47, 'Can delete Bill', 12, 'delete_billmodel'),
(48, 'Can view Bill', 12, 'view_billmodel'),
(49, 'Can add BusinessIndustry', 13, 'add_businessindustrymodel'),
(50, 'Can change BusinessIndustry', 13, 'change_businessindustrymodel'),
(51, 'Can delete BusinessIndustry', 13, 'delete_businessindustrymodel'),
(52, 'Can view BusinessIndustry', 13, 'view_businessindustrymodel'),
(53, 'Can add Currency', 14, 'add_currencymodel'),
(54, 'Can change Currency', 14, 'change_currencymodel'),
(55, 'Can delete Currency', 14, 'delete_currencymodel'),
(56, 'Can view Currency', 14, 'view_currencymodel'),
(57, 'Can add Customer Location', 15, 'add_customerlocationmodel'),
(58, 'Can change Customer Location', 15, 'change_customerlocationmodel'),
(59, 'Can delete Customer Location', 15, 'delete_customerlocationmodel'),
(60, 'Can view Customer Location', 15, 'view_customerlocationmodel'),
(61, 'Can add Customer', 16, 'add_customermodel'),
(62, 'Can change Customer', 16, 'change_customermodel'),
(63, 'Can delete Customer', 16, 'delete_customermodel'),
(64, 'Can view Customer', 16, 'view_customermodel'),
(65, 'Can add Department', 17, 'add_departmentmodel'),
(66, 'Can change Department', 17, 'change_departmentmodel'),
(67, 'Can delete Department', 17, 'delete_departmentmodel'),
(68, 'Can view Department', 17, 'view_departmentmodel'),
(69, 'Can add Employee', 18, 'add_employeemodel'),
(70, 'Can change Employee', 18, 'change_employeemodel'),
(71, 'Can delete Employee', 18, 'delete_employeemodel'),
(72, 'Can view Employee', 18, 'view_employeemodel'),
(73, 'Can add Entity Manager', 19, 'add_entitymanagementmodel'),
(74, 'Can change Entity Manager', 19, 'change_entitymanagementmodel'),
(75, 'Can delete Entity Manager', 19, 'delete_entitymanagementmodel'),
(76, 'Can view Entity Manager', 19, 'view_entitymanagementmodel'),
(77, 'Can add Entity', 20, 'add_entitymodel'),
(78, 'Can change Entity', 20, 'change_entitymodel'),
(79, 'Can delete Entity', 20, 'delete_entitymodel'),
(80, 'Can view Entity', 20, 'view_entitymodel'),
(81, 'Can add Branch Model', 21, 'add_entityunitmodel'),
(82, 'Can change Branch Model', 21, 'change_entityunitmodel'),
(83, 'Can delete Branch Model', 21, 'delete_entityunitmodel'),
(84, 'Can view Branch Model', 21, 'view_entityunitmodel'),
(85, 'Can add Customer Job', 22, 'add_estimatemodel'),
(86, 'Can change Customer Job', 22, 'change_estimatemodel'),
(87, 'Can delete Customer Job', 22, 'delete_estimatemodel'),
(88, 'Can view Customer Job', 22, 'view_estimatemodel'),
(89, 'Can add ImmigrationDetail', 23, 'add_immigrationdetailmodel'),
(90, 'Can change ImmigrationDetail', 23, 'change_immigrationdetailmodel'),
(91, 'Can delete ImmigrationDetail', 23, 'delete_immigrationdetailmodel'),
(92, 'Can view ImmigrationDetail', 23, 'view_immigrationdetailmodel'),
(93, 'Can add Import Job Model', 24, 'add_importjobmodel'),
(94, 'Can change Import Job Model', 24, 'change_importjobmodel'),
(95, 'Can delete Import Job Model', 24, 'delete_importjobmodel'),
(96, 'Can view Import Job Model', 24, 'view_importjobmodel'),
(97, 'Can add Invoice', 25, 'add_invoicemodel'),
(98, 'Can change Invoice', 25, 'change_invoicemodel'),
(99, 'Can delete Invoice', 25, 'delete_invoicemodel'),
(100, 'Can view Invoice', 25, 'view_invoicemodel'),
(101, 'Can add item model', 26, 'add_itemmodel'),
(102, 'Can change item model', 26, 'change_itemmodel'),
(103, 'Can delete item model', 26, 'delete_itemmodel'),
(104, 'Can view item model', 26, 'view_itemmodel'),
(105, 'Can add item through model', 27, 'add_itemthroughmodel'),
(106, 'Can change item through model', 27, 'change_itemthroughmodel'),
(107, 'Can delete item through model', 27, 'delete_itemthroughmodel'),
(108, 'Can view item through model', 27, 'view_itemthroughmodel'),
(109, 'Can add JobCategory', 28, 'add_jobcategorymodel'),
(110, 'Can change JobCategory', 28, 'change_jobcategorymodel'),
(111, 'Can delete JobCategory', 28, 'delete_jobcategorymodel'),
(112, 'Can view JobCategory', 28, 'view_jobcategorymodel'),
(113, 'Can add Journal Entry', 29, 'add_journalentrymodel'),
(114, 'Can change Journal Entry', 29, 'change_journalentrymodel'),
(115, 'Can delete Journal Entry', 29, 'delete_journalentrymodel'),
(116, 'Can view Journal Entry', 29, 'view_journalentrymodel'),
(117, 'Can add LeaveRequestAction', 30, 'add_leaverequestactionmodel'),
(118, 'Can change LeaveRequestAction', 30, 'change_leaverequestactionmodel'),
(119, 'Can delete LeaveRequestAction', 30, 'delete_leaverequestactionmodel'),
(120, 'Can view LeaveRequestAction', 30, 'view_leaverequestactionmodel'),
(121, 'Can add LeaveRequest', 31, 'add_leaverequestmodel'),
(122, 'Can change LeaveRequest', 31, 'change_leaverequestmodel'),
(123, 'Can delete LeaveRequest', 31, 'delete_leaverequestmodel'),
(124, 'Can view LeaveRequest', 31, 'view_leaverequestmodel'),
(125, 'Can add NotificationExternalType', 32, 'add_notificationexternaltypemodel'),
(126, 'Can change NotificationExternalType', 32, 'change_notificationexternaltypemodel'),
(127, 'Can delete NotificationExternalType', 32, 'delete_notificationexternaltypemodel'),
(128, 'Can view NotificationExternalType', 32, 'view_notificationexternaltypemodel'),
(129, 'Can add PayrollAdvanceRequestAction', 33, 'add_payrolladvancerequestactionmodel'),
(130, 'Can change PayrollAdvanceRequestAction', 33, 'change_payrolladvancerequestactionmodel'),
(131, 'Can delete PayrollAdvanceRequestAction', 33, 'delete_payrolladvancerequestactionmodel'),
(132, 'Can view PayrollAdvanceRequestAction', 33, 'view_payrolladvancerequestactionmodel'),
(133, 'Can add Payroll Advance Request', 34, 'add_payrolladvancerequestmodel'),
(134, 'Can change Payroll Advance Request', 34, 'change_payrolladvancerequestmodel'),
(135, 'Can delete Payroll Advance Request', 34, 'delete_payrolladvancerequestmodel'),
(136, 'Can view Payroll Advance Request', 34, 'view_payrolladvancerequestmodel'),
(137, 'Can add RequisitionAction', 35, 'add_requisitionactionmodel'),
(138, 'Can change RequisitionAction', 35, 'change_requisitionactionmodel'),
(139, 'Can delete RequisitionAction', 35, 'delete_requisitionactionmodel'),
(140, 'Can view RequisitionAction', 35, 'view_requisitionactionmodel'),
(141, 'Can add RequisitionCategory', 36, 'add_requisitioncategorymodel'),
(142, 'Can change RequisitionCategory', 36, 'change_requisitioncategorymodel'),
(143, 'Can delete RequisitionCategory', 36, 'delete_requisitioncategorymodel'),
(144, 'Can view RequisitionCategory', 36, 'view_requisitioncategorymodel'),
(145, 'Can add Requisition', 37, 'add_requisitionmodel'),
(146, 'Can change Requisition', 37, 'change_requisitionmodel'),
(147, 'Can delete Requisition', 37, 'delete_requisitionmodel'),
(148, 'Can view Requisition', 37, 'view_requisitionmodel'),
(149, 'Can add Work Category', 38, 'add_workcategorymodel'),
(150, 'Can change Work Category', 38, 'change_workcategorymodel'),
(151, 'Can delete Work Category', 38, 'delete_workcategorymodel'),
(152, 'Can view Work Category', 38, 'view_workcategorymodel'),
(153, 'Can add work order jobcard model', 39, 'add_workorderjobcardmodel'),
(154, 'Can change work order jobcard model', 39, 'change_workorderjobcardmodel'),
(155, 'Can delete work order jobcard model', 39, 'delete_workorderjobcardmodel'),
(156, 'Can view work order jobcard model', 39, 'view_workorderjobcardmodel'),
(157, 'Can add WorkOrder', 40, 'add_workordermodel'),
(158, 'Can change WorkOrder', 40, 'change_workordermodel'),
(159, 'Can delete WorkOrder', 40, 'delete_workordermodel'),
(160, 'Can view WorkOrder', 40, 'view_workordermodel'),
(161, 'Can add Work Order Task', 41, 'add_workordertaskmodel'),
(162, 'Can change Work Order Task', 41, 'change_workordertaskmodel'),
(163, 'Can delete Work Order Task', 41, 'delete_workordertaskmodel'),
(164, 'Can view Work Order Task', 41, 'view_workordertaskmodel'),
(165, 'Can add WorkOrder Type', 42, 'add_workordertypemodel'),
(166, 'Can change WorkOrder Type', 42, 'change_workordertypemodel'),
(167, 'Can delete WorkOrder Type', 42, 'delete_workordertypemodel'),
(168, 'Can view WorkOrder Type', 42, 'view_workordertypemodel'),
(169, 'Can add Work Order Personnel', 43, 'add_workordertaskpersonnelmodel'),
(170, 'Can change Work Order Personnel', 43, 'change_workordertaskpersonnelmodel'),
(171, 'Can delete Work Order Personnel', 43, 'delete_workordertaskpersonnelmodel'),
(172, 'Can view Work Order Personnel', 43, 'view_workordertaskpersonnelmodel'),
(173, 'Can add Work Order Asset', 44, 'add_workordertaskassetmodel'),
(174, 'Can change Work Order Asset', 44, 'change_workordertaskassetmodel'),
(175, 'Can delete Work Order Asset', 44, 'delete_workordertaskassetmodel'),
(176, 'Can view Work Order Asset', 44, 'view_workordertaskassetmodel'),
(177, 'Can add WorkOrder Status', 45, 'add_workorderstatusmodel'),
(178, 'Can change WorkOrder Status', 45, 'change_workorderstatusmodel'),
(179, 'Can delete WorkOrder Status', 45, 'delete_workorderstatusmodel'),
(180, 'Can view WorkOrder Status', 45, 'view_workorderstatusmodel'),
(181, 'Can add Work Order Personnel', 46, 'add_workorderpersonnelmodel'),
(182, 'Can change Work Order Personnel', 46, 'change_workorderpersonnelmodel'),
(183, 'Can delete Work Order Personnel', 46, 'delete_workorderpersonnelmodel'),
(184, 'Can view Work Order Personnel', 46, 'view_workorderpersonnelmodel'),
(185, 'Can add Jobcard Status', 47, 'add_workorderjobcardstatusmodel'),
(186, 'Can change Jobcard Status', 47, 'change_workorderjobcardstatusmodel'),
(187, 'Can delete Jobcard Status', 47, 'delete_workorderjobcardstatusmodel'),
(188, 'Can view Jobcard Status', 47, 'view_workorderjobcardstatusmodel'),
(189, 'Can add Work Order Asset', 48, 'add_workorderassetmodel'),
(190, 'Can change Work Order Asset', 48, 'change_workorderassetmodel'),
(191, 'Can delete Work Order Asset', 48, 'delete_workorderassetmodel'),
(192, 'Can view Work Order Asset', 48, 'view_workorderassetmodel'),
(193, 'Can add WorkflowType', 49, 'add_workflowtypemodel'),
(194, 'Can change WorkflowType', 49, 'change_workflowtypemodel'),
(195, 'Can delete WorkflowType', 49, 'delete_workflowtypemodel'),
(196, 'Can view WorkflowType', 49, 'view_workflowtypemodel'),
(197, 'Can add WorkflowStatus', 50, 'add_workflowstatusmodel'),
(198, 'Can change WorkflowStatus', 50, 'change_workflowstatusmodel'),
(199, 'Can delete WorkflowStatus', 50, 'delete_workflowstatusmodel'),
(200, 'Can view WorkflowStatus', 50, 'view_workflowstatusmodel'),
(201, 'Can add Workflow', 51, 'add_workflowmodel'),
(202, 'Can change Workflow', 51, 'change_workflowmodel'),
(203, 'Can delete Workflow', 51, 'delete_workflowmodel'),
(204, 'Can view Workflow', 51, 'view_workflowmodel'),
(205, 'Can add WorkflowActionType', 52, 'add_workflowactiontypemodel'),
(206, 'Can change WorkflowActionType', 52, 'change_workflowactiontypemodel'),
(207, 'Can delete WorkflowActionType', 52, 'delete_workflowactiontypemodel'),
(208, 'Can view WorkflowActionType', 52, 'view_workflowactiontypemodel'),
(209, 'Can add WorkflowAction', 53, 'add_workflowactionmodel'),
(210, 'Can change WorkflowAction', 53, 'change_workflowactionmodel'),
(211, 'Can delete WorkflowAction', 53, 'delete_workflowactionmodel'),
(212, 'Can view WorkflowAction', 53, 'view_workflowactionmodel'),
(213, 'Can add WeeklyEmployeeProcessed', 54, 'add_weeklyemployeeprocessedmodel'),
(214, 'Can change WeeklyEmployeeProcessed', 54, 'change_weeklyemployeeprocessedmodel'),
(215, 'Can delete WeeklyEmployeeProcessed', 54, 'delete_weeklyemployeeprocessedmodel'),
(216, 'Can view WeeklyEmployeeProcessed', 54, 'view_weeklyemployeeprocessedmodel'),
(217, 'Can add WeeklyEmployee', 55, 'add_weeklyemployeemodel'),
(218, 'Can change WeeklyEmployee', 55, 'change_weeklyemployeemodel'),
(219, 'Can delete WeeklyEmployee', 55, 'delete_weeklyemployeemodel'),
(220, 'Can view WeeklyEmployee', 55, 'view_weeklyemployeemodel'),
(221, 'Can add Weekend', 56, 'add_weekendmodel'),
(222, 'Can change Weekend', 56, 'change_weekendmodel'),
(223, 'Can delete Weekend', 56, 'delete_weekendmodel'),
(224, 'Can view Weekend', 56, 'view_weekendmodel'),
(225, 'Can add Visa', 57, 'add_visamodel'),
(226, 'Can change Visa', 57, 'change_visamodel'),
(227, 'Can delete Visa', 57, 'delete_visamodel'),
(228, 'Can view Visa', 57, 'view_visamodel'),
(229, 'Can add Vendor', 58, 'add_vendormodel'),
(230, 'Can change Vendor', 58, 'change_vendormodel'),
(231, 'Can delete Vendor', 58, 'delete_vendormodel'),
(232, 'Can view Vendor', 58, 'view_vendormodel'),
(233, 'Can add unit of measure model', 59, 'add_unitofmeasuremodel'),
(234, 'Can change unit of measure model', 59, 'change_unitofmeasuremodel'),
(235, 'Can delete unit of measure model', 59, 'delete_unitofmeasuremodel'),
(236, 'Can view unit of measure model', 59, 'view_unitofmeasuremodel'),
(237, 'Can add Transaction', 60, 'add_transactionmodel'),
(238, 'Can change Transaction', 60, 'change_transactionmodel'),
(239, 'Can delete Transaction', 60, 'delete_transactionmodel'),
(240, 'Can view Transaction', 60, 'view_transactionmodel'),
(241, 'Can add Tax', 61, 'add_taxmodel'),
(242, 'Can change Tax', 61, 'change_taxmodel'),
(243, 'Can delete Tax', 61, 'delete_taxmodel'),
(244, 'Can view Tax', 61, 'view_taxmodel'),
(245, 'Can add TaskStatus', 62, 'add_taskstatusmodel'),
(246, 'Can change TaskStatus', 62, 'change_taskstatusmodel'),
(247, 'Can delete TaskStatus', 62, 'delete_taskstatusmodel'),
(248, 'Can view TaskStatus', 62, 'view_taskstatusmodel'),
(249, 'Can add Task', 63, 'add_taskmodel'),
(250, 'Can change Task', 63, 'change_taskmodel'),
(251, 'Can delete Task', 63, 'delete_taskmodel'),
(252, 'Can view Task', 63, 'view_taskmodel'),
(253, 'Can add TaskAssignee', 64, 'add_taskassigneemodel'),
(254, 'Can change TaskAssignee', 64, 'change_taskassigneemodel'),
(255, 'Can delete TaskAssignee', 64, 'delete_taskassigneemodel'),
(256, 'Can view TaskAssignee', 64, 'view_taskassigneemodel'),
(257, 'Can add Staged Transaction Model', 65, 'add_stagedtransactionmodel'),
(258, 'Can change Staged Transaction Model', 65, 'change_stagedtransactionmodel'),
(259, 'Can delete Staged Transaction Model', 65, 'delete_stagedtransactionmodel'),
(260, 'Can view Staged Transaction Model', 65, 'view_stagedtransactionmodel'),
(261, 'Can add Skill', 66, 'add_skillmodel'),
(262, 'Can change Skill', 66, 'change_skillmodel'),
(263, 'Can delete Skill', 66, 'delete_skillmodel'),
(264, 'Can view Skill', 66, 'view_skillmodel'),
(265, 'Can add Salary', 67, 'add_salarymodel'),
(266, 'Can change Salary', 67, 'change_salarymodel'),
(267, 'Can delete Salary', 67, 'delete_salarymodel'),
(268, 'Can view Salary', 67, 'view_salarymodel'),
(269, 'Can add RequisitionWorkflow', 68, 'add_requisitionworkflowmodel'),
(270, 'Can change RequisitionWorkflow', 68, 'change_requisitionworkflowmodel'),
(271, 'Can delete RequisitionWorkflow', 68, 'delete_requisitionworkflowmodel'),
(272, 'Can view RequisitionWorkflow', 68, 'view_requisitionworkflowmodel'),
(273, 'Can add RequisitionWorkflowAction', 69, 'add_requisitionworkflowactionmodel'),
(274, 'Can change RequisitionWorkflowAction', 69, 'change_requisitionworkflowactionmodel'),
(275, 'Can delete RequisitionWorkflowAction', 69, 'delete_requisitionworkflowactionmodel'),
(276, 'Can view RequisitionWorkflowAction', 69, 'view_requisitionworkflowactionmodel'),
(277, 'Can add RequisitionStatus', 70, 'add_requisitionstatusmodel'),
(278, 'Can change RequisitionStatus', 70, 'change_requisitionstatusmodel'),
(279, 'Can delete RequisitionStatus', 70, 'delete_requisitionstatusmodel'),
(280, 'Can view RequisitionStatus', 70, 'view_requisitionstatusmodel'),
(281, 'Can add RequisitionFlowType', 71, 'add_requisitionflowtypemodel'),
(282, 'Can change RequisitionFlowType', 71, 'change_requisitionflowtypemodel'),
(283, 'Can delete RequisitionFlowType', 71, 'delete_requisitionflowtypemodel'),
(284, 'Can view RequisitionFlowType', 71, 'view_requisitionflowtypemodel'),
(285, 'Can add Report', 72, 'add_reportmodel'),
(286, 'Can change Report', 72, 'change_reportmodel'),
(287, 'Can delete Report', 72, 'delete_reportmodel'),
(288, 'Can view Report', 72, 'view_reportmodel'),
(289, 'Can add Relationship', 73, 'add_relationshipmodel'),
(290, 'Can change Relationship', 73, 'change_relationshipmodel'),
(291, 'Can delete Relationship', 73, 'delete_relationshipmodel'),
(292, 'Can view Relationship', 73, 'view_relationshipmodel'),
(293, 'Can add ReceivedEmailDocument', 74, 'add_receivedemaildocumentmodel'),
(294, 'Can change ReceivedEmailDocument', 74, 'change_receivedemaildocumentmodel'),
(295, 'Can delete ReceivedEmailDocument', 74, 'delete_receivedemaildocumentmodel'),
(296, 'Can view ReceivedEmailDocument', 74, 'view_receivedemaildocumentmodel'),
(297, 'Can add Qualification', 75, 'add_qualificationmodel'),
(298, 'Can change Qualification', 75, 'change_qualificationmodel'),
(299, 'Can delete Qualification', 75, 'delete_qualificationmodel'),
(300, 'Can view Qualification', 75, 'view_qualificationmodel'),
(301, 'Can add purchase order model', 76, 'add_purchaseordermodel'),
(302, 'Can change purchase order model', 76, 'change_purchaseordermodel'),
(303, 'Can delete purchase order model', 76, 'delete_purchaseordermodel'),
(304, 'Can view purchase order model', 76, 'view_purchaseordermodel'),
(305, 'Can add PayrollAdvanceRequestWorkflow', 77, 'add_payrolladvancerequestworkflowmodel'),
(306, 'Can change PayrollAdvanceRequestWorkflow', 77, 'change_payrolladvancerequestworkflowmodel'),
(307, 'Can delete PayrollAdvanceRequestWorkflow', 77, 'delete_payrolladvancerequestworkflowmodel'),
(308, 'Can view PayrollAdvanceRequestWorkflow', 77, 'view_payrolladvancerequestworkflowmodel'),
(309, 'Can add PayrollAdvanceRequestWorkflowAction', 78, 'add_payrolladvancerequestworkflowactionmodel'),
(310, 'Can change PayrollAdvanceRequestWorkflowAction', 78, 'change_payrolladvancerequestworkflowactionmodel'),
(311, 'Can delete PayrollAdvanceRequestWorkflowAction', 78, 'delete_payrolladvancerequestworkflowactionmodel'),
(312, 'Can view PayrollAdvanceRequestWorkflowAction', 78, 'view_payrolladvancerequestworkflowactionmodel'),
(313, 'Can add PayrollAdvanceRequestStatus', 79, 'add_payrolladvancerequeststatusmodel'),
(314, 'Can change PayrollAdvanceRequestStatus', 79, 'change_payrolladvancerequeststatusmodel'),
(315, 'Can delete PayrollAdvanceRequestStatus', 79, 'delete_payrolladvancerequeststatusmodel'),
(316, 'Can view PayrollAdvanceRequestStatus', 79, 'view_payrolladvancerequeststatusmodel'),
(317, 'Can add PayrollAdvanceRequestDetail', 80, 'add_payrolladvancerequestdetailmodel'),
(318, 'Can change PayrollAdvanceRequestDetail', 80, 'change_payrolladvancerequestdetailmodel'),
(319, 'Can delete PayrollAdvanceRequestDetail', 80, 'delete_payrolladvancerequestdetailmodel'),
(320, 'Can view PayrollAdvanceRequestDetail', 80, 'view_payrolladvancerequestdetailmodel'),
(321, 'Can add PayrollAdvance', 81, 'add_payrolladvancemodel'),
(322, 'Can change PayrollAdvance', 81, 'change_payrolladvancemodel'),
(323, 'Can delete PayrollAdvance', 81, 'delete_payrolladvancemodel'),
(324, 'Can view PayrollAdvance', 81, 'view_payrolladvancemodel'),
(325, 'Can add PaymentMode', 82, 'add_paymentmodemodel'),
(326, 'Can change PaymentMode', 82, 'change_paymentmodemodel'),
(327, 'Can delete PaymentMode', 82, 'delete_paymentmodemodel'),
(328, 'Can view PaymentMode', 82, 'view_paymentmodemodel'),
(329, 'Can add NotificationTracker', 83, 'add_notificationtrackermodel'),
(330, 'Can change NotificationTracker', 83, 'change_notificationtrackermodel'),
(331, 'Can delete NotificationTracker', 83, 'delete_notificationtrackermodel'),
(332, 'Can view NotificationTracker', 83, 'view_notificationtrackermodel'),
(333, 'Can add Notification', 84, 'add_notificationmodel'),
(334, 'Can change Notification', 84, 'change_notificationmodel'),
(335, 'Can delete Notification', 84, 'delete_notificationmodel'),
(336, 'Can view Notification', 84, 'view_notificationmodel'),
(337, 'Can add Nation', 85, 'add_nationmodel'),
(338, 'Can change Nation', 85, 'change_nationmodel'),
(339, 'Can delete Nation', 85, 'delete_nationmodel'),
(340, 'Can view Nation', 85, 'view_nationmodel'),
(341, 'Can add MaritalStatus', 86, 'add_maritalstatusmodel'),
(342, 'Can change MaritalStatus', 86, 'change_maritalstatusmodel'),
(343, 'Can delete MaritalStatus', 86, 'delete_maritalstatusmodel'),
(344, 'Can view MaritalStatus', 86, 'view_maritalstatusmodel'),
(345, 'Can add Location', 87, 'add_locationmodel'),
(346, 'Can change Location', 87, 'change_locationmodel'),
(347, 'Can delete Location', 87, 'delete_locationmodel'),
(348, 'Can view Location', 87, 'view_locationmodel'),
(349, 'Can add Ledger', 88, 'add_ledgermodel'),
(350, 'Can change Ledger', 88, 'change_ledgermodel'),
(351, 'Can delete Ledger', 88, 'delete_ledgermodel'),
(352, 'Can view Ledger', 88, 'view_ledgermodel'),
(353, 'Can add LeaveRequestWorkflow', 89, 'add_leaverequestworkflowmodel'),
(354, 'Can change LeaveRequestWorkflow', 89, 'change_leaverequestworkflowmodel'),
(355, 'Can delete LeaveRequestWorkflow', 89, 'delete_leaverequestworkflowmodel'),
(356, 'Can view LeaveRequestWorkflow', 89, 'view_leaverequestworkflowmodel'),
(357, 'Can add LeaveRequestWorkflowAction', 90, 'add_leaverequestworkflowactionmodel'),
(358, 'Can change LeaveRequestWorkflowAction', 90, 'change_leaverequestworkflowactionmodel'),
(359, 'Can delete LeaveRequestWorkflowAction', 90, 'delete_leaverequestworkflowactionmodel'),
(360, 'Can view LeaveRequestWorkflowAction', 90, 'view_leaverequestworkflowactionmodel'),
(361, 'Can add Leave Request Status', 91, 'add_leaverequeststatusmodel'),
(362, 'Can change Leave Request Status', 91, 'change_leaverequeststatusmodel'),
(363, 'Can delete Leave Request Status', 91, 'delete_leaverequeststatusmodel'),
(364, 'Can view Leave Request Status', 91, 'view_leaverequeststatusmodel'),
(365, 'Can add LeaveRequestDetail', 92, 'add_leaverequestdetailmodel'),
(366, 'Can change LeaveRequestDetail', 92, 'change_leaverequestdetailmodel'),
(367, 'Can delete LeaveRequestDetail', 92, 'delete_leaverequestdetailmodel'),
(368, 'Can view LeaveRequestDetail', 92, 'view_leaverequestdetailmodel'),
(369, 'Can add LeaveCard', 93, 'add_leavecardmodel'),
(370, 'Can change LeaveCard', 93, 'change_leavecardmodel'),
(371, 'Can delete LeaveCard', 93, 'delete_leavecardmodel'),
(372, 'Can view LeaveCard', 93, 'view_leavecardmodel'),
(373, 'Can add LeaveCardDetail', 94, 'add_leavecarddetailmodel'),
(374, 'Can change LeaveCardDetail', 94, 'change_leavecarddetailmodel'),
(375, 'Can delete LeaveCardDetail', 94, 'delete_leavecarddetailmodel'),
(376, 'Can view LeaveCardDetail', 94, 'view_leavecarddetailmodel'),
(377, 'Can add LeaveCardCarriedOver', 95, 'add_leavecardcarriedovermodel'),
(378, 'Can change LeaveCardCarriedOver', 95, 'change_leavecardcarriedovermodel'),
(379, 'Can delete LeaveCardCarriedOver', 95, 'delete_leavecardcarriedovermodel'),
(380, 'Can view LeaveCardCarriedOver', 95, 'view_leavecardcarriedovermodel'),
(381, 'Can add Language', 96, 'add_languagemodel'),
(382, 'Can change Language', 96, 'change_languagemodel'),
(383, 'Can delete Language', 96, 'delete_languagemodel'),
(384, 'Can view Language', 96, 'view_languagemodel'),
(385, 'Can add KpiPob', 97, 'add_kpipobmodel'),
(386, 'Can change KpiPob', 97, 'change_kpipobmodel'),
(387, 'Can delete KpiPob', 97, 'delete_kpipobmodel'),
(388, 'Can view KpiPob', 97, 'view_kpipobmodel'),
(389, 'Can add KpiOps', 98, 'add_kpiopsmodel'),
(390, 'Can change KpiOps', 98, 'change_kpiopsmodel'),
(391, 'Can delete KpiOps', 98, 'delete_kpiopsmodel'),
(392, 'Can view KpiOps', 98, 'view_kpiopsmodel'),
(393, 'Can add KpiOnOff', 99, 'add_kpionoffmodel'),
(394, 'Can change KpiOnOff', 99, 'change_kpionoffmodel'),
(395, 'Can delete KpiOnOff', 99, 'delete_kpionoffmodel'),
(396, 'Can view KpiOnOff', 99, 'view_kpionoffmodel'),
(397, 'Can add KpiHse', 100, 'add_kpihsemodel'),
(398, 'Can change KpiHse', 100, 'change_kpihsemodel'),
(399, 'Can delete KpiHse', 100, 'delete_kpihsemodel'),
(400, 'Can view KpiHse', 100, 'view_kpihsemodel'),
(401, 'Can add Job', 101, 'add_jobmodel'),
(402, 'Can change Job', 101, 'change_jobmodel'),
(403, 'Can delete Job', 101, 'delete_jobmodel'),
(404, 'Can view Job', 101, 'view_jobmodel'),
(405, 'Can add Job Applicant', 102, 'add_jobapplicantmodel'),
(406, 'Can change Job Applicant', 102, 'change_jobapplicantmodel'),
(407, 'Can delete Job Applicant', 102, 'delete_jobapplicantmodel'),
(408, 'Can view Job Applicant', 102, 'view_jobapplicantmodel'),
(409, 'Can add InvoiceType', 103, 'add_invoicetypemodel'),
(410, 'Can change InvoiceType', 103, 'change_invoicetypemodel'),
(411, 'Can delete InvoiceType', 103, 'delete_invoicetypemodel'),
(412, 'Can view InvoiceType', 103, 'view_invoicetypemodel'),
(413, 'Can add InvoiceStatus', 104, 'add_invoicestatusmodel'),
(414, 'Can change InvoiceStatus', 104, 'change_invoicestatusmodel'),
(415, 'Can delete InvoiceStatus', 104, 'delete_invoicestatusmodel'),
(416, 'Can view InvoiceStatus', 104, 'view_invoicestatusmodel'),
(417, 'Can add InvoiceAction', 105, 'add_invoiceactionmodel'),
(418, 'Can change InvoiceAction', 105, 'change_invoiceactionmodel'),
(419, 'Can delete InvoiceAction', 105, 'delete_invoiceactionmodel'),
(420, 'Can view InvoiceAction', 105, 'view_invoiceactionmodel'),
(421, 'Can add InsuranceDetail', 106, 'add_insurancedetailmodel'),
(422, 'Can change InsuranceDetail', 106, 'change_insurancedetailmodel'),
(423, 'Can delete InsuranceDetail', 106, 'delete_insurancedetailmodel'),
(424, 'Can view InsuranceDetail', 106, 'view_insurancedetailmodel'),
(425, 'Can add IncomingDocumentType', 107, 'add_incomingdocumenttypemodel'),
(426, 'Can change IncomingDocumentType', 107, 'change_incomingdocumenttypemodel'),
(427, 'Can delete IncomingDocumentType', 107, 'delete_incomingdocumenttypemodel'),
(428, 'Can view IncomingDocumentType', 107, 'view_incomingdocumenttypemodel'),
(429, 'Can add IncomingDocument', 108, 'add_incomingdocumentmodel'),
(430, 'Can change IncomingDocument', 108, 'change_incomingdocumentmodel'),
(431, 'Can delete IncomingDocument', 108, 'delete_incomingdocumentmodel'),
(432, 'Can view IncomingDocument', 108, 'view_incomingdocumentmodel'),
(433, 'Can add IncomingDocumentHandler', 109, 'add_incomingdocumenthandlermodel'),
(434, 'Can change IncomingDocumentHandler', 109, 'change_incomingdocumenthandlermodel'),
(435, 'Can delete IncomingDocumentHandler', 109, 'delete_incomingdocumenthandlermodel'),
(436, 'Can view IncomingDocumentHandler', 109, 'view_incomingdocumenthandlermodel'),
(437, 'Can add Holiday', 110, 'add_holidaymodel'),
(438, 'Can change Holiday', 110, 'change_holidaymodel'),
(439, 'Can delete Holiday', 110, 'delete_holidaymodel'),
(440, 'Can view Holiday', 110, 'view_holidaymodel'),
(441, 'Can add GeneralNotification', 111, 'add_generalnotificationmodel'),
(442, 'Can change GeneralNotification', 111, 'change_generalnotificationmodel'),
(443, 'Can delete GeneralNotification', 111, 'delete_generalnotificationmodel'),
(444, 'Can view GeneralNotification', 111, 'view_generalnotificationmodel'),
(445, 'Can add EmployeeTransaction', 112, 'add_employeetransactionmodel'),
(446, 'Can change EmployeeTransaction', 112, 'change_employeetransactionmodel'),
(447, 'Can delete EmployeeTransaction', 112, 'delete_employeetransactionmodel'),
(448, 'Can view EmployeeTransaction', 112, 'view_employeetransactionmodel'),
(449, 'Can add EmployeePayroll', 113, 'add_employeepayrollmodel'),
(450, 'Can change EmployeePayroll', 113, 'change_employeepayrollmodel'),
(451, 'Can delete EmployeePayroll', 113, 'delete_employeepayrollmodel'),
(452, 'Can view EmployeePayroll', 113, 'view_employeepayrollmodel'),
(453, 'Can add EmployeePayrollBenefit', 114, 'add_employeepayrollbenefitmodel'),
(454, 'Can change EmployeePayrollBenefit', 114, 'change_employeepayrollbenefitmodel'),
(455, 'Can delete EmployeePayrollBenefit', 114, 'delete_employeepayrollbenefitmodel'),
(456, 'Can view EmployeePayrollBenefit', 114, 'view_employeepayrollbenefitmodel'),
(457, 'Can add EmployeeOfTheWeek', 115, 'add_employeeoftheweekmodel'),
(458, 'Can change EmployeeOfTheWeek', 115, 'change_employeeoftheweekmodel'),
(459, 'Can delete EmployeeOfTheWeek', 115, 'delete_employeeoftheweekmodel'),
(460, 'Can view EmployeeOfTheWeek', 115, 'view_employeeoftheweekmodel'),
(461, 'Can add EmployeeLicenseType', 116, 'add_employeelicensetypemodel'),
(462, 'Can change EmployeeLicenseType', 116, 'change_employeelicensetypemodel'),
(463, 'Can delete EmployeeLicenseType', 116, 'delete_employeelicensetypemodel'),
(464, 'Can view EmployeeLicenseType', 116, 'view_employeelicensetypemodel'),
(465, 'Can add EmployeeLicenseDetail', 117, 'add_employeelicensedetailmodel'),
(466, 'Can change EmployeeLicenseDetail', 117, 'change_employeelicensedetailmodel'),
(467, 'Can delete EmployeeLicenseDetail', 117, 'delete_employeelicensedetailmodel'),
(468, 'Can view EmployeeLicenseDetail', 117, 'view_employeelicensedetailmodel'),
(469, 'Can add EmployeeLanguage', 118, 'add_employeelanguagemodel'),
(470, 'Can change EmployeeLanguage', 118, 'change_employeelanguagemodel'),
(471, 'Can delete EmployeeLanguage', 118, 'delete_employeelanguagemodel'),
(472, 'Can view EmployeeLanguage', 118, 'view_employeelanguagemodel'),
(473, 'Can add EmployeeContractType', 119, 'add_employeecontracttypemodel'),
(474, 'Can change EmployeeContractType', 119, 'change_employeecontracttypemodel'),
(475, 'Can delete EmployeeContractType', 119, 'delete_employeecontracttypemodel'),
(476, 'Can view EmployeeContractType', 119, 'view_employeecontracttypemodel'),
(477, 'Can add EmployeeContract', 120, 'add_employeecontractmodel'),
(478, 'Can change EmployeeContract', 120, 'change_employeecontractmodel'),
(479, 'Can delete EmployeeContract', 120, 'delete_employeecontractmodel'),
(480, 'Can view EmployeeContract', 120, 'view_employeecontractmodel'),
(481, 'Can add EmployeeAvatar', 121, 'add_employeeavatarmodel'),
(482, 'Can change EmployeeAvatar', 121, 'change_employeeavatarmodel'),
(483, 'Can delete EmployeeAvatar', 121, 'delete_employeeavatarmodel'),
(484, 'Can view EmployeeAvatar', 121, 'view_employeeavatarmodel'),
(485, 'Can add EmployeeAssignment', 122, 'add_employeeassignmentmodel'),
(486, 'Can change EmployeeAssignment', 122, 'change_employeeassignmentmodel'),
(487, 'Can delete EmployeeAssignment', 122, 'delete_employeeassignmentmodel'),
(488, 'Can view EmployeeAssignment', 122, 'view_employeeassignmentmodel'),
(489, 'Can add Education', 123, 'add_educationmodel'),
(490, 'Can change Education', 123, 'change_educationmodel'),
(491, 'Can delete Education', 123, 'delete_educationmodel'),
(492, 'Can view Education', 123, 'view_educationmodel'),
(493, 'Can add DocumentType', 124, 'add_documenttypemodel'),
(494, 'Can change DocumentType', 124, 'change_documenttypemodel'),
(495, 'Can delete DocumentType', 124, 'delete_documenttypemodel'),
(496, 'Can view DocumentType', 124, 'view_documenttypemodel'),
(497, 'Can add DocumentStatus', 125, 'add_documentstatusmodel'),
(498, 'Can change DocumentStatus', 125, 'change_documentstatusmodel'),
(499, 'Can delete DocumentStatus', 125, 'delete_documentstatusmodel'),
(500, 'Can view DocumentStatus', 125, 'view_documentstatusmodel'),
(501, 'Can add Document', 126, 'add_documentmodel'),
(502, 'Can change Document', 126, 'change_documentmodel'),
(503, 'Can delete Document', 126, 'delete_documentmodel'),
(504, 'Can view Document', 126, 'view_documentmodel'),
(505, 'Can add Dependant', 127, 'add_dependantmodel'),
(506, 'Can change Dependant', 127, 'change_dependantmodel'),
(507, 'Can delete Dependant', 127, 'delete_dependantmodel'),
(508, 'Can view Dependant', 127, 'view_dependantmodel'),
(509, 'Can add CurrencyRate', 128, 'add_currencyratemodel'),
(510, 'Can change CurrencyRate', 128, 'change_currencyratemodel'),
(511, 'Can delete CurrencyRate', 128, 'delete_currencyratemodel'),
(512, 'Can view CurrencyRate', 128, 'view_currencyratemodel'),
(513, 'Can add Chart of Account', 129, 'add_chartofaccountmodel'),
(514, 'Can change Chart of Account', 129, 'change_chartofaccountmodel'),
(515, 'Can delete Chart of Account', 129, 'delete_chartofaccountmodel'),
(516, 'Can view Chart of Account', 129, 'view_chartofaccountmodel'),
(517, 'Can add Benefit', 130, 'add_benefitmodel'),
(518, 'Can change Benefit', 130, 'change_benefitmodel'),
(519, 'Can delete Benefit', 130, 'delete_benefitmodel'),
(520, 'Can view Benefit', 130, 'view_benefitmodel'),
(521, 'Can add Bank Account', 131, 'add_bankaccountmodel'),
(522, 'Can change Bank Account', 131, 'change_bankaccountmodel'),
(523, 'Can delete Bank Account', 131, 'delete_bankaccountmodel'),
(524, 'Can view Bank Account', 131, 'view_bankaccountmodel'),
(525, 'Can add AttachedEmail', 132, 'add_attachedemailmodel'),
(526, 'Can change AttachedEmail', 132, 'change_attachedemailmodel'),
(527, 'Can delete AttachedEmail', 132, 'delete_attachedemailmodel'),
(528, 'Can view AttachedEmail', 132, 'view_attachedemailmodel'),
(529, 'Can add Announcement', 133, 'add_announcementmodel'),
(530, 'Can change Announcement', 133, 'change_announcementmodel'),
(531, 'Can delete Announcement', 133, 'delete_announcementmodel'),
(532, 'Can view Announcement', 133, 'view_announcementmodel'),
(533, 'Can add AccountcodePrefix', 134, 'add_accountcodeprefixmodel'),
(534, 'Can change AccountcodePrefix', 134, 'change_accountcodeprefixmodel'),
(535, 'Can delete AccountcodePrefix', 134, 'delete_accountcodeprefixmodel'),
(536, 'Can view AccountcodePrefix', 134, 'view_accountcodeprefixmodel'),
(537, 'Can add AbsenceDate', 135, 'add_absencedatemodel'),
(538, 'Can change AbsenceDate', 135, 'change_absencedatemodel'),
(539, 'Can delete AbsenceDate', 135, 'delete_absencedatemodel'),
(540, 'Can view AbsenceDate', 135, 'view_absencedatemodel'),
(541, 'Can add UserAllocation', 136, 'add_userallocationmodel'),
(542, 'Can change UserAllocation', 136, 'change_userallocationmodel'),
(543, 'Can delete UserAllocation', 136, 'delete_userallocationmodel'),
(544, 'Can view UserAllocation', 136, 'view_userallocationmodel'),
(545, 'Can add Systems Support Status', 137, 'add_aixitsstatusreportmodel'),
(546, 'Can change Systems Support Status', 137, 'change_aixitsstatusreportmodel'),
(547, 'Can delete Systems Support Status', 137, 'delete_aixitsstatusreportmodel'),
(548, 'Can view Systems Support Status', 137, 'view_aixitsstatusreportmodel'),
(549, 'Can add Equipment Axle', 138, 'add_equipmentaxlemodel'),
(550, 'Can change Equipment Axle', 138, 'change_equipmentaxlemodel'),
(551, 'Can delete Equipment Axle', 138, 'delete_equipmentaxlemodel'),
(552, 'Can view Equipment Axle', 138, 'view_equipmentaxlemodel'),
(553, 'Can add Equipment Manufacturer', 139, 'add_equipmentmanufacturermodel'),
(554, 'Can change Equipment Manufacturer', 139, 'change_equipmentmanufacturermodel'),
(555, 'Can delete Equipment Manufacturer', 139, 'delete_equipmentmanufacturermodel'),
(556, 'Can view Equipment Manufacturer', 139, 'view_equipmentmanufacturermodel'),
(557, 'Can add Equipment', 140, 'add_equipmentmodel'),
(558, 'Can change Equipment', 140, 'change_equipmentmodel'),
(559, 'Can delete Equipment', 140, 'delete_equipmentmodel'),
(560, 'Can view Equipment', 140, 'view_equipmentmodel'),
(561, 'Can add Systems Support Status', 141, 'add_aixitshandovermodel'),
(562, 'Can change Systems Support Status', 141, 'change_aixitshandovermodel'),
(563, 'Can delete Systems Support Status', 141, 'delete_aixitshandovermodel'),
(564, 'Can view Systems Support Status', 141, 'view_aixitshandovermodel'),
(565, 'Can add Equipment Type', 142, 'add_equipmenttypemodel'),
(566, 'Can change Equipment Type', 142, 'change_equipmenttypemodel'),
(567, 'Can delete Equipment Type', 142, 'delete_equipmenttypemodel'),
(568, 'Can view Equipment Type', 142, 'view_equipmenttypemodel'),
(569, 'Can add Equipment Assignment', 143, 'add_equipmentassignmentmodel'),
(570, 'Can change Equipment Assignment', 143, 'change_equipmentassignmentmodel'),
(571, 'Can delete Equipment Assignment', 143, 'delete_equipmentassignmentmodel'),
(572, 'Can view Equipment Assignment', 143, 'view_equipmentassignmentmodel'),
(573, 'Can add Equipment Join', 144, 'add_equipmentjoinmodel'),
(574, 'Can change Equipment Join', 144, 'change_equipmentjoinmodel'),
(575, 'Can delete Equipment Join', 144, 'delete_equipmentjoinmodel'),
(576, 'Can view Equipment Join', 144, 'view_equipmentjoinmodel'),
(577, 'Can add Equipment Handover', 145, 'add_equipmenthandovermodel'),
(578, 'Can change Equipment Handover', 145, 'change_equipmenthandovermodel'),
(579, 'Can delete Equipment Handover', 145, 'delete_equipmenthandovermodel'),
(580, 'Can view Equipment Handover', 145, 'view_equipmenthandovermodel'),
(581, 'Can add RouteSurveyInfo', 146, 'add_routesurveyinfomodel'),
(582, 'Can change RouteSurveyInfo', 146, 'change_routesurveyinfomodel'),
(583, 'Can delete RouteSurveyInfo', 146, 'delete_routesurveyinfomodel'),
(584, 'Can view RouteSurveyInfo', 146, 'view_routesurveyinfomodel'),
(585, 'Can add RouteSurvey', 147, 'add_routesurveymodel'),
(586, 'Can change RouteSurvey', 147, 'change_routesurveymodel'),
(587, 'Can delete RouteSurvey', 147, 'delete_routesurveymodel'),
(588, 'Can view RouteSurvey', 147, 'view_routesurveymodel'),
(589, 'Can add EmployeeFaw', 148, 'add_employeefawmodel'),
(590, 'Can change EmployeeFaw', 148, 'change_employeefawmodel'),
(591, 'Can delete EmployeeFaw', 148, 'delete_employeefawmodel'),
(592, 'Can view EmployeeFaw', 148, 'view_employeefawmodel'),
(593, 'Can add item faw model', 149, 'add_itemfawmodel'),
(594, 'Can change item faw model', 149, 'change_itemfawmodel'),
(595, 'Can delete item faw model', 149, 'delete_itemfawmodel'),
(596, 'Can view item faw model', 149, 'view_itemfawmodel'),
(597, 'Can add item faw through model', 150, 'add_itemfawthroughmodel'),
(598, 'Can change item faw through model', 150, 'change_itemfawthroughmodel'),
(599, 'Can delete item faw through model', 150, 'delete_itemfawthroughmodel'),
(600, 'Can view item faw through model', 150, 'view_itemfawthroughmodel'),
(601, 'Can add EquipmentFet', 151, 'add_equipmentfetmodel'),
(602, 'Can change EquipmentFet', 151, 'change_equipmentfetmodel'),
(603, 'Can delete EquipmentFet', 151, 'delete_equipmentfetmodel'),
(604, 'Can view EquipmentFet', 151, 'view_equipmentfetmodel'),
(605, 'Can add item fet through model', 152, 'add_itemfetthroughmodel'),
(606, 'Can change item fet through model', 152, 'change_itemfetthroughmodel'),
(607, 'Can delete item fet through model', 152, 'delete_itemfetthroughmodel'),
(608, 'Can view item fet through model', 152, 'view_itemfetthroughmodel'),
(609, 'Can add item fet model', 153, 'add_itemfetmodel'),
(610, 'Can change item fet model', 153, 'change_itemfetmodel'),
(611, 'Can delete item fet model', 153, 'delete_itemfetmodel'),
(612, 'Can view item fet model', 153, 'view_itemfetmodel'),
(613, 'Can add Equipment Fuel', 154, 'add_equipmentfuelmodel'),
(614, 'Can change Equipment Fuel', 154, 'change_equipmentfuelmodel'),
(615, 'Can delete Equipment Fuel', 154, 'delete_equipmentfuelmodel'),
(616, 'Can view Equipment Fuel', 154, 'view_equipmentfuelmodel'),
(617, 'Can add WorkOrderActivity', 155, 'add_workorderactivitymodel'),
(618, 'Can change WorkOrderActivity', 155, 'change_workorderactivitymodel'),
(619, 'Can delete WorkOrderActivity', 155, 'delete_workorderactivitymodel'),
(620, 'Can view WorkOrderActivity', 155, 'view_workorderactivitymodel'),
(621, 'Can add Work Order Asset', 156, 'add_workorderactivityassetmodel'),
(622, 'Can change Work Order Asset', 156, 'change_workorderactivityassetmodel'),
(623, 'Can delete Work Order Asset', 156, 'delete_workorderactivityassetmodel'),
(624, 'Can view Work Order Asset', 156, 'view_workorderactivityassetmodel'),
(625, 'Can add Work Order Personnel', 157, 'add_workorderactivitypersonnelmodel'),
(626, 'Can change Work Order Personnel', 157, 'change_workorderactivitypersonnelmodel'),
(627, 'Can delete Work Order Personnel', 157, 'delete_workorderactivitypersonnelmodel'),
(628, 'Can view Work Order Personnel', 157, 'view_workorderactivitypersonnelmodel'),
(629, 'Can add Work Order Document', 158, 'add_workorderactivitydocumentmodel'),
(630, 'Can change Work Order Document', 158, 'change_workorderactivitydocumentmodel'),
(631, 'Can delete Work Order Document', 158, 'delete_workorderactivitydocumentmodel'),
(632, 'Can view Work Order Document', 158, 'view_workorderactivitydocumentmodel'),
(633, 'Can add Work Order Lifting', 159, 'add_workorderactivityliftingmodel'),
(634, 'Can change Work Order Lifting', 159, 'change_workorderactivityliftingmodel'),
(635, 'Can delete Work Order Lifting', 159, 'delete_workorderactivityliftingmodel'),
(636, 'Can view Work Order Lifting', 159, 'view_workorderactivityliftingmodel'),
(637, 'Can add Work Order Transport', 160, 'add_workorderactivitytransportmodel'),
(638, 'Can change Work Order Transport', 160, 'change_workorderactivitytransportmodel'),
(639, 'Can delete Work Order Transport', 160, 'delete_workorderactivitytransportmodel'),
(640, 'Can view Work Order Transport', 160, 'view_workorderactivitytransportmodel');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$870000$9jR0rWaBi0uCtWc1j2BbEG$UiK1Orm+mS1ZY95t4cutU1jua2lh2PQ1doXqvDKbn9A=', '2025-09-04 11:00:31.215212', 1, 'mando', '', '', 'mandonpolo@gmail.com', 1, 1, '2024-02-24 02:33:12.000000'),
(2, 'pbkdf2_sha256$870000$oz3LWPQ7OvirkcZUDh0YdU$wstTDhvQQ0rR++v0bWfBiYitFh9BvrLM7vn9J1RXqMA=', '2025-09-04 06:38:09.372063', 1, 'admin', '', '', 'pshopi@threewaysshipping.com', 1, 1, '2024-02-24 02:33:51.000000'),
(3, 'pbkdf2_sha256$600000$JvqiW1Yift4FNkXV8csDuc$NN7aR6nFfXYpZLOTtyQLPoGTWvJD8kGqwVZLgnd2e8Y=', '2024-03-22 08:06:30.341098', 0, 'adminclerk', '', '', 'polosp09@gmail.com', 0, 1, '2024-02-24 02:39:42.000000'),
(4, 'pbkdf2_sha256$600000$71smfGQ5G3iXcNqOO12AD5$/hxTHJq+Yi5tBGmhs9LpZilxWgnKvP/0oyg2BKw4pGc=', '2024-03-19 05:17:10.000000', 0, 'sitetransportsupervisor', '', '', 'pshopi@threewayshipping.com', 0, 1, '2024-03-09 01:32:47.000000'),
(5, 'pbkdf2_sha256$870000$OY9IVvbJ9se8sHIf1QoKsH$y6jOpqLw5U8fXRWEWjfhPraA/ipzY7JQr5XTDWnMHM4=', '2025-02-03 12:33:59.207087', 0, 'operationsmanager', '', '', 'pshopi@threewayshipping.com', 0, 1, '2024-03-09 01:36:14.000000'),
(6, 'pbkdf2_sha256$600000$4hNVIiPP1Y3IkDEhvYng7d$i8gRRvmbrbAgbvVulkoNN4qYjO8zm5ftAUs7d8NGBhU=', '2024-03-28 05:21:57.412635', 0, 'totalsupervisor', '', '', 'pshopi@threewaysshipping.com', 0, 1, '2024-03-09 01:38:09.000000'),
(7, 'pbkdf2_sha256$600000$5arsTkJ0UpioRNbiayuN8D$ZZa6/GvmyC48ZB7Rj3flOiWLfIgIhcCQXu09/cDgIqc=', '2024-03-20 04:52:18.142605', 0, 'siteliftingsupervisor', '', '', 'pshopi@threewaysshipping.com', 0, 1, '2024-03-18 11:54:52.000000');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(7, 1, 1),
(2, 2, 1),
(1, 3, 3),
(3, 4, 2),
(4, 5, 4),
(5, 6, 5),
(6, 7, 2);

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-02-24 02:38:14.718323', '1', 'Admins', 1, '[{\"added\": {}}]', 3, 2),
(2, '2024-02-24 02:38:33.728589', '2', 'Supervisor', 1, '[{\"added\": {}}]', 3, 2),
(3, '2024-02-24 02:38:47.479002', '3', 'Clerks', 1, '[{\"added\": {}}]', 3, 2),
(4, '2024-02-24 02:39:43.146096', '3', 'adminclerk', 1, '[{\"added\": {}}]', 4, 2),
(5, '2024-02-24 02:39:56.168328', '3', 'adminclerk', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 2),
(6, '2024-02-24 02:40:16.505361', '109cc05a-4040-4a3b-8762-4ebfc8970a6f', 'adminclerk - Total Uganda', 1, '[{\"added\": {}}]', 19, 2),
(7, '2024-02-24 02:44:48.970420', '2', 'admin', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 2),
(8, '2024-03-08 10:45:43.400799', '4', 'Operations Manager', 1, '[{\"added\": {}}]', 3, 2),
(9, '2024-03-08 10:46:15.150064', '4', 'OperationsManager', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 3, 2),
(10, '2024-03-08 10:47:23.415672', '5', 'TotalProjectManager', 1, '[{\"added\": {}}]', 3, 2),
(11, '2024-03-08 10:47:49.933664', '6', 'ProjectManager', 1, '[{\"added\": {}}]', 3, 2),
(12, '2024-03-09 01:28:42.945285', '339f1af8-355d-4636-8287-880d810028e8', 'UserAllocation: WOR4BJQ72246 - None', 1, '[{\"added\": {}}]', 136, 2),
(13, '2024-03-09 01:32:48.071748', '4', 'sitesupervisor', 1, '[{\"added\": {}}]', 4, 2),
(14, '2024-03-09 01:33:12.452818', '4', 'sitesupervisor', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 2),
(15, '2024-03-09 01:33:52.335418', '3', 'adminclerk', 2, '[{\"changed\": {\"fields\": [\"Email address\"]}}]', 4, 2),
(16, '2024-03-09 01:35:37.371741', '4', 'sitetransportsupervisor', 2, '[{\"changed\": {\"fields\": [\"Username\", \"Email address\"]}}]', 4, 2),
(17, '2024-03-09 01:36:15.548001', '5', 'operationsmanager', 1, '[{\"added\": {}}]', 4, 2),
(18, '2024-03-09 01:36:48.425635', '5', 'operationsmanager', 2, '[{\"changed\": {\"fields\": [\"Email address\", \"Groups\"]}}]', 4, 2),
(19, '2024-03-09 01:38:10.150895', '6', 'totalsupervisor', 1, '[{\"added\": {}}]', 4, 2),
(20, '2024-03-09 01:38:50.557533', '6', 'totalsupervisor', 2, '[{\"changed\": {\"fields\": [\"Email address\", \"Groups\"]}}]', 4, 2),
(21, '2024-03-10 01:13:49.359305', '339f1af8-355d-4636-8287-880d810028e8', 'UserAllocation: WOR4BJQ72246 - TSKWK378HB', 2, '[{\"changed\": {\"fields\": [\"Work Order Task\"]}}]', 136, 2),
(22, '2024-03-10 01:14:13.739817', '339f1af8-355d-4636-8287-880d810028e8', 'UserAllocation: None - TSKWK378HB', 2, '[{\"changed\": {\"fields\": [\"Work Order\"]}}]', 136, 2),
(23, '2024-03-10 01:19:24.714399', '339f1af8-355d-4636-8287-880d810028e8', 'UserAllocation: WOR4BJQ72246 - TSKWK378HB', 2, '[{\"changed\": {\"fields\": [\"Work Order\"]}}]', 136, 2),
(24, '2024-03-10 01:34:42.141231', '339f1af8-355d-4636-8287-880d810028e8', 'UserAllocation: None - TSKWK378HB', 2, '[{\"changed\": {\"fields\": [\"Work Order\"]}}]', 136, 2),
(25, '2024-03-10 01:38:42.203407', 'aba5cfbd-675e-414b-acb3-42a0f353ceb2', 'sitetransportsupervisor - Total Uganda', 1, '[{\"added\": {}}]', 19, 2),
(26, '2024-03-10 01:42:02.087476', 'a6eca64f-6d1a-4e1c-8c13-9b5f92fa8a43', 'UserAllocation: WO3418ANE6W4 - None', 1, '[{\"added\": {}}]', 136, 2),
(27, '2024-03-10 01:53:01.134921', '4ea1bcfc-f9c1-49be-966d-b2806d1e9c91', 'UserAllocation: WOR4BJQ72246 - TSKWK378HB', 1, '[{\"added\": {}}]', 136, 2),
(28, '2024-03-18 11:48:34.709912', '5', 'operationsmanager', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 4, 2),
(29, '2024-03-18 11:49:20.276160', '4', 'sitetransportsupervisor', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 4, 2),
(30, '2024-03-18 11:50:06.109061', '6', 'totalsupervisor', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 4, 2),
(31, '2024-03-18 11:54:53.064133', '7', 'siteliftingsupervisor', 1, '[{\"added\": {}}]', 4, 2),
(32, '2024-03-18 11:55:13.437340', '7', 'siteliftingsupervisor', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 2),
(33, '2024-03-18 11:55:38.017918', '7', 'siteliftingsupervisor', 2, '[{\"changed\": {\"fields\": [\"Email address\"]}}]', 4, 2),
(34, '2024-03-18 12:01:32.571176', '6', 'totalsupervisor', 2, '[{\"changed\": {\"fields\": [\"Email address\"]}}]', 4, 2),
(35, '2024-03-18 12:08:47.249001', '6', 'totalsupervisor', 2, '[]', 4, 2),
(36, '2024-03-18 12:26:47.350084', '13c648b6-54c7-4f8c-b5ba-e8f642e52aee', 'totalsupervisor - Total Uganda', 1, '[{\"added\": {}}]', 19, 2),
(37, '2024-03-18 12:27:02.097225', '5a4633b0-cfb8-4ac7-be25-3ae732440e87', 'operationsmanager - Total Uganda', 1, '[{\"added\": {}}]', 19, 2),
(38, '2024-03-18 12:27:14.204954', 'f782bfef-96a3-47dc-825c-2ee1d239e2f9', 'siteliftingsupervisor - Total Uganda', 1, '[{\"added\": {}}]', 19, 2),
(39, '2024-03-19 06:09:40.143651', '4', 'sitetransportsupervisor', 2, '[{\"changed\": {\"fields\": [\"Email address\"]}}]', 4, 2),
(40, '2024-03-20 08:22:40.933386', '5', 'operationsmanager', 2, '[{\"changed\": {\"fields\": [\"Email address\"]}}]', 4, 2),
(41, '2024-03-22 07:52:36.897169', '104de248-e065-4067-8857-8a889efe4676', 'admin - Total Uganda', 1, '[{\"added\": {}}]', 19, 2),
(42, '2024-03-22 11:48:08.820708', '1', 'mando', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 4, 2),
(43, '2024-08-28 08:04:35.828785', '83aa4390-44c8-4d68-a2b9-6ad16107cd34', 'admin - Keba', 1, '[{\"added\": {}}]', 19, 2),
(44, '2024-08-28 08:29:57.652435', 'd283079e-1fc1-4aa1-9c7f-7130ce218557', 'admin - Threeways', 1, '[{\"added\": {}}]', 19, 2),
(45, '2025-03-31 06:12:05.494548', 'b809460e-d849-4d2c-9edd-46987b94d57e', 'mando - Threeways', 1, '[{\"added\": {}}]', 19, 1),
(46, '2025-03-31 06:13:54.684421', '1', 'mando', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(135, 'aix', 'absencedatemodel'),
(7, 'aix', 'absencetypemodel'),
(134, 'aix', 'accountcodeprefixmodel'),
(8, 'aix', 'accountmodel'),
(141, 'aix', 'aixitshandovermodel'),
(137, 'aix', 'aixitsstatusreportmodel'),
(133, 'aix', 'announcementmodel'),
(9, 'aix', 'assetmodel'),
(132, 'aix', 'attachedemailmodel'),
(131, 'aix', 'bankaccountmodel'),
(10, 'aix', 'benefitcalculationmodel'),
(130, 'aix', 'benefitmodel'),
(11, 'aix', 'benefittypemodel'),
(12, 'aix', 'billmodel'),
(13, 'aix', 'businessindustrymodel'),
(129, 'aix', 'chartofaccountmodel'),
(14, 'aix', 'currencymodel'),
(128, 'aix', 'currencyratemodel'),
(15, 'aix', 'customerlocationmodel'),
(16, 'aix', 'customermodel'),
(17, 'aix', 'departmentmodel'),
(127, 'aix', 'dependantmodel'),
(126, 'aix', 'documentmodel'),
(125, 'aix', 'documentstatusmodel'),
(124, 'aix', 'documenttypemodel'),
(123, 'aix', 'educationmodel'),
(122, 'aix', 'employeeassignmentmodel'),
(121, 'aix', 'employeeavatarmodel'),
(120, 'aix', 'employeecontractmodel'),
(119, 'aix', 'employeecontracttypemodel'),
(148, 'aix', 'employeefawmodel'),
(118, 'aix', 'employeelanguagemodel'),
(117, 'aix', 'employeelicensedetailmodel'),
(116, 'aix', 'employeelicensetypemodel'),
(18, 'aix', 'employeemodel'),
(115, 'aix', 'employeeoftheweekmodel'),
(114, 'aix', 'employeepayrollbenefitmodel'),
(113, 'aix', 'employeepayrollmodel'),
(112, 'aix', 'employeetransactionmodel'),
(19, 'aix', 'entitymanagementmodel'),
(20, 'aix', 'entitymodel'),
(21, 'aix', 'entityunitmodel'),
(143, 'aix', 'equipmentassignmentmodel'),
(138, 'aix', 'equipmentaxlemodel'),
(151, 'aix', 'equipmentfetmodel'),
(154, 'aix', 'equipmentfuelmodel'),
(145, 'aix', 'equipmenthandovermodel'),
(144, 'aix', 'equipmentjoinmodel'),
(139, 'aix', 'equipmentmanufacturermodel'),
(140, 'aix', 'equipmentmodel'),
(142, 'aix', 'equipmenttypemodel'),
(22, 'aix', 'estimatemodel'),
(111, 'aix', 'generalnotificationmodel'),
(110, 'aix', 'holidaymodel'),
(23, 'aix', 'immigrationdetailmodel'),
(24, 'aix', 'importjobmodel'),
(109, 'aix', 'incomingdocumenthandlermodel'),
(108, 'aix', 'incomingdocumentmodel'),
(107, 'aix', 'incomingdocumenttypemodel'),
(106, 'aix', 'insurancedetailmodel'),
(105, 'aix', 'invoiceactionmodel'),
(25, 'aix', 'invoicemodel'),
(104, 'aix', 'invoicestatusmodel'),
(103, 'aix', 'invoicetypemodel'),
(149, 'aix', 'itemfawmodel'),
(150, 'aix', 'itemfawthroughmodel'),
(153, 'aix', 'itemfetmodel'),
(152, 'aix', 'itemfetthroughmodel'),
(26, 'aix', 'itemmodel'),
(27, 'aix', 'itemthroughmodel'),
(102, 'aix', 'jobapplicantmodel'),
(28, 'aix', 'jobcategorymodel'),
(101, 'aix', 'jobmodel'),
(29, 'aix', 'journalentrymodel'),
(100, 'aix', 'kpihsemodel'),
(99, 'aix', 'kpionoffmodel'),
(98, 'aix', 'kpiopsmodel'),
(97, 'aix', 'kpipobmodel'),
(96, 'aix', 'languagemodel'),
(95, 'aix', 'leavecardcarriedovermodel'),
(94, 'aix', 'leavecarddetailmodel'),
(93, 'aix', 'leavecardmodel'),
(30, 'aix', 'leaverequestactionmodel'),
(92, 'aix', 'leaverequestdetailmodel'),
(31, 'aix', 'leaverequestmodel'),
(91, 'aix', 'leaverequeststatusmodel'),
(90, 'aix', 'leaverequestworkflowactionmodel'),
(89, 'aix', 'leaverequestworkflowmodel'),
(88, 'aix', 'ledgermodel'),
(87, 'aix', 'locationmodel'),
(86, 'aix', 'maritalstatusmodel'),
(85, 'aix', 'nationmodel'),
(32, 'aix', 'notificationexternaltypemodel'),
(84, 'aix', 'notificationmodel'),
(83, 'aix', 'notificationtrackermodel'),
(82, 'aix', 'paymentmodemodel'),
(81, 'aix', 'payrolladvancemodel'),
(33, 'aix', 'payrolladvancerequestactionmodel'),
(80, 'aix', 'payrolladvancerequestdetailmodel'),
(34, 'aix', 'payrolladvancerequestmodel'),
(79, 'aix', 'payrolladvancerequeststatusmodel'),
(78, 'aix', 'payrolladvancerequestworkflowactionmodel'),
(77, 'aix', 'payrolladvancerequestworkflowmodel'),
(76, 'aix', 'purchaseordermodel'),
(75, 'aix', 'qualificationmodel'),
(74, 'aix', 'receivedemaildocumentmodel'),
(73, 'aix', 'relationshipmodel'),
(72, 'aix', 'reportmodel'),
(35, 'aix', 'requisitionactionmodel'),
(36, 'aix', 'requisitioncategorymodel'),
(71, 'aix', 'requisitionflowtypemodel'),
(37, 'aix', 'requisitionmodel'),
(70, 'aix', 'requisitionstatusmodel'),
(69, 'aix', 'requisitionworkflowactionmodel'),
(68, 'aix', 'requisitionworkflowmodel'),
(146, 'aix', 'routesurveyinfomodel'),
(147, 'aix', 'routesurveymodel'),
(67, 'aix', 'salarymodel'),
(66, 'aix', 'skillmodel'),
(65, 'aix', 'stagedtransactionmodel'),
(64, 'aix', 'taskassigneemodel'),
(63, 'aix', 'taskmodel'),
(62, 'aix', 'taskstatusmodel'),
(61, 'aix', 'taxmodel'),
(60, 'aix', 'transactionmodel'),
(59, 'aix', 'unitofmeasuremodel'),
(136, 'aix', 'userallocationmodel'),
(58, 'aix', 'vendormodel'),
(57, 'aix', 'visamodel'),
(56, 'aix', 'weekendmodel'),
(55, 'aix', 'weeklyemployeemodel'),
(54, 'aix', 'weeklyemployeeprocessedmodel'),
(38, 'aix', 'workcategorymodel'),
(53, 'aix', 'workflowactionmodel'),
(52, 'aix', 'workflowactiontypemodel'),
(51, 'aix', 'workflowmodel'),
(50, 'aix', 'workflowstatusmodel'),
(49, 'aix', 'workflowtypemodel'),
(156, 'aix', 'workorderactivityassetmodel'),
(158, 'aix', 'workorderactivitydocumentmodel'),
(159, 'aix', 'workorderactivityliftingmodel'),
(155, 'aix', 'workorderactivitymodel'),
(157, 'aix', 'workorderactivitypersonnelmodel'),
(160, 'aix', 'workorderactivitytransportmodel'),
(48, 'aix', 'workorderassetmodel'),
(39, 'aix', 'workorderjobcardmodel'),
(47, 'aix', 'workorderjobcardstatusmodel'),
(40, 'aix', 'workordermodel'),
(46, 'aix', 'workorderpersonnelmodel'),
(45, 'aix', 'workorderstatusmodel'),
(44, 'aix', 'workordertaskassetmodel'),
(41, 'aix', 'workordertaskmodel'),
(43, 'aix', 'workordertaskpersonnelmodel'),
(42, 'aix', 'workordertypemodel'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-02-24 02:25:09.726417'),
(2, 'auth', '0001_initial', '2024-02-24 02:25:10.143664'),
(3, 'admin', '0001_initial', '2024-02-24 02:25:10.230210'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-02-24 02:25:10.237225'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-02-24 02:25:10.243376'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-02-24 02:25:10.288201'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-02-24 02:25:10.327759'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-02-24 02:25:10.342255'),
(9, 'auth', '0004_alter_user_username_opts', '2024-02-24 02:25:10.349185'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-02-24 02:25:10.382341'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-02-24 02:25:10.385945'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-02-24 02:25:10.392041'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-02-24 02:25:10.405381'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-02-24 02:25:10.415871'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-02-24 02:25:10.429057'),
(16, 'auth', '0011_update_proxy_permissions', '2024-02-24 02:25:10.438045'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-02-24 02:25:10.448850'),
(18, 'aix', '0001_initial', '2024-02-24 02:32:30.726900'),
(19, 'sessions', '0001_initial', '2024-02-24 02:32:30.775349'),
(20, 'aix', '0002_assetmodel_wialon_id', '2024-02-26 10:04:57.848345'),
(21, 'aix', '0003_assetmodel_id_alter_workordermodel_is_active_and_more', '2024-03-08 15:56:37.819997'),
(22, 'aix', '0004_userallocationmodel_allocation', '2024-03-08 16:04:10.122643'),
(23, 'aix', '0005_alter_userallocationmodel_task_and_more', '2024-03-08 16:07:24.432697'),
(24, 'aix', '0006_remove_userallocationmodel_aix_useral_work_or_75bd01_idx_and_more', '2024-03-08 16:09:41.683493'),
(25, 'aix', '0007_alter_userallocationmodel_task_and_more', '2024-03-08 16:12:32.871578'),
(26, 'aix', '0008_remove_kpipobmodel_work_order_kpipobmodel_task_and_more', '2024-03-21 04:53:02.750341'),
(27, 'aix', '0009_kpionoffmodel_task_kpipobmodel_work_order', '2024-03-21 06:14:14.623783'),
(28, 'aix', '0010_alter_kpionoffmodel_status', '2024-03-21 06:14:14.760125'),
(29, 'aix', '0011_alter_kpionoffmodel_task', '2024-03-21 06:14:15.248385'),
(30, 'aix', '0012_alter_kpipobmodel_activity_location_and_more', '2024-03-21 06:39:51.236994'),
(31, 'aix', '0013_remove_kpionoffmodel_work_order_and_more', '2024-03-21 06:51:04.993969'),
(32, 'aix', '0014_alter_employeemodel_name', '2024-03-22 06:37:37.939956'),
(33, 'aix', '0002_kpiopsmodel_equipment', '2024-10-15 12:27:19.497182'),
(34, 'aix', '0003_rename_aix_absenc_created_250d79_idx_aix_absence_created_134fa8_idx_and_more', '2024-10-15 12:48:13.224330'),
(35, 'aix', '0004_rename_aix_absenc_created_250d79_idx_aix_absence_created_134fa8_idx_and_more', '2024-10-15 12:53:45.373875'),
(36, 'aix', '0005_aixitsstatusreportmodel', '2025-01-06 12:41:53.431485'),
(37, 'aix', '0006_rename_priorities_aixitsstatusreportmodel_priority', '2025-01-06 12:45:45.202975'),
(38, 'aix', '0007_aixitsstatusreportmodel_description', '2025-01-07 07:20:28.240918'),
(39, 'aix', '0008_equipmentaxlemodel_equipmentmanufacturermodel_and_more', '2025-01-08 07:55:27.110359'),
(40, 'aix', '0009_equipmentassignmentmodel_equipmentjoinmodel_and_more', '2025-01-24 08:22:11.978541'),
(41, 'aix', '0010_remove_equipmentmodel_chassis_and_more', '2025-03-31 08:02:05.120871'),
(42, 'aix', '0011_alter_equipmentmodel_yom', '2025-03-31 08:09:04.026407'),
(43, 'aix', '0012_alter_equipmentmodel_details', '2025-03-31 08:10:38.272059'),
(44, 'aix', '0013_equipmentmodel_serial', '2025-03-31 09:08:41.503833'),
(45, 'aix', '0014_equipmentmodel_code', '2025-03-31 09:11:54.817600'),
(46, 'aix', '0015_alter_equipmenttypemodel_code', '2025-03-31 11:37:51.556551'),
(47, 'aix', '0016_equipmenthandovermodel', '2025-04-01 07:26:40.959974'),
(48, 'aix', '0017_alter_equipmentmodel_reg_no', '2025-04-03 10:11:52.783671'),
(49, 'aix', '0018_alter_equipmentmodel_active', '2025-04-11 05:31:50.441527'),
(51, 'aix', '0019_equipmenthandovermodel_approved_by_hr_and_more', '2025-05-06 12:59:06.134482'),
(52, 'aix', '0020_equipmenthandovermodel_approved_by_hr_and_more', '2025-05-14 07:42:30.745411'),
(53, 'aix', '0021_equipmenthandovermodel_approved_by_hr_and_more', '2025-05-14 11:34:12.756122'),
(54, 'aix', '0022_equipmenthandovermodel_approved_by_hr_and_more', '2025-05-15 08:29:30.872322'),
(55, 'aix', '0023_equipmenthandovermodel_approved_by_hr_and_more', '2025-07-10 09:20:17.510642'),
(56, 'aix', '0024_equipmenthandovermodel_approved_by_hr_and_more', '2025-07-10 09:20:19.296493'),
(57, 'aix', '0025_employeefawmodel_faw_status_and_more', '2025-07-10 09:51:01.525655'),
(58, 'aix', '0026_employeefawmodel_approved_date_and_more', '2025-07-14 08:16:49.776700'),
(59, 'aix', '0027_remove_itemfawmodel_employee_and_more', '2025-07-14 09:19:32.072724'),
(60, 'aix', '0028_rename_employee_itemfawthroughmodel_employee_model_and_more', '2025-07-14 12:40:49.931307'),
(61, 'aix', '0029_equipmenthandovermodel_approved_by_hr_and_more', '2025-07-14 13:16:17.326600'),
(62, 'aix', '0030_alter_employeefawmodel_faw_items', '2025-07-14 13:16:17.628519'),
(63, 'aix', '0031_remove_itemfawthroughmodel_aix_itemfaw_faw_mod_e5e8b0_idx_and_more', '2025-07-14 13:22:15.328671'),
(64, 'aix', '0032_equipmenthandovermodel_approved_by_hr_and_more', '2025-07-16 11:27:25.255731'),
(65, 'aix', '0033_equipmenthandovermodel_approved_by_hr_and_more', '2025-07-16 13:19:33.109606'),
(66, 'aix', '0034_equipmenthandovermodel_approved_by_hr_and_more', '2025-07-16 13:28:49.748538'),
(67, 'aix', '0035_equipmenthandovermodel_approved_by_hr_and_more', '2025-07-16 13:32:09.749180'),
(68, 'aix', '0036_employeefawmodel_markdown_notes_and_more', '2025-07-17 13:34:03.278265'),
(69, 'aix', '0037_equipmenthandovermodel_approved_by_hr_and_more', '2025-07-17 13:48:39.692940'),
(70, 'aix', '0038_equipmenthandovermodel_approved_by_hr_and_more', '2025-07-21 09:35:37.475804'),
(71, 'aix', '0039_equipmenthandovermodel_approved_by_hr_and_more', '2025-07-21 13:12:08.882311'),
(72, 'aix', '0040_equipmenthandovermodel_approved_by_hr_and_more', '2025-07-22 08:18:32.869994'),
(73, 'aix', '0041_equipmenthandovermodel_approved_by_hr_and_more', '2025-07-22 09:23:00.655500'),
(74, 'aix', '0042_equipmenthandovermodel_approved_by_hr_and_more', '2025-07-24 09:55:33.680402'),
(75, 'aix', '0043_customerlocationmodel_is_active_and_more', '2025-07-24 11:38:33.562372'),
(76, 'aix', '0044_equipmenthandovermodel_approved_by_hr_and_more', '2025-07-25 06:51:16.239734'),
(77, 'aix', '0045_equipmenthandovermodel_approved_by_hr_and_more', '2025-07-28 08:14:22.305544'),
(78, 'aix', '0046_rename_genera_notes_routesurveymodel_general_notes_and_more', '2025-07-28 09:38:01.315342'),
(79, 'aix', '0047_equipmentfetmodel_asset_and_more', '2025-07-29 11:58:02.347742'),
(80, 'aix', '0048_remove_equipmentfetmodel_asset_and_more', '2025-07-29 12:56:05.783037'),
(81, 'aix', '0049_equipmenthandovermodel_approved_by_hr_and_more', '2025-08-19 09:27:40.614571'),
(82, 'aix', '0050_equipmenthandovermodel_approved_by_hr_and_more', '2025-08-20 11:13:40.360200'),
(83, 'aix', '0051_workorderactivitymodel_workorderactivityassetmodel_and_more', '2025-08-20 11:13:43.068083'),
(84, 'aix', '0052_equipmenthandovermodel_approved_by_hr_and_more', '2025-08-21 13:17:11.996682'),
(85, 'aix', '0053_equipmenthandovermodel_approved_by_hr_and_more', '2025-08-22 08:25:48.967723'),
(86, 'aix', '0054_equipmenthandovermodel_approved_by_hr_and_more', '2025-08-22 10:07:24.253929'),
(87, 'aix', '0055_documentmodel_activity_documentmodel_task_and_more', '2025-08-26 10:05:30.788079'),
(88, 'aix', '0056_equipmenthandovermodel_approved_by_hr_and_more', '2025-08-26 10:14:49.889520'),
(89, 'aix', '0057_equipmenthandovermodel_approved_by_hr_and_more', '2025-08-27 06:39:46.244522'),
(90, 'aix', '0058_equipmenthandovermodel_approved_by_hr_and_more', '2025-09-02 08:27:19.796436'),
(91, 'aix', '0059_equipmenthandovermodel_approved_by_hr_and_more', '2025-09-02 12:34:19.478374'),
(92, 'aix', '0060_equipmenthandovermodel_approved_by_hr_and_more', '2025-09-03 08:17:16.865417');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('09in9q17cnlk0rvf6u1kiy533cqt09o5', '.eJxVj7GOwyAQRP-F-mwBBgMu0193PVrMEpOzcWSwTlGUfz8cuYm22n0zs5onsRlzjmuyMcViS1wwF1julgxMyU4ZpSVrORNMM_5FLOxlsnvGzUZPBsLJx83B-IvpAP4G6bq245rKFl17SNqT5vZ79ThfTu1HwAR5qm4ULlAlAkgz6kC9QGM0Dyh5HUOVAslZb0ALCsHzzo2cIe0ZraeeSV1D_W22HgPsc7GYSiwPuxxvyfAk577v7w5GgFKu7xvhpG9E9TROU9Y40LKnXndhPAJPU573azV1f_DIzX2bhObvEidOsGDFP9OGeEjI6_UPb2Fz7g:1ugkw7:3as0Z_b94Zyaa5i-OzXANDmjknLrGWWGtZaZEV1iUGg', '2025-08-12 14:04:11.583363'),
('0jnz2egzjh6nzul7ip3g5rl70e5sozj6', '.eJxVj71uwzAMhN9Fc2xIin4zZu_WXaAsKlZry4ElowiCvHvlwEMLTuTdRx6fxMFWR7cVXF0K5EI4Of2deRi-Me9C-IJ8W_phyXVNvt8t_aGW_mMJOF0P778FI5Sx0Sh8pFpEkHYwkQaB1hoeUfJWlmoNkjNlwQgKMfCzHzhDqhhtI8Wk2ZcWLCUt2aWcqqtpxlJhvjtyYVoqQ4XlumdMNEqdWtzJBYywTdVhrqk-3LyHJJcnOfpte39sBWjtleqEl6ETjem8oazzYKSiwZzjsJ8_oDJttwadf-BRuvs6CsPfLx9yhhmb_DmuiLuFvF6_qNlz6g:1utNDL:0wrF8jLYTY_Z-fWNH-UlNrMQGOaTC09PQDJfdRzEq_w', '2025-09-16 09:22:07.151709'),
('0lqdmo8kapi61otmdcd0pr0iuwkawgm9', '.eJxVTz1vwyAQ_S_MsQUYA_aYvVt3dJgjprVxZLCqKMp_L0QeWt109z7uvScxcOTZHAl3ExwZCSeXvzcL0zfGCrgviLetnbaY92DbSmlPNLUfm8PlenL_GcyQ5qJGYT1VwkM_TNpTJ3AYNPfY8zIDVQp6zuQAWlDwjnd24gypZLScJOt1NU2YUtiiCTFkk8OKKcN6N2RkSqiOFq5sqegUpepS4i7GoYdjyQZjDvlh1hqSjE9y7sfxbjwIUMpK2Qjbu0YUTWM1ZY0F3UvqdOen-v4UpeW4FVH3A4_U3PdZaP6ufMIRVizw57wjVgp5vX4Bo2tz4Q:1uFUpk:H6MzsCXIdYPdrG9lRXZh8Jtd7ta9YGUoWIdU3JNI1vI', '2025-05-29 09:24:56.065796'),
('0u70upb5wauvfepz3jd5f6fu14w21kd2', '.eJxVULtuhDAQ_BfXB7LBLyjTp0tvrfE6OAFzwkbJ6XT_HvtEkdNWO4_V7NzJkXCPsCIZCbg1RHIhBo48m0qY4ArevWIWpm-MlXBfED-3dtpi3oNtq6Q92dS-bw6Xt1P7cmCGNBc3cuup4h7EMGlPHcdh0J1H0ZUZqFIgOiYH0JyCd11vp44hlYwWSDKh69GEKYUtGvy9hv1Gxp7Sf2iIIZscVkwZ1qshI1NCasopo63ouRqouJQnFuPQw7FkgzGHfDNrjU7GOzn343j2MHBQykrZcCtcw4unsZqyxoIWkjrd-6mGOk1pOT6Lqf-BW2qu-8x19yzipM_OP-YdsUrI4_EH4aiB3g:1utMyY:perTVr7r9eLrPuXTwhJdS8Ee4Wo9HTW8TNeXApFrumA', '2025-09-02 09:11:50.664182'),
('102q0mp42far3jns14gzaoh4evq68uy3', '.eJxVjMFuwyAQRP-Fc4SWNRjwsfd8A1qbJaatcWSI1CrKv8eWckg0t_dm5i5ulbdCC4tBUFxyEScR6NbmcIiQ487xk400_XA5RPymclnltJa25VEeFfmyVZ7XyL9fr-7HwUx13tesxwRWJzJ-cgmiZu8dJja4x4O1ZFD1npwGShG7cULF0CvYUa-MO04r15rXEvjvmrd_MXQAbzSX3ELLC9dGyzWIQVnUXYdorFTO9aDd4wngB1Nr:1sh7ab:W4A8Ob1h969KxGbndpyFzbxKqfKqp1OQfyrJk8JLfms', '2024-08-22 13:15:57.193772'),
('15easnbwyjaldx2m3bj0ad9c5jjsrlpn', '.eJxVkL1uwzAMhN9Fc2xIiv7ssXu37gJlUbFaWzYsGWgQ5N0rBx4acOJ9PIK8B9kzbglmJD0BP8dELsTCXkZ7ABt91fm75mD4wXQA_w3ptrTDksoWXXuMtCfN7eficfo4Z98WjJDH6kbhAtUigOwGE6gX2HWGB5S8Vke1BsmZ6sAICsHzqxs4Q6oYrZJi0hxLM-Ycl2Txd43bnfRXSv-pMcViS5wxF5hXS3qmuTGdYYq1Umgh1KX-MFmPAfapWEwllrudj8tJ_yBnv--vGDoBWjulGuGkb0T1NM5Q1jgwUlFvrmE4bjpNedpv1VRqi6lZt1EY_gri5GfmXy9Ons8_hEuBBw:1t0HOD:KENhsdwCaIcfQMCyhvMaJuvgm_CuZlyvLHcTQ9v9LCA', '2024-10-14 09:34:21.899700'),
('1df4g905xdajso1mjfj4782w2a5jtoo8', '.eJxVkLtuwyAUht-FObYgXO0xe7fu6GAOMa2NI4PVRlHevTjy0Ix8_0WH_0G2jGuCGUlPZkh-ISdiYSuj3QUbfeXsnTkYvjHtgv-CdF3aYUllja7dLe2h5vZj8ThdDu9bwQh5rOmAXSdDoEbL4AKA6Dit6FzZIJEJlOCkEowCCmOGQXDlDQPwnVPIUe-lGXOOS7L4e4vrnfSc0n80plhsiTPmAvPNkp5pKZWmXNOWKSOVPNU_TNZjgG0qFlOJ5W7n_XLSP8jx3rbXDJ0ArZ1SjXDSN6JmGmcoaxzUJuoND4OpNx2hPG3XGuI_cM_NbR2FOb92OORj8s9xRdwt5Pn8A-fjg0s:1uoc43:BsPN6BkUZkIFB1gAo9SCS55F9ZDhu7EYkEyJ5fKAECE', '2025-08-20 06:17:51.427429'),
('1kpoqk1hypemvvt71xfkfqf8arx652rg', '.eJxVjEFuwyAQRe_COkKAYdx62X3PgAaY1LQxWAyuEkW5e20pi2b73vv_LjamVnAhMYleO154W6n9Zq5NnITHrc_-SHxOewGvLGD8oXKI9I3lq8pYS285yCORT8vysya6fDzbl4MZed7XaMzZWozJOWcGpd8JEVQaIThrFBrQ4HQgtxszQNhbojFE8zYoSBDDccrEnGvxdF1zu4lpUOofzSV33_NC3HFZvZj0qLXT1iolR2cB9OMPFsdX3g:1rpL4y:ZK5P7qhc3Yw_D6XRVvxovpCqDzjWSovQix-nKmCNJNk', '2024-03-27 04:45:00.773121'),
('1ldiwq6bryak506lenqw39dow2fwc3u6', '.eJxVT8tugzAQ_BefA_ITG46599a7tcbr4BZMhI2qKMq_10QcWu1pdx478yQW9jLZPeNmoycD4eTy9-Zg_MZ0AP4L0m1txzWVLbr2oLQnmtuP1eN8Pbn_DCbIU1WjdIFqGUD1ownUS-x7wwMqXqenWoPirOvBSArBc-FGzpB2jNZTx5Q5TDPmHNdkY4rFlrhgLrDcLRmYVkIzyoxoqRBGSX6pcWfrMcA-F4upxPKwyxGSDE9y7vv-btxL0Np1XSOd8o2smsYZyhoHRnXUGxHG4_0pyvN-qyLxA4_c3LdJGv6ufMIJFqzw57QhHhTyev0CpIZz4w:1ugO87:Ugf-wfSTKF8NGorFI4ngOrAnwEgVt0bt2owKWrzRV1E', '2025-08-11 13:43:03.488229'),
('1y5mc9qr29aob5uiverwpfkvukfi1mnr', '.eJxVkEFvhCAQhf8L59WAAqLH3nvrnQwyrLSKRjDpZrP_vWg4dI_zvfcmM-9Jjoh7gAXJQBYIdiU3ouFIkz4F7W3m7J0ZGH8wnIL9hnBf63ENafemPi11UWP9uVqcP4r3bcEEccpph30vnKOqE844AN63NKMms1Eg4yjACMkZBeRKjSNvpVUMwPZGYovduTRijH4NGn83vz_I0FL6j_rgk05-wZhg2TQZWMdb3jDGZM0bSaWUt_zErC06OOakMSSfHno5TyfDk5T5OK4eeg5dZ6SsuBG24jlTGUVZZUAJSa1q3ajyUSUU5-OeQymPGKptn7hqriaKXkr_unTyev0BUlKCuA:1tzDTQ:x0hWMm-f1ntpEgv8dogu3T4dL6avXjWWE61E7w6u2Ws', '2025-03-31 11:43:36.444300'),
('271dmh14atriut6ggnayvuoxxwedqm2n', '.eJxVULluhDAQ_RfXCzLGJ2X6dOmtMR4HJ2BW2ChZrfbfY1YUWU0175jj3cmecUuwIBkI-CUmciEW9jLZg7DRV5y9Yg7Gb0wH4b8gfa7tuKayRdcekvZkc_u-epzfTu3LgAnyVN3IXaCKBxBm1IF6jsZoFlCwWoYqBYJ10oDmFIJnvRtZh1R2tEKyE_oYmjHnuCaLv9e43cjQU_oPjSkWW-KCucBytWTolJBaGdOZVktWl_NLfWK2HgPsc7GYSiw3uxynk-FOzn7fnzkYDko5KRvuhG949TRO065xoIWkXvdhPI46TXneP6up_4Fbbq7bxDV7BnHSZ-Yf04Z4SMjj8QfyRYH6:1utgiu:6TpMw6V-pO-r9a0es4qdszpujScDh8JtgtjamM0sS8o', '2025-09-03 06:17:00.749463'),
('2queko0zbbanrd0vdr2owmeyen7x5vdq', '.eJxVUD1vwyAQ_S_MsQUYDPbYvVt3dJijprVxZLDaKMp_L0QeGt107-P07t3JkXCPsCIZCbg1RHIhBo48m0qY4ArOXzEL0zfGSrgviJ9bO20x78G2VdKebGrfN4fL26l9OTBDmosbhfVUCQ9ymLSnTuAwaO5R8jIDVQokZ_0AWlDwjnd24gxpz2iBeiZ1PZowpbBFg7_XsN_I2FH6Dw0xZJPDiinDejVkZEpKqRlXtGXdQKnSl_LEYhx6OJZsMOaQb2at0cl4J-d-HM8eBgFK2b5vhJWuEcXTWE1ZY0HLnjrd-amGOk1pOT6LqfuBW2qu-yw0fxZx0mfnH_OOWCXk8fgD5AyB4g:1uoEsw:xR0ChPDIzmBWKLGBrBWu3elSJOCxTaztHYd-iFF29KM', '2025-08-19 05:32:50.577200'),
('3a4rawybl70o1n7zcecdftdnltcxr85x', '.eJxVULtuhDAQ_BfXBzLGLyjTp0tvrfE6OAFzwkbJ6XT_HvtEkdNWO4_V7NzJkXCPsCIZCbg1RHIhBo48m0qY4ArOXjEL0zfGSrgviJ9bO20x78G2VdKebGrfN4fL26l9OTBDmosbufVUcQ9imLSnjuMwaOZRsDIDVQoE6-QAmlPwjvV2Yh1S2dECyU7oejRhSmGLBn-vYb-Rsaf0HxpiyCaHFVOG9WrI2Ckh2dArTtui1FyLS3liMQ49HEs2GHPIN7PW6GS8k3M_jmcPAwelrJQNt8I1vHgaq2nXWNBCUqd7P9VQpyktx2cx9T9wS811n7lmzyJO-uz8Y94Rq4Q8Hn_lzYHl:1urEEO:IO8h1GIIXcdOppQ5PvmifsTlPIG6FhiFcsAe9yQcdI4', '2025-08-27 11:27:20.727923'),
('3cqidd9x7v8068op3ts9djp4wls7vha6', '.eJxVj09vwyAMxb_KxLmJgPEn5Lj7btsZOcGktAmpCkzbqn73kSrSNvnk5997tm_EQslHWxJebXCkJ5wc_moDjGeM28CdIE5rO64xX8PQbki7T1P7ujqcX3b2X8AR0rG6UQyeauFBmrHz1Ak0puMeJa9lqNYgOVMGOkHBO_48jJwhVYxWSTHZbaEJUwprtCGGbHNYMGVYLpb0THOhlaRGtUJzI9WhXjtbhx7KnC3GHPKXXbYbSX8je1_K42FmOuo4-EYisEaAk83AUDeaca2ZV1QyXbfvpjSXqZrymmFuygTRQfMtBvz4vJx-qQgLVupto57eHxS5338A2cV3Kw:1siwBs:4EFUOo_kAYXm7kQXJc5I6ZaWW-Sjtfzm1uX7UpCtzzM', '2024-09-10 13:24:56.481136'),
('3kp0wwua564mz50lorhfr9h29xkpm9b4', '.eJxVUDtvgzAQ_i-eA7LBLxi7d-tunfG5uAUTYaM2ivLfa0cMjW6676W7706OhHuEFclIwK0hkgsxcOTZVMIEV_DuFbMwfWOshPuC-Lm10xbzHmxbJe3JpvZ9c7i8ndqXgBnSXNzIraeKexDDpD11HIdBdx5FV2agSoHomBxAcwredb2dOoZUMlogyYSuoQlTCls0-HsN-42MPaX_0BBDNjmsmDKsV0NGpoRUjDHOW6H6En8pPyzGoYdjyQZjDvlm1no5Ge_k3I_jWcPAQSkrZcOtcA0vnsZqyhoLWkjqdO-netNpSsvxWUz9D9xSc91nrrtnDyd9Vv4x74hVQh6PP3Hkgak:1usyoi:6Chfcv7bI_SK-U7UyVDAkajEVmcB7srM27t8Tusfsz0', '2025-09-01 07:24:04.916858'),
('428vzqk8sxcykzwo1i062k6hd0wyr9r0', '.eJxVj71yhDAMhN_F9cHYxn9QXp8uvUfG8uEEzA02Rebm3j2GoUhG1erTaqUXsbCXye4ZNxs9GQgnt789B-M3pgP4L0iPtR3XVLbo2mOkvWhuP1aP8_2a_bdggjxVNwoXqBYBZD-aQL3Avjc8oOS1eqo1SM5UD0ZQCJ53buQMqWK0thST5liaMee4JhtTLLbEBXOB5WnJwLQQneykEi0ThmupbvXc2XoMsM_FYiqx_NjlOJIML3LpfT8_7gVo7ZRqhJO-EdXTOENZ48BIRb3pwnjEX6Y8749qKlViap7bVAPPny-eYMHKP09O3u9fzmNzOg:1u382u:JhW_apQ4FrbXhRH3b7cx0ycW7wzPy97mdDIfhDzyEmY', '2025-04-25 06:39:24.164161'),
('47kzar4jto5odoem0g9524cfo02lbh7b', '.eJxVjDkOwjAUBe_iGlmJ15-U9JzB-t6IgdgodirE3cFSCmjfzJsXMbi3xew1bCZ5MhNJTr-bRXcPuQN_w3wt1JXctmRpV-hBK70UHx7nw_0LLFiX7xuk9BC8GDR3ikmBjGvhohgiWIVKR20dH9kkRlQ-aoggI4-j5qDl6KTr0RpqTSWblFMzLa2hNlyfhsxdk6AGPlHGQExMvz867UXD:1teveJ:vIrTs6WMZs9xLVZluKxzqYUeyaDElXAPvDr86EXGKts', '2025-02-17 12:33:59.334217'),
('547seg5t74k13czf5ppstdxbhutenun0', '.eJxVkEGPhCAMhf8L59EAIqDHve9t76RIGdlVNILJTibz3xeNh5301Pf1Ne17kj3hFmFG0hNwc4jkRgzseTQHMMEVnb9rFoYfjAdw3xDvSz0sMW_B1sdIfdFUfy4Op49r9m3BCGksbhTWUyU8tN2gPXUCu05zjy0v1VGloOVMdqAFBe94YwfOkEpGiyRZq4-lCVMKSzT4u4btQfqG0n9qiCGbHGZMGebVkJ6pRvJGcK5qyoRQWtzKE5Nx6GGfssGYQ36Y-Tid9E9y9ft-5tAJUMpKWQnbukoUT2U1ZZUF3UrqdOOH46jLlKb9Xky5tBirdRuF5mcSF79C_zo5eb3-AOeJgSc:1tV3pr:oBQOKtvhlPqPvk7uF4_M6kusXn6C8YQiKSPNe6e1ixA', '2025-01-07 07:22:07.052945'),
('5li0fs5au81hq154yu2vzfbf84q4pz7u', '.eJxVjDsOwyAQRO9CHaHlYy-4TJ8zIGyWmHwgMriKcvfYkotEmmrevHkz59c2u7XS4lJgA9Ps9NuNfrpT3kG4-XwtfCq5LWnk-4QftPJLCfQ4H9u_g9nXebO9nozZgohRgcQgbCDbgRRolPQWQxQolIaOoraq15YsCmmgi7ZXAffTSrWmkl3KqbmWnlSbf74cGzYTQFkhgPdaAYD-fAHwCESM:1rj9Hy:iXZtml8dxuEd2rH_Z5qU2WXKV9P65entVMHBZZh7Szs', '2024-03-24 02:51:50.753436'),
('5pr5powbn2vtbka30ay0278vqm0s1kq1', '.eJxVULtuhDAQ_BfXBzLGT8r06dJba7wOTsCcsFFyOt2_B58octpq57GanTvZM24JFiQDAb_ERC7Ewl4mWwkb_YGzV8zB-I2pEv4L0ufajmsqW3RtlbQnm9v31eP8dmpfDkyQp8ON3AWqeABhRh2o52iMZgEFO8ZQpUCwThrQnELwrHcj65DKjh6Q7ISuRzPmHNdk8fcatxsZekr_oTHFYktcMBdYrpYMnRK9okYq0wqmtBTscjwxW48B9rlYTCWWm11qdDLcybnv-7MHw0EpJ2XDnfANPzyN07RrHGghqdd9GGuo05Tn_fMw9T9wy811m7hmzyJO-uz8Y9oQq4Q8Hn_vo4H2:1ugNzz:fn9E4zCS6gkpKrkWAeMttaLyj7IptFdAtxCo1z4-2Zg', '2025-07-28 13:39:39.597453'),
('5xeiu075r3z092w67x6d8m1rkikjnacd', '.eJxVjEtuxCAQBe_COkJgYz5eZp8zoDY0MUkMFo2jRKO5e2xpFpltVb13YwdhK7Ahmxnljr1Bob22TseO7TtTbeyFeTj66q_U53iW6pktED6xXCJ-QHmvPNTSW174lfCHJf5WI369PtqngxVoPdd6ABeFTiGgG61VSg42KjfiYtApE7QEk5xAFZMeJ5jMYtXpU4jBpEmb65SQKNfi8WfP7ZfNoxD_aC65-543pA7b7tksjRR2UE46LpQWk7P3P1_zXFA:1rmRiJ:W0nG0WQooRzVIecto8MeV3_ze3bXwDl1EnM-ZTViu_0', '2024-03-19 05:13:39.058452'),
('63qlskuia9dwgh5853azvcwizl7j02go', '.eJxVjMFugzAQRP_F58paYwwLx97zDdbauxQ3wUTYkRJV_feAlENymMu8N_OnbkW2TIuoUREvKceLbGf1pTzd6uwP6hPv0H52geJZ8gH4l_LPquOa65aCPhT9okWfVpbL98v9OJipzPsammBwaFrjWrGwZ5g4oAM2GIBc19PUTxwdIrB1FLu2ZTOBs24QGVw4TouUktbs5X5N20ONFuCtTTlVX9MipdJy9Wo0PSB2DRqje9ugxe7_CfgKVd0:1reDHP:oEbLCNLP8VSosg0NV98_MjZV0HeHv6MgOMKSE2VUZSk', '2024-02-25 12:11:51.853475'),
('657v379dkul3ucovr243vwow6cv2u1k3', '.eJxVkEGPhCAMhf8L59EAgqDHve9t76RIGdlVNILJTibz3xeNh5301Pf1Ne17kj3hFmFG0hNwc4jkRgzseTQHMMEVnb9rFoYfjAdw3xDvSz0sMW_B1sdIfdFUfy4Op49r9m3BCGksbhTWUyU8yG7QnjqBXae5R8lLdVQpkJy1HWhBwTve2IEzpC2jRWqZ1MfShCmFJRr8XcP2IH1D6T81xJBNDjOmDPNqSM8Ul5RTqUUtlGgE47fyxGQcetinbDDmkB9mPk4n_ZNc_b6fOXQClLJtWwkrXSWKp7KassqCli11uvHDcdRlStN-L6ZcWozVuo1C8zOJi1-hf52cvF5_5DqBIQ:1sk0ef:BnfRqBExYp9sk9EQIqJno3t9O_WDDo2zlSBRZxY_dqQ', '2024-08-30 12:28:05.012171'),
('66jp0f0s8xluf4b9ua2zt93pum8vjmnj', '.eJxVUD1vwyAQ_S_MsQU2GPDYvVt3dJijprVxZLDaKMp_L0QeGt1070t3706OhHuEFclIwK0hkgsxcOTZVMIEV_DuFbMwfWOshPuC-Lm10xbzHmxbJe3JpvZ9c7i8ndqXgBnSXNzIraeSexB6Up46jlqrzqPoymgqJYiODRoUp-Bd19upY0gHRgs0MKFqaMKUwhYN_l7DfiNjT-k_NMSQTQ4rpgzr1ZCRSdFTqUp4q1kvOGWX8sRiHHo4lmww5pBvZq2nk_FOzv04nj1oDlLaYWi4Fa7hxdNYRVljQYmBOtX7qR51mtJyfBZT_wO31Fz3mavuWcRJn51_zDtilZDH4w_k2oHj:1udjuG:8vBbwUjulcpQg0vrXC-652GfVBocLKoky6o3H_M48uE', '2025-07-21 06:26:48.068689'),
('6jlod5iqqb9uuf1iavtoizcbbxxcoyra', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE3MTEwMjk4MjYuNTE1MjkzMX0:1rnJ1G:DdPtFxZcFSQRsuqQ1b7E3xHfcSEm4tnPtyec0Rn2r1M', '2024-04-04 14:03:46.526470'),
('6lhls50ya5qn7kiwtl5kueej6h8zeb02', '.eJxVULtuhDAQ_BfXB_LbhjJ9uvTWGi_BCZgTNkpOp_v34BNFTlvtPFazcyd7xi3BgqQnEJaYyIU42MvkKuFiOHD-inkYvjFVInxB-lzbYU1li76tkvZkc_u-BpzfTu3LgQnydLhR-pEaOYLqBjvSILHrLB9R8WM6agwoznQHVlIYAxd-4AypZvSANFO2Hs2Yc1yTw99r3G6kF5T-Q2OKxZW4YC6wXB3pmVFSGNEp1nKmhNH6cjwxu4Aj7HNxmEosN7fU6KS_k3Pf92cPnQRjvNaN9Co08vA03lLWeLBK02DFONRQpynP--dhEj9wy811m6TlzyJO-uz8Y9oQq4Q8Hn_neoHo:1ujAo3:HAja6oiDJD80OUTIqm4ERzv2783OUbvn9APM74IYtK4', '2025-08-05 06:10:51.340922'),
('7469vdt19lcmcau2730kozexj5jb92oi', '.eJxVkL1uwzAMhN9Fc2xI0a89Zu_WXaAsKlZry4Elow2CvHvlwEMz8rs7grwH2TKuCWYkPZkh-YWciIWtjHYXbPSVs3fmYPjGtAv-C9J1aYcllTW6dre0h5rbj8XjdDm8bwtGyGNNB-w6GQI1WgYXAETHaUXnygaJTKAEJ5VgFFAYMwyCK28YgO-cQo56X5ox57gki7-3uN5Jzyn9R2OKxZY4Yy4w3yzpmZa8U1pz1p5Zx6RQp_rEZD0G2KZiMZVY7nbeTyf9gxzztr166ARo7ZRqhJO-ETXTOENZ48BIRb3hYTD1qCOUp-1aQ_wH7rm5raMw51cRh3x0_jmuiLuFPJ9_WbKDgA:1uhT88:UIlJVShnXJEVA2R6uygZ1Bi6rUIbOOoVi9H6mLUOIig', '2025-07-31 13:20:32.548591'),
('7fl67y3d9yct01lu8kk0axvte5pd7a40', '.eJxVkL1uwzAMhN9Fc2xI0a89Zu_WXaAsKlZry4Elow2CvHvlwEMz8rs7grwH2TKuCWYkPZkh-YWciIWtjHYXbPSVs3fmYPjGtAv-C9J1aYcllTW6dre0h5rbj8XjdDm8bwtGyGNNB-w6GQI1WgYXAETHaUXnygaJTKAEJ5VgFFAYMwyCK28YgO-cQo56X5ox57gki7-3uN5Jzyn9R2OKxZY4Yy4w3yzpmRZKUS21apnQknN9qk9M1mOAbSoWU4nlbuf9dNI_yDFv26uHToDWTqlGOOkbUTONM5Q1DoxU1BseBlOPOkJ52q41xH_gnpvbOgpzfhVxyEfnn-OKuFvI8_kHWriDgg:1uCaPw:-q8iFMtwzbZ74mpQmY_nEuwqmkxViiAb-6GnPfCYKF4', '2025-05-07 08:51:16.390616'),
('7pq000144e6r3c8s5wype0wdrjyphzpl', '.eJxVUD1vwyAQ_S_MsQUYDHjs3q07Osy5prVxZLDaKMp_L0QeGt107-P07t3JkXCPsCIZCPg1RHIhFo4820rY4AvOXzEH4zfGSvgviJ9bO24x78G1VdKebGrfN4_L26l9OTBDmosbhZuoEhNIM-qJeoHGaD6h5GUMVQokZ70BLShMnndu5Axpz2iBeiZ1PZowpbBFi7_XsN_I0FH6Dw0xZJvDiinDerVkYEpK2gtjVMu0ltxcyg-L9TjBsWSLMYd8s2tNToY7OffjeNZgBCjl-r4RTvpGFE_jNGWNAy176nU3jTXTaUrL8VlM3Q_cUnPdZ6H5s4eTPiv_mHfEKiGPxx-AroHD:1um4Zx:aDeRO-VP1W_xLsHsYkrj_6oH8PdJiJE8KA11uXq8W4E', '2025-08-13 06:08:17.767599'),
('7wybfdnd29ko89koz7clolh8zxuohera', '.eJxVjMFuwyAQRP-Fc4UWYwz42Hu-AS3suqaJcWSIlKjqv8eWckgOc5n3Zv7ErfJWcGExCqQll3Th7Sy-RMBbm8NBQ6Yd6s8uYjpzOQD9YvlZZVpL23KUhyJftMrTSnz5frkfBzPWeV9DF5XzXa9Mzxr2-ImiM0DKRUAzWJzsRMk4B6QNpqHvSU1gtPHM3sTjtHKteS2B79e8PcSoAd7aXHILLS9cGy7XIEZlFVhtnbUSjPJ26P6f9_hV3A:1rm54P:J9XQDTCdIkXnxhASucceBLUg-qOtYCsoautnLyKB6AM', '2024-03-18 05:02:57.166570'),
('8iywdtz1o4vzuhnkh5axhsxi46jf54y6', '.eJxVjMsOwiAQRf-FtSHDo6V06d5vIANMLWqpKZhojP9um3Sh23PuPW_2KLRknIj1DOOUMjswh486uk24FFcu_5nHcKW8iXjBfJ55mHNdkufbhO-28NMc6Xbct3-BEcu4vrvWeENIHtBrKxoF0SK1YFCBjaYLw0CdajoDUQrhvdYUAGQrYJAaA27RQqWkOTt63tPyYr0C-KEpp-pqmqhUnO6O9cKAtUJqDXxNKtWKzxcjC1Qo:1ricKu:eX4JY_YGA8nNtbALjDW77Z4eouq9L5OpNWw7kLHVQ1k', '2024-03-08 15:45:40.425049'),
('8xtvk0zczdt6x9o8tiibnpn0f4te6w8d', '.eJxVjDkOwyAURO9CHSFjdpfpcwb0gU9MFogMrqLcPbbkxtVIb97Ml7iGreVaXC65u57f2Dq8P45MTHOtRj0oS7dkWl6Ig7XPbm24uBzJRBg5MQ_hiWUv4gPKvdJQS1-yp7tCj7bRW434uh7u6WCGNm_rhNbKlAajZfIJQFg-bGjcWJDIBErwUgk2AApjQhBcRcMAovUKOWry-wP3lkbZ:1tauB3:iaz24780CX1Z2lgSJ5a52zxjRHvDA5l9dOHlCs0za4A', '2025-02-06 10:11:09.868294'),
('9kk91v5le8qndadw4s9oikufenl3qnd0', '.eJxVj7GOwyAQRP-F-mxBvGBImf6669FilpicjSODi1OUfz9suUm582ZmNS9mM-Ucl2RjisWWOFMuOD8tu4oeOjBGCdF2CoBz88UsbmW0W6bVRs-uTLAPzeHwS2kH_oHpvrTDksoaXbtb2pPm9nvxNN1O70fBiHms6UDGyBC47mVwARFMx6t0qdogSQBJdFKB4Eig9TBAp7wWiN44RR31tdQ_Jusp4DYVS6nE8mfn_S27vth5b9uxwQD2vVOqASd9AzXTOM1F41BLxb3uwqBr4RnK03avoVJPSs1zHUFfjhUnTzhT5T8HZ-_3P4oxdMY:1tzXtT:DkszGDUh0wJYVqlsv1m8pUFCQT-n1sSzdb4VpxoqE2w', '2025-04-15 09:26:51.368105'),
('9pypaino2kqkky0dlyydrw759jiy3v8y', '.eJxVkM2OhCAQhN-F82gQkR-Pe9_b3kkjzciuohFMdjKZd180HnbCqevrqjT1JHvCLcKMpCfg5hDJjRjY82gOYIIrOnvXLAw_GA_gviHel3pYYt6CrY-V-qKp_lwcTh_X7lvACGksbuTWU8k9dHpQnjqOWivmsWPlaSoldKwRGhSn4B1r7cAapKKhRRJNp47QhCmFJRr8XcP2IH1L6T81xJBNDjOmDPNqSN_IVgqtS3ytaKNaqm7lE5Nx6GGfssGYQ36Y-Tid9E9yzft-9qA5SGmFqLjtXMWLp7IlprKgOkGdav1wHHWZ0rTfiymXEWO1biNX7Gzi4lfpXycnr9cf8_eBPA:1tbCxP:8PhibZTQGDOOFZ2kw2Hz5JK0YlGAKH2LO_voU0Cl13I', '2025-01-24 06:19:19.858697'),
('9tgoursh0l4745s36vv3utgrdk8yg5sc', '.eJxVUD1vwyAQ_S_MsYUxYPDYvVt3dJijprVxZLDaKMp_L0QeGt107-P07t3JkXCPsCIZCbg1RHIhBo48m0qY4ArOXjEL0zfGSrgviJ9bO20x78G2VdKebGrfN4fL26l9OTBDmosbufV04B6EnpSnjqPWinkUrIymwwCCdVKD4hS8Y72dWIdUdrRAshOqHk2YUtiiwd9r2G9k7Cn9h4YYsslhxZRhvRoydoNgkmsuRMs1U3q4lB8W49DDsWSDMYd8M2tNTsY7OffjeNagOQyDlbLhVriGF09jFe0aC0pI6lTvp5rpNKXl-Cym_gduqbnuM1fs2cNJn5V_zDtilZDH4w-BK4HE:1ubwBf:SM97PKRvydUMmYS3Vr-HQ3DB6QWFuKtGnqXRMEHgaFM', '2025-07-16 07:09:19.568390'),
('9u7lf30a9re4phnhvxidn8acvktu3s8y', '.eJxVjzFzhCAQhf8L9emILoiW16dLzyyynCSKNwJF5ub-e9CxSMp93763b19MY06zzpF27S0bGWe3v5rB6ZvCAewXhsdWT1tIuzf1sVJfNNYfm6Xlfu3-C5gxzsXtaBiEc43qhTMOEYauKVJbtEkQBxJohATeIIFS0wSdtIoj2sFI6qg_QiPF6LegffBJJ79STLg-NRt5Dx20XPChVhIU8Ftpu2hLDvOSNIXk049ej45sfLFrzvl8eADseyNlBUbYCoqnMqrhlUElZGNV5yZVrl-muORHMaUyUqie-wyqPV--eMCVCv88OXu_fwGsY3ST:1tzDZv:Dqvcj7PshGBU6ybhxJv45difkeWd3dIYp4T1Q7E2Ob4', '2025-04-14 11:45:19.881300'),
('a5cf5so80oahjdz1gyzhg91n06027shd', '.eJxVjMFuwyAQRP-Fc4UWAzb42Hu-AS3suqaJcWSIlKjqv8eWckgOc5n3Zv7ErfJWcGExCqQll3Th7Sy-RMBbm8NBQ6Yd6s8uYjpzOQD9YvlZZVpL23KUhyJftMrTSnz5frkfBzPWeV9DF5XznVHWsIY9fqLoLJByEdD2A07DRMk6B6Qtpt4YUhNYbT2zt_E4rVxrXkvg-zVvDzFqgLc2l9xCywvXhss1iFEN4FzXe2ekMQ58Z_-f-GxV4w:1re3xY:XoUm6RzfJ3zG5_H3RuZJUWJ_hhsUIDKYQAVkIGMo6Zo', '2024-02-25 02:14:44.848310'),
('aw8cz79wnhej4n12we6rocptgovsoocb', '.eJxVUD1vwyAQ_S_MsQUGA_bYvVt3dJijprVxZLDaKMp_L0QeGt1070t3706OhHuEFclIwK0hkgsxcOTZVMIEV_DuFbMwfWOshPuC-Lm10xbzHmxbJe3JpvZ9c7i8ndqXgBnSXNworKdKeOiHSXvqBA6D7jz2XZmBKgV9x-QAWlDwruN26hhSyWiBJOt1DU2YUtiiwd9r2G9k5JT-Q0MM2eSwYsqwXg0ZmSrRUnDNWyW05kxdyhOLcejhWLLBmEO-mbWeTsY7OffjePYwCFDKStkI27tGFE9jNWWNBd1L6jT3Uz3qNKXl-Cwm_gO31Fz3WejuWcRJn51_zDtilZDH4w_rfIHv:1uba3T:LjCtd5Qhtk8gsxytu-Jy7TVY5xvY3AkxmqBXNoHg5xM', '2025-07-15 07:31:23.811274'),
('cf3otb3e3u0i46irsd1r0ji8nr696e1v', '.eJxVT8tugzAQ_BefA7LxE46599a7tcbr4BZMhI2qKMq_10Qc2uPOa2eexMJeJrtn3Gz0ZCCMXP5iDsZvTAfhvyDd1nZcU9miaw9Je7K5_Vg9ztdT-y9ggjxVd8C-lyFQo2VwAUD0nFaoq9gokQmU4KQSjAIKY8ZRcOUNA_C9U8hRH6EZc45rsjHFYktcMBdY7pYMTEtplOg73VKuKRPyUuvO1mOAfS4WU4nlYZejJBme5Lz3_b24F6C1U6oRTvpGVE_jDGWNAyMV9YaH0dT3pynP-62a-A88cnPfJmG69-STTrBgpT-nDfGQkNfrF_HPdYA:1upQg3:0Ib3Y5tqo5IBuQg1zH5ygHwXTYa_wt9X2Qd3Syu8aQE', '2025-09-05 12:15:27.073224'),
('cvm269y88wdd0n8qzsxotfd1uwl0f3y4', '.eJxVUD1vwyAQ_S_MsQUYG_DYvVt3dJijprVxZLDaKMp_L0QeGt1070t3706OhHuEFclIwK0hkgsxcOTZVMIEV3D-ilmYvjFWwn1B_NzaaYt5D7atkvZkU_u-OVzeTu1LwAxpLm4U1lMpPPR6Up46gVor7rHnZTSVEnrOBg1KUPCOd3biDOnAaIEG1qsamjClsEWDv9ew38jYUfoPDTFkk8OKKcN6NWRkskQrLoVoBWNSC34pTyzGoYdjyQZjDvlm1no6Ge_k3I_j2YMWIKUdhkbY3jWieBqrKGssqH6gTnV-qkedprQcn8XU_cAtNdd9Foo_izjps_OPeUesEvJ4_AHmZIHm:1ubepc:pr756LtY0On2hGSzliDHF76k2PtvDLzXcxjSPyP1tXA', '2025-07-15 12:37:24.438308'),
('cwob2b5keeeyvcko4rval6tzs9fltbbv', '.eJxVkEFvgzAMhf_KlHNBCWBCOO6-23aOHOK0aSEgEqZ2Vf_7oELaevDBft-znn1nS6Q54ECsZWgHH7qe5gs7MI1LOulN1d6uYvk6M9hdKGyCPWM4jnk3hjR7k29Ivqsx_xgt9e87-7LghPG0unlhRKOKSkBFJV9LOWsa4FY0hiPUEp10toOm4bYE7OqqssJxKEERKTDb0kgx-jFouk5-vrG25Pzf1AefdPIDxYTDpFkrJFdcQQ1FXldFU0g4rEf02pLDpU-aQvLppoctOmvvbO-X5fkHodYkBboMCEVWoYXMCJKZFIWUwtUchFxD7abYL8fVlMaEfbYcMVjMfipD39fp_Eft___cqLevJ8Uej19_eIe6:1rfBqv:VBpOU2OZD-Wq2aml8bEFSkRCARbsd6WRC_GFhIw-o6I', '2024-02-28 04:52:33.408194'),
('d1w23gh5b4iktsi4f8w7t60ukkit8dt3', '.eJxVjMFuwyAQRP-Fc4UWw9rgY-_5BrTAuqaJcWSIlKjqv8eWckg0msu8mfkTt8pboYXFKCgtucQLb2fxJTzd2uwP6nPaof7MAsUzlwOkXyo_q4xraVsO8qjIF63ytCa-fL-6Hwcz1XlfQxeUdZ1RaFjDbjelYBGSsgEI-4GmYUoRrYWkkWJvTFIToEbH7DAcp5VrzWvxfL_m7SFGDfCW5pKbb3nh2mi5ejGqAZyyepc02NtO2_8n-DVV4g:1rfYnG:4C7hd1itwiR2ww169xRND6KhIy1Kpu3uMxe43BI660I', '2024-02-29 05:22:18.462910'),
('dbxg3i1jek6at9bigjc2eoqbvpaw6a45', '.eJxVkEFvhCAQhf8L59UAgqDH3nvrnQwyrLSKRjDpZrP_vWg8dMNp3jfvZXhPsifcIsxIegJuDpHciIE9j-YAJrii83fNwvCD8QDuG-J9qYcl5i3Y-lipL5rqz8Xh9HHtvgWMkMbiRmE9VcKD7AbtqRPYdZp7lLy8jioFkrO2Ay0oeMcbO3CGtGW0SC2T-ghNmFJYosHfNWwP0jeU_lNDDNnkMGPKMK-G9EwJwZWWVNRMS1nyb-UTk3HoYZ-ywZhDfpj5OJ30T3LN-3720AlQyrZtJax0lSieymrKKgtattTpxg_HUZcpTfu9mHIZMVbrNgrNzyYufpX-dXLyev0B6h6BKw:1u2oWG:G7ZCOLzTiAscCpgK9yGIzNDs5QKSPHzH0KBSq7cBDNg', '2025-04-10 09:53:24.205771'),
('dmm5xelu7o0jpwba9re4pqdfnvsa1ewy', '.eJxVjLGOwyAQRP-F-oSW4MXgMn2-AS2wPpPEODJEShTl38-WUlyKaea9mZe4V14LzSwGQWnOJV55vYgf4eneJr9Tn9MG9XcXKF647CCdqfwuMi6lrTnIXZEfWuVpSXw9ftyvg4nqtK3hEJR1h05hxxq2uDEFi5CUDUBoehr7MUW0FpJGiqbrkhoBNTpmh2E_rVxrXornxy2vTzFogH9tLrn5lmeujeabF4PqFYAGpY10aIzp33-hflWb:1rj6xF:O5xb-nHWXTPfKDp4Ot7noItqE-PnZHJO2SVYj4Ye5U0', '2024-03-10 00:27:17.069931'),
('e61nyt9bs9tqdar25c7o58361zqk1141', '.eJxVjDkOwyAUBe9CHSEwi8Fl-pwBfeATkwUig6sod48tuUjamffmTRysfXZrw8XlSCbCyemXeQh3LLuINyjXSkMtfcme7hN62EYvNeLjfGz_AjO0eXsntFalxMyokk8A0gq2oWFjQSGXqMArLTkDlMaEIIWOhgNE6zUKHPdow9ZyLS6X3F3PT2wdni9HJj4KPQjD1UiZZFJY8_kCpw5HBA:1tV4rF:TxRJcv3iVoQlP5QCrrPLe2beBU1qaYI2EMhoXj1IXr0', '2025-01-21 08:22:37.045453'),
('evpu3vmbafvhn5272d6cfw33dyagdbyf', '.eJxVj72OwyAQhN-F-mxB-DGkTH_d9WgxS0zOxpGB4hTl3Q9bblLufDOzmhexGXOOa7IxxWJLXDAXWJ6WXNkguDDGUNNLaiil_ItYqGWyNeNmoydXwsiH5mD8xbQD_4B0X_txTWWLrt8t_Ulz_716nG-n96Nggjy1dEBjZAhUDzK4ACAMp026NG2UyARKcFIJRgGF1uMouPKaAXjjFHIcWql_zNZjgDoXi6nE8meX_S25vsh513psMAKGwSnVCSd9J1qmc5qyzoGWinrNw6hb4RnKc723UGknpu65TUJfjhUnT7Bg4z8HJ-_3P4uxdMc:1tzXyH:9sp8ivZQQv6YxN3IxXq_nEVs_oaAEnOxsZPlBzZ47ow', '2025-04-15 09:31:49.533889'),
('evq263uaiujzhnoreqwozetinceyy6bq', '.eJxVULtuhDAQ_BfXBzLgJ2X6dOmtNV4HJ2BO2Cg5ne7fY58octpq57GanTs5Eu4RViQjAbeGSC7EwJFnUwkTXMH7V8zC9I2xEu4L4ufWTlvMe7BtlbQnm9r3zeHydmpfDsyQ5uJGZj2VzAPXk_LUMdRa9R55X0ZTKYH3ndCgGAXv-sFOfYdUdLRAouOqHk2YUtiiwd9r2G9kHCj9h4YYsslhxZRhvRoydpILxrjUvBVKaybkpTyxGIcejiUbjDnkm1lrdDLeybkfx7MHzUBKK0TDLHcNK57GKto1FhQX1KnBTzXUaUrL8VlMww_cUnPdZ6b6ZxEnfXb-Me-IVUIejz_2-4ID:1urrmu:LQVMx8-eiPwf6BmkbAjKPZDPnLUbl7SgFP8DiksQnTg', '2025-08-29 05:41:36.028719'),
('fsv02jixe97di85j4h61fmnnqeiymaf2', '.eJxVkEFvhCAQhf8L59WAAqLH3nvrnQwyrLSKRjDpZrP_vWg4dI_zvXkvM-9Jjoh7gAXJQBYIdiU3ouFIkz4F7W3m7J0ZGH8wnIL9hnBf63ENafemPlfqosb6c7U4f5Tdt4AJ4pTdDvteOEdVJ5xxALxvaUZNZqNAxlGAEZIzCsiVGkfeSqsYgO2NxBa7MzRijH4NGn83vz_I0FL6j_rgk05-wZhg2TQZWMc5U0zKthaSsq5Rt_zErC06OOakMSSfHno5TyfDk5T5OK4eeg5dZ6SsuBG24tlTGUVZZUDlNKtaN6p8VDHF-bhnU8ojhmrbJ66aq4mil9K_Lp28Xn9YOYLC:1u2PKJ:ZzeI0iAtlnJhQwoYUSKb-v2R_5LZXNN7k_y8Lt6v7t4', '2025-04-09 06:59:23.747499'),
('fzdg2x7kqrrznmrw39zjjvke4fesspl1', '.eJxVUD1vwyAQ_S_MsQU2YPDYvVt3dJijprVxZLDaKMp_L0QeGt107-P07t3JkXCPsCIZCbg1RHIhBo48m0qY4ArevWIWpm-MlXBfED-3dtpi3oNtq6Q92dS-bw6Xt1P7cmCGNBc3cuvpwD0IPSlPHUetVedRdGU0HQYQHZMaFKfgXdfbqWNIJaMFkkyoejRhSmGLBn-vYb-Rsaf0HxpiyCaHFVOG9WrIyAbBNRW0162UumdcXsoTi3Ho4ViywZhDvpm1RifjnZz7cTx70ByGwUrZcCtcw4unsYqyxoISkjrV-6mGOk1pOT6Lqf-BW2qu-8xV9yzipM_OP-YdsUrI4_EH6TiB6w:1ulOxz:7irj8N4AcbxgHzDjwNVbgtnU25ab9gkilfN64XfSQ58', '2025-08-11 09:42:19.680864'),
('gr6em3jo4w549jh3qf7cmlfp4ezxuexm', '.eJxVUD1vwyAQ_S_MsQUYDPbYvVt3dJijprVxZLDaKMp_L0QeGt1070t3706OhHuEFclIwK0hkgsxcOTZVMIEV3D-ilmYvjFWwn1B_NzaaYt5D7atkvZkU_u-OVzeTu1LwAxpLm4U1lMlPMhh0p46gcOguUfJywxUKZCc9QNoQcE73tmJM6Q9owXqmdQ1NGFKYYsGf69hv5Gxo_QfGmLIJocVU4b1asjIlOx6zbuOtSVCqEt5YTEOPRxLNhhzyDez1sPJeCfnfhzPFgYBStm-b4SVrhHF01hNWWNBy5463fmpnnSa0nJ8FlP3A7fUXPdZaP6s4aTPxj_mHbFKyOPxBwfOgX4:1ugGsu:DaVusOwmofYKWbSC33JKZiFoyCGj30nVwqBnUjGQ-Pc', '2025-07-28 06:03:52.175342'),
('gtyiu5w4j6ydu4wwk4aywh5umcqflnxj', '.eJxVkL1uwzAMhN9Fc2xIsv7ssXu37gJlUbFaWw4sGWgQ5N0rBx4acOJ9PIK8B9kzbgkWJAMBv8RELsTCXiZ7ABt91fm75mD8wXQA_w3purbjmsoWXXuMtCfN7efqcf44Z98WTJCn6kbhAtUigOxHE6gX2PeGB5S8Vk-1BsmZ6sEICsHzzo2cIVWMVkkxaY6lGXOOa7L4e4vbnQwdpf_UmGKxJS6YCyw3SwamRceUoJS3tNdSCn2pT8zWY4B9LhZTieVul-N0MjzI2e_7K4degNZOqUY46RtRPY0zlDUOjFTUmy6Mx1GnKc_7tZpKbTE1t20Shr-SOPkZ-teLk-fzD-dmgSc:1ty8aQ:nu2jS8UbPCEg5prW5uZ2jeGBaYEpVmRcyeXY7KvfQT0', '2025-03-28 12:18:22.105803'),
('h1ecfqlxf8sm1v588w5gqhonirjzg2mc', '.eJxVTz1vwyAQ_S_MsQUYG_CYvVt3dJgjprVxZEBVFOW_F0ceWt109z7uvScxUPJsSsLdBEdGwsnl783C9I3xANwXxNvWTlvMe7DtQWlPNLUfm8PlenL_GcyQ5qpGYT2VwkOvJ-WpE6i14h57XkdTKaHnbNCgBAXveGcnzpAOjNbTwHp1mCZMKWzRhBiyyWHFlGG9GzIyKWRHmVC6ZVIpyi817WIceihLNhhzyA-zHhnJ-CTnXsq7sBYgpR2GRtjeNaJqGqsoayyofqBOdX46vp-itJRbFXU_8EjNfZ-F4u_GJxxhxQp_zjviQSGv1y9KqXO8:1uFUw5:jLf10SLW-QUOpqlKkx2vAH6pytw-eHSTKQlGGXLrClE', '2025-05-29 09:31:29.198009'),
('h9doyd3r2k69ba2ec4o04k2rc8rfjhg2', '.eJxVT8tugzAQ_BefA8L4wcIx9956t9Z4HdyCibBRFUX595qIQ3vcee3Mkxnc82T2RJsJjg2Ms8tfzOL4TfEg3BfG21qPa8xbsPUhqU821R-ro_l6av8FTJim4vbU98r7BjrlrUeUvWgK1BZsVMQlKbRKS94gSYBxlEI74Iiut5oEdUdoopTCGk2IIZscFkoZl7thA--UkC1I6GtQoEHoS6k7G0ce9zkbijnkh1mOkmx4svPe9_fiXmLXWa0raZWrZPFUFhpeWQSlGwfCj1Den6Y077diEj_4SNV9myS078knHXGhQn9OG9EhYa_XL_19dZU:1ufCqf:91Rg4xW2tL1mTTFL1V2d6Uc6fVqQPYgKrnDVmtQ0feY', '2025-08-08 07:28:09.902542'),
('hkt5hg3o3leerdvq9j6l09nas7f56lzb', '.eJxVjLGOwyAQRP-FOkKLYWNweX2-AS2wjrnEODJEulOUf48tpUiKaea9mYe4V14LzSwGQWnOJV55vYiD8HRvk9-pz2mD-rsLFC9cdpB-qZwXGZfS1hzkrsg3rfK0JL7-vN2vg4nqtK2hC8q6zig0rGGLG1OwCEnZAITHnsZ-TBGthaSR4tGYpEZAjY7ZYdhPK9eal-L575bXfzFogI82l9x8yzPXRvPNi0H14ECBMloiWmewe74A9z1Vzg:1repbj:77WTs1wl_RQUwSoyfRZ_nsIlKOsBNc31yGAh6aMnWbw', '2024-02-27 05:07:23.574149'),
('hmykpr95ugc8lsxqmqyhcam45w27eepr', '.eJxVT8tuwyAQ_BfOsQXhnWPuvfWOFrPEtDaODFYVRfn34siH9rjz2pkncbDV0W0FV5cCuRBGTn8xD8M35p0IX5BvSz8sua7J97ukP9jSfywBp-uh_RcwQhmbO6K1MkZqtIw-AgjLaYPODRskMoESvFSCUUBhzDAIroJhAMF6hRz1HlqwlLRkl3KqrqYZS4X57siFaams0drQXklFKZenVndyASNsU3WYa6oPN-8lyeVJjnvb3outAK29Up3wMnSieTpvKOs8mBYWDI-Dae8PU5m2WzPxH3iU7r6Owpzfkw86w4yN_hxXxF1CXq9f9yl1iQ:1uu8mb:EAsS6HyJB4fVmKAPvNRNnktZGGFfpcPtGtXa1rMs7-k', '2025-09-18 12:09:41.156347'),
('i13n702hgcmmw0lw444goemsy8yqmiig', '.eJxVj0FuxCAMRe_CehIBgQCznG3VMyATzIQmIdUAi2o0dy9RI7WVV_bz9_9-Egu1zLZmfNjoyZVwcvk7czAtmA7gPyDd937aU3lE1x8r_Ulz_757XG_n7r8DM-S5qVG4QJUIIM2kA_UCjdE8oOStDFUKJGejAS0oBM8HN3GGdGS0jUYm9XE0Y85xTzamWGyJG-YC26clV6a40MNgjOgF44obeWlxV-sxQF2LxVRi-bLbEZJcn-Tsa_35uBkpP-nOSeU6MeqhMxpFx9G1NIYO4-Sa_SnKa7030YIOOtxK5jwuvzTBho2-NUper2_a4XDv:1sjE78:_5Ot1ou_tcUZOLq2Bs5Zkig1hRMAZBOrE43OHvxlOg0', '2024-09-11 08:33:14.538077'),
('i60st6j744cfoc3xzih53vvflxr4hrud', '.eJxVT7tuxCAQ_BfqswWY55Xp06VHi1liEhufDFZ0Ot2_B59cJNpqdx478yAO9jq5veDmUiBXwsnl783D-I35AMIX5M-1H9dct-T7g9KfaOnf14Dz28n9ZzBBmZoahY9UiwjSjibSINBawyNK3sZSrUFypiwYQSEGPviRM6SK0XZSTJrDtGApac0u5VRdTQuWCsvNkSvTwshBMyV6O0ir1XBpcWcXMMI-V4e5pnp3yxGSXB_k3Pf91dgK0Nor1QkvQyeapvOGss6DkYoGM8TxeH-Kyrx_NtHwA_fS3bZJGP6qfMIZFmzwx7QhHhTyfP4CtCRz_g:1uKgOK:5n0W8AAp7sVSqCaduHzySLCWz_0vT02sbyrwCMzQYO4', '2025-06-12 16:46:04.978212'),
('i83k1gmnn7a2rdgyszlsdk66tfqh75yq', '.eJxVkM1uwyAQhN-Fc2wB4dfH3nvrHS1mHdPa2DJYahTl3YsjHxpx2vl2Rss8yJ5xSzAj6QiEOSZyIQ72MroDuBiqzt81D_0PpgOEb0i3pe2XVLbo22OlPWluP5eA08e5-xYwQh6rG4UfqBYDSNubgQaB1ho-oOT1Wao1SM6UBSMoDIFffc8ZUsVolRST5gjNmHNcksPfNW530l0p_afGFIsrccZcYF4d6Zjmxmpa81umpGVaXeonJhdwgH0qDlOJ5e7m43TSPcg57_urBytAa69UI7wMjaiexhvKGg9GKhrMdeiPo05TnvZbNZU6YmrWbRSGv5o4-Vn614uT5_MP8NiBNw:1t0aDN:71I_UCgjx3hhfqS7CQPfR-FhJbAO1b8yTTttmsLIDh4', '2024-10-15 05:40:25.217677'),
('iqq5to8n7l6ql0nwg6jb1y2hlqk3rfnz', '.eJxVkEFvhCAQhf8L59WAAqLH3nvrnQwyrLSKRjDpZrP_vWg4dI_zvfcmM-9Jjoh7gAXJQBYIdiU3ouFIkz4F7W3m7J0ZGH8wnIL9hnBf63ENafemPi11UWP9uVqcP4r3bcEEccpph30vnKOqE844AN63NKMms1Eg4yjACMkZBeRKjSNvpVUMwPZGYovduTRijH4NGn83vz_I0FL6j_rgk05-wZhg2TQZWMfbjismWS2FVA1Vt_zErC06OOakMSSfHno5TyfDk5T5OK4eeg5dZ6SsuBG24jlTGUVZZUAJSa1q3ajyUSUU5-OeQymPGKptn7hqriaKXkr_unTyev0BXEOCyQ:1u0aYL:BTV9rlLCYzVxXr23bNAG8_n21JpAcimne8mtHmLZU6k', '2025-04-04 06:34:21.779684'),
('jbaarjawmvlwlz8brs9wr1twxwrxc05y', '.eJxVjMFuwyAQRP-Fc4UWw9rgY-_5BrTAuqaJcWSIlKjqv8eWckgOc5n3Zv7ErfJWaGExCkpLLvHC21l8CU-3NvuD-px2qD-7QPHM5QDpl8rPKuNa2paDPBT5olWe1sSX75f7cTBTnfc1dEFZ1xmFhjXscVMKFiEpG4CwH2gaphTRWkgaKfbGJDUBanTMDsNxWrnWvBbP92veHmLUAG9tLrn5lheujZarF6MawIFGNE6i0zD03f8T9-ZV2Q:1rewDV:deyAk8_I70vB_Fos3QgKsIlVY57Dofyog1iyxd6q3MM', '2024-02-27 12:10:49.641391'),
('jgm12b8cc3qrtev3lohnsqtllahowq0a', '.eJxVjMFuwyAQRP-Fc4UWwxrwsfd8A1pgXdPEODJEalX132tLOTSHucx7Mz_i0XivtLKYBOW11HTj_SreRKBHX8JJQ8kH1K9dpHTleoL8SfVjk2mrfS9Rnop80iYvW-bb-9N9OVioLccahqicH4xCwxqO-DlHh5CVi0A4WprtnBM6B1kjpdGYrGZAjZ7ZYzxPG7dWthr46172bzFpgH9tqaWHXlZundZ7EJOy4L2x4-gkWotqsL9_-LZV6Q:1rilV7:NIXriV-cSnTZcVDCdwwpgFkRyln0mI9xBBN0lqo6OcQ', '2024-03-09 01:32:49.272872'),
('k4z7vx57s7uvptp0a0pl0izg6vte1vhx', '.eJxVUD1vxCAM_S_MlwgSIJCxe7fuyATT0CbkFIja0-n-e-GUoWdPfh-W_e7kSLhHWJGMBNwaIrkQA0eeTSVMcAXvXjEL0zfGSrgviJ9bO20x78G2VdKebGrfN4fL26l9WTBDmosbufV04B6EnpSnjqPWqvMoutKaDgOIjkkNilPwruvt1DGkktECSSZUXZowpbBFg7_XsN_I2FP6Dw0xZJPDiinDejVkZIPoS2mq214NQjJ5KU8sxqGHY8kGYw75ZtZ6Ohnv5JyP45mD5jAMVsqGW-EaXjyNVZQ1FpSQ1KneT_Wo05SW47OY-h-4pea6z1x1zyBO-sz8Y94Rq4Q8Hn_ps4Hs:1ueoFI:kwLHVwNiTUx4mAZQl-xxDbiFmLJe_2xVnZmiOftaYvg', '2025-07-24 05:16:56.206406'),
('kcycryz4792rwvkzx15o7gduct0d267m', '.eJxVj72ShCAQhN-F-LRAfkTDzS-7nBpkWNlT3BIIrrb23Q8tkw2nv-6emRcxCVMKWzQhhmxyWDFlWJ-GjKwXXCnBNW8HzSnrxBcxUPJsSsLdBEdGwsiHZmH6xXgA94B439ppi3kPtj0s7UVT-705XG6X96NghjTXtMdhkN5T3UtvPYAYOK1SV7VJIhMowUolGAUUWk9TPdRpBuAGq5BjX0vdYzEOPZQlG4w55D-zHmvJ-CLXXMr5wyCg761SjbDSNaJmGqspayxoqajT3E-6Fl6htJR7DeU6Ymye-yx0d35x8QgrVv5zcvJ-_wOLeHTH:1u0El6:N0x1tudcTq7jEPCKwrWpYGkzJ_NSTSJoIcVvwHj9hUg', '2025-04-17 07:13:04.001597'),
('ke07vu4l8w8tcn3x873inr0dab6xb2w6', '.eJxVUD1vwyAQ_S_MsQUYDHjs3q07OsxR09o4MlhtFOW_10QeGt107-P07t3JnnFLsCAZCPglJnIhFvYy2UrY6A-cv2IOxm9MlfBfkD7XdlxT2aJrq6Q92dy-rx7nt1P7cmCCPB1uFC5QJQJIM-pAvUBjNA8o-TGGKgWSs96AFhSC550bOUPaM3pAPZO6Hs2Yc1yTxd9r3G5k6Cj9h8YUiy1xwVxguVoyMCW5UMII2XbMMC7F5Xhith4D7HOxmEosN7vU6GS4k3Pf92cPRoBSru8b4aRvxOFpnKascaBlT73uwlhDnaY875-HqfuBW26u2yQ0fxZx0mfnH9OGWCXk8fgD5niB5g:1ubCmv:du3IkQymWsTTRBApUBCQUykIDcopFhSX-Glt9x7_WeU', '2025-07-14 06:40:45.340669'),
('l3b3j5cdrkw1xuacot5p74snbvlrkkpw', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE3MzYyMzc0MjYuNjA1MDQ4N30:1tV4fS:LzI1AUZ03XMoseDC9wAiifeox3fRaS5vzA_wO_44jEs', '2025-01-21 08:10:26.619356'),
('lwqhuxhdagmffhfo38w57lhqfxughg80', '.eJxVUDtvgzAQ_i-eAzLGT8bu3bpbZ3wubsFE2KiNovz3moih0U33vXT33cmecUuwIBkI-CUmciEW9jLZg7DRV5y9Yg7Gb0wH4b8gfa7tuKayRdcekvZkc_u-epzfTu1LwAR5qm7kLlDFAwgz6kA9R2M0CyhYHUOVAsE6aUBzCsGz3o2sQyo7WiHZCX2EZsw5rsni7zVuNzL0lP5DY4rFlrhgLrBcLRk6VSN7o7hqRSeZUvJSn5itxwD7XCymEsvNLsfpZLiTc9_3Zw-Gg1JOyoY74RtePY3TtGscaCGp130Yj6NOU573z2rqf-CWm-s2cc2eRZz02fnHtCEeEvJ4_AHqPoHt:1uZnaV:5lN4JcwYbsBsIRonGwXi6NGIXv52Y9lJFNrm2R6aiO4', '2025-07-10 09:34:07.525300'),
('m8fbpkcuq3odcmysqw5ry6domdd60m5u', '.eJxVULtuxCAQ_Bfqs4Ux5uEyfbr0aDFLTGLjk8FKTqf798DJRU5b7TxWs3MnR8I9wopkJODWEMmFGDjybCphgis4e8UsTN8YK-G-IH5u7bTFvAfbVkl7sql93xwub6f25cAMaS5u5NZTyT0MelKeOo5aK-ZxYGU0lRIG1gkNilPwjvV2Yh1S0dECiW5Q9WjClMIWDf5ew34jY0_pPzTEkE0OK6YM69WQsZMD47oXUrWyV1IzfilPLMahh2PJBmMO-WbWGp2Md3Lux_HsQXOQ0grRcDu4hhdPYxXtGgtqENSp3k811GlKy_FZTP0P3FJz3Weu2LOIkz47_5h3xCohj8cf8UyB-Q:1ubHf4:oDatBbLa9kJ3STE97bhnZzOIe9mQoIoVC5zlD1CcLMU', '2025-07-14 11:52:58.910290'),
('n8a44elqo51cf38b4nps42i8wvys6j47', '.eJxVTz1vwyAQ_S_MsQUGDPaYvVt3dJgjprVxZEBVFOW_F0ce2vHe1733JAZKnk1JuJvgyEgYufzFLEzfGA_CfUG8be20xbwH2x6S9mRT-7E5XK6n9l_ADGmubo_DIL2nWklvPYAYOK1QV7FJIhMowcpeMAootJ4mwXunGYAbbI8c1RGaMKWwRRNiyCaHFVOG9W7IyJRQgnKpaNsxJjrJL7XuYhx6KEs2GHPID7MeJcn4JOddynvxIEAp2_eNsNI1onoaqylrLGjZU6e5n3R9f5rSUm7VxH_gkZr7PgvdvSefdIQVK_0574iHhLxev-cxdW4:1uFvUY:J18Q0IfJYS5ot8OkNN2wZ8pIUsnS_CMihNCQINrq6B8', '2025-05-30 13:52:50.223432'),
('nv2yw3ptkns008tmghabsolmufy4lw35', '.eJxVUD1vwyAQ_S_MsQUYDPbYvVt3dJijprVxZLDaKMp_L0QeGt107-P07t3JkXCPsCIZCbg1RHIhBo48m0qY4ArOXzEL0zfGSrgviJ9bO20x78G2VdKebGrfN4fL26l9OTBDmosbhfVUCQ9ymLSnTuAwaO5R8jIDVQokZ_0AWlDwjnd24gxpz2iBeiZ1PZowpbBFg7_XsN_I2FH6Dw0xZJPDiinDejVkZEpKSTlnstWKdmxgl_LEYhx6OJZsMOaQb2at0cl4J-d-HM8eBgFK2b5vhJWuEcXTWE1ZY0HLnjrd-amGOk1pOT6LqfuBW2qu-yw0fxZx0mfnH_OOWCXk8fgD3_WB2w:1unuJr:8GTP1EM7PVSJImqUVYP0cQjAtN1ilG8ZDA_nEH0co7I', '2025-08-18 07:35:15.922454'),
('nykbw0km31msvrix322k52k7t9evri4e', '.eJxVUD1vwyAQ_S_MsQUYMHjs3q07OsxR09o4MlhtFOW_10QeGt107-P07t3JnnFLsCAZCPglJnIhFvYy2UrY6A-cv2IOxm9MlfBfkD7XdlxT2aJrq6Q92dy-rx7nt1P7cmCCPB1uFC7QXgSQZtSBeoHGaB5Q8mMM7XuQnCkDWlAInndu5AypYvSAFJO6Hs2Yc1yTxd9r3G5k6Cj9h8YUiy1xwVxguVoysF4qo3pDu9ZI1nGqLscTs_UYYJ-LxVRiudmlRifDnZz7vj97MAL63inVCCd9Iw5P4zRljQMtFfW6C2MNdZryvH8epu4Hbrm5bpPQ_FnESZ-df0wbYpWQx-MP6jmB7A:1uu3c0:pVb3TrZaKfRj4a955Kb_Oy6URiA4BLD6AxDIcESkbdI', '2025-09-04 06:43:24.443541'),
('nzpksokz2yuybsiwey4oqsl2bnivhznc', '.eJxVjEEOwiAURO_C2pAPtIV26d4zkA_8WtRSUzDRGO9uSbrQzO69mXmzR6Y14UxsYBjmmNiBWXyUyVZhY9i4_GcO_ZVSFeGC6bxwv6SyRsdrhe8289MS6Hbcu38HE-ZpW5tOO01IDtA1vWgVhB6pA40K-qCNH0cyqjUaghTCuaYhDyA7AaNs0GM9zZRzXJKl5z2uLzYogB8aUyy2xJlywflu2SC0EGCkgpb3sqv5fAEi01Qv:1rnWfh:DZa0a6VIcCqGGJ1S7hWfgQrODTOm_nHiV6l6nrL998I', '2024-03-22 04:43:25.951395'),
('p2istqu3c9m3p8la7b27qwpiyk6j2aqn', '.eJxVUD1vwyAQ_S_MsQUYMPbYvVt3dJijprVxZLDaKMp_L0QeGt1074vj3cmRcI-wIhkJuDVEciEGjjybSpjgCs5fMQvTN8ZKuC-In1s7bTHvwbZV0p5sat83h8vbqX0JmCHNxY3CetoLD3KYtKdO4DBo7lHyMgPte5CcqQG0oOAd7-zEGVLFaIEUk7qGJkwpbNHg7zXsNzJ2lP5DQwzZ5LBiyrBeDRlZL5RkQnPdCilKhr6UTyzGoYdjyQZjDvlm1no6Ge_k3I_j2cMgoO-tUo2w0jWieBqrKWssaKmo052f6lGnKS3HZzF1P3BLzXWfy6vPIk767Pxj3hGrhDwef-rZge4:1uCCI0:-AOaL4yBpDuhCFyVem2RtRSa5gydBUNtqptOIx3r4hA', '2025-05-06 07:05:28.493855'),
('pbwjhe7m06kcvi3n408vasyh46tew22x', '.eJxVTz1vgzAQ_S-eA8L4bAxj9m7drTM-B7dgImxURVH-e03E0I73vu69JzO458nsiTYTHBsYZ5e_mMXxm-JBuC-Mt7Ue15i3YOtDUp9sqj9WR_P11P4LmDBNxe2p76X3je6ktx4RetEUqC3YKIkDSbRSAW-QQOtxBKGc5oiut4oEdUdoopTCGk2IIZscFkoZl7thA--kgFYByFpooaGVl1J3No487nM2FHPID7McJdnwZOe97-_FPWDXWaUqsNJVUDyV1Q2vLGqpGqeFH3V5f5rSvN-KSfzgI1X3bQLdviefdMSFCv05bUSHhL1ev_FsdYA:1ufCJh:QSLgZ24Qe7i5xskbveT5y9DglcVurcgK0oVXKttdw9s', '2025-08-08 06:54:05.438496'),
('plyiguujuxxkn8ddimlhgtjw4t4crwt8', '.eJxVkEFvhCAQhf8L59XgCgge995b72SQYaVVNIJpzWb_e3HDoXuc7703mXkPskfcAsxIejJDsAu5EA17GvUpaG8zb96ZgeEbwynYLwj3pR6WkDZv6tNSFzXWH4vF6Va8bwtGiGNOO1SKO0dlx51xAEy1NKNrZgPHhiEHwwVrKCCTchhYK6xsAKwyAlvszqURY_RL0Pi7-u0gfUvpP-qDTzr5GWOCedWkbzouVKeYEPVVciUou-QnJm3RwT4ljSH5dOj5PJ30D1LmfX_1oBh0nRGiYobbiuVMZSRtKgOSC2pl6waZjyqhOO33HGp_4IjVuo1MXl9FFLl0_jluiKeFPJ9_Y6mDkQ:1uu6cU:76VVmUI5ep-9BhYAQ3iopMDSrbgFtl1K2IY_F30N0fw', '2025-09-04 09:56:06.295780'),
('pmk0ztq2z3sg83g2xzndj66jjcjrjlo4', '.eJxVT8tuwyAQ_BfOsQWYl33Mvbfe0WKWmNbGkcGqoij_Xhz50GpPu_PYmSexsJfJ7hk3Gz0ZCCeXvzcH4zemA_BfkG5rO66pbNG1B6U90dx-rB7n68n9ZzBBnqoahQtUiwCyH02gXmDfGx5Q8jo91RokZ6oHIygEzzs3coZUMVpPiklzmGbMOa7JxhSLLXHBXGC5WzIwLXRHKWemNVoyo_Slxp2txwD7XCymEsvDLkdIMjzJue_7u3EvQGunVCOc9I2omsYZyhoHRirqTRfG4_0pyvN-q6LuBx65uW-TMPxd-YQTLFjhz2lDPCjk9foFrFdz8Q:1uFUbb:QuzHry57L7FwaicN5cIbpSymSAtmDycuFsPILX5fTg8', '2025-05-29 09:10:19.022343'),
('q0l09ppt6d7aodgla8amo82438in3edw', '.eJxVjMsOgjAQRf-la9NMefTB0r3f0EzbQapSCC2JxvjvQsJCk1mdc-e82ZppSTgS6xiGMSZ2YhbXMthd2Bg2Xv0zh_5OaRfhhuk6cT-lskTH9wk_bOaXKdDjfGz_AgPmYfvWUjlFSA7QNUa0NQSDJEFhDSYo7fuedN1qBaESwrmmIQ9QSQF91aDHPZop5zglS885Li_W1QA_NKZYbIkj5YLjbFknlBCwnTZcyy2qP1_OvlP5:1rnE93:ODWFbBHCFV0HkZ4WsMXrnmVzCg481gaDAGnjxpK0SSI', '2024-03-21 08:56:29.891596'),
('qa77oqpdu58ir8jcrn8ky0wj4yw68933', '.eJxVkL1uhDAQhN_F9YEM-Jcyfbr01hqvDydgEDZSTqd79xhEkSv3m5nV7jzJnnCLMCPpyQzRLeRGDOx5NIdggiu8eWcWhh-Mh-C-Id6Xelhi3oKtD0t9qan-XBxOH5f3bcEIaSxpj1pz76mS3FsPwHRHC2oLGzg2DDlYLlhDAZlSw8A64VQD4LQV2KE8liZMKSzR4O8atgfpO0r_0RBDNjnMmDLMqyF9I1nHNWda11KKlstb-WEyDj3sUzYYc8gPMx-Xk_5Jrnnfzxo0AymtEBWz3FWsZCqraFNZUFxQpzo_qHLTFUrTfi-hXEaM1bqNTLVnEZd-df516uT1-gP1UYKm:1tzwq3:WbZGYZtqzV1DYbyMfeYmKbDCJYAZRXosJYj5eGfyBtQ', '2025-04-02 12:09:59.809632'),
('qbno2tgwsdvx0g3yfyn6blr0tt07mlby', '.eJxVUD1vwyAQ_S_MsQUYMPbYvVt3dJijprVxZLDaKMp_L0QeGt107-P07t3JkXCPsCIZCbg1RHIhBo48m0qY4ArOXzEL0zfGSrgviJ9bO20x78G2VdKebGrfN4fL26l9OTBDmosbhfW0Fx7kMGlPncBh0Nyj5GUG2vcgOVMDaEHBO97ZiTOkitECKSZ1PZowpbBFg7_XsN_I2FH6Dw0xZJPDiinDejVkZL0UQjEleMvEwDshL-WJxTj0cCzZYMwh38xao5PxTs79OJ49DAL63irVCCtdI4qnsZqyxoKWijrd-amGOk1pOT6LqfuBW2qu-yw0fxZx0mfnH_OOWCXk8fgD43eB4Q:1ujXcQ:wQNCSOXtllE2_EiKzsvjhgHZfccdsTMdJzzRyUCcAi4', '2025-08-06 06:32:22.491919'),
('qmvpxblsdfwujgjivnhwd45d4dd4s436', '.eJxVj0FvwyAMhf_KxLmJgEKA3Dbtut12Rk4wLV1CqgLTtqr_faSKtE0--fl7z_aVWCj5aEvCiw2O9IST3V9tgPEd4zpwJ4iHpR2XmC9haFek3aapfVkcTk8b-y_gCOlY3SgGT5XwIM2oPXUCjdHco-S1DFUKJGedAS0oeMf3w8gZ0o7RKnVM6jU0YUphiTbEkG0OM6YM89mSnqm9FpwaZVrZSaEl39VzJ-vQQ5myxZhD_rLzeiTpr2TrS7l_zIymjoNvJAJrBDjZDAxVoxhXivmOSqbq-s2UpnKoprxkmJpygOig-RYDfnyeT79UhBkr9fz6-PB2Z8jt9gNKKXYv:1teEi3:a95rSoIs7f1otSE0JcEICT7HTGkxLC6uATUFVx5KrjQ', '2025-02-15 14:42:59.673346'),
('qtl2ecu6y7waue262qco7sh5da1emzfy', '.eJxVjMEOgyAQBf-Fc0MWUEGPvfcbyAJrpa1oBJM2Tf-9mnhorzPvzZutmZaEI7GOYRhjYidmcS2D3YWNYePynzn0d0q7CDdM14n7KZUlOr5P-GEzv0yBHudj-xcYMA_b2zTaaUJygK5qRa0gtEgNaFTQBm1835NRtdEQpBDOVRV5ANkI6GWFHvdoppzjlCw957i8WKcAfmhMsdgSR8oFx9myTmgBoJSsFddSGTCfL86iU_c:1rj7lV:P4lNR2UfX-5ApDb4P7GVjom0Yergqr-MOprm4p1Zjd8', '2024-03-10 01:19:13.745821'),
('r3igqwyoxi5i5bboutj8waaxqupr105q', '.eJxVUD1vwyAQ_S_MsYUBG_DYvVt3dJijprVxZLDaKMp_L0QeGt107-P07t3JkXCPsCIZCbg1RHIhBo48m0qY4ArOXjEL0zfGSrgviJ9bO20x78G2VdKebGrfN4fL26l9OTBDmosbhfVUCg-9npSnTqDWinnsWRlNpYSedYMGJSh4x7idWId06GiBhq5X9WjClMIWDf5ew34jI6f0HxpiyCaHFVOG9WrI2MmeSS44Y63UnDIpLuWJxTj0cCzZYMwh38xao5PxTs79OJ49aAFS2mFohO1dI4qnsYp2jQXVD9Qp7qca6jSl5fgsJv4Dt9Rc91ko9izipM_OP-YdsUrI4_EH42-B4Q:1ucIGQ:bnyg0FvPe6sAzcDL89CwbSoksU6c9OVw0L6tXcuCx2w', '2025-07-17 06:43:42.905066'),
('r4h3krd1onuqk8y3v4b1eygm150iizfb', '.eJxVkL1uwzAMhN9Fc2xIsn49du_WXaAsOlZry4ElAw2CvHvlwEMDTryPR5D3IHvGLcGCpCcQlpjIhTjYy-QO4GKoOn_XPAw_mA4QviFd13ZYU9mib4-R9qS5_VwDzh_n7NuCCfJU3Sj8SLUYQdrBjDQItNbwESWvZanWIDlTFoygMAbe-YEzpIrRKikmzbE0Y85xTQ5_b3G7k76j9J8aUyyuxAVzgeXmSM90p7jsjGStNVbT7lJ_mF3AEfa5OEwllrtbjstJ_yBnv--vGKwArb1SjfAyNKJ6Gm8oazwYqWgw3TgcN52mPO_Xaiq1xdTctkkY_gri5GfmXy9Ons8_gdCBAw:1tV8wO:ElcBpIs_QieISte2UiSc_9alU7-OXnSC3yFr-8s9fgw', '2025-01-07 12:49:12.002799'),
('r96yajd2z5xl8tp1tfs7qhh7q7ndisy9', '.eJxVUDtvwyAQ_i_MsQUYDHjs3q07OsxR09o4MlhtFOW_F0ceGt103-Me353sGbcEC5KBgF9iIhdiYS-TPQgbfcX5K-Zg_MZ0EP4L0ufajmsqW3TtIWlPNrfvq8f57dS-DJggT9WNwgWqRABpRh2oF2iM5gElr2WoUiA56w1oQSF43rmRM6Q9oxXqmdTH0Iw5xzVZ_L3G7UaGjtJ_aEyx2BIXzAWWqyUDU7LjkinVt1pIU_dc6hOz9Rhgn4vFVGK52eU4nQx3cvb7_szBCFDK9X0jnPSNqJ7GacoaB1r21OsujMdRpynP-2c1dT9wy811m4TmzyBO-sz8Y9oQDwl5PP4A62-B7w:1ueSsS:3lc67IgVnNgPx3KZlr2b1laJy5aTft6QMsN9opX7y_A', '2025-07-23 06:27:56.904850'),
('rg41ak8pg34jl5d7liecy8et4qswu1ev', '.eJxVj71yhDAMhN_F9cEYY_xDeX269B4Zy4cTMDfYLjI39-4xDEUyqlafdiW9iIGSZ1MS7iY4MhJGbn97FqZvjAdwXxAfWzttMe_BtsdIe9HUfmwOl_s1-y9ghjRXN3LrqeQeBj0pTx1HrRXzOLBamkoJA-uEBsUpeMd6O7EOqehobYluUEdowpTCFk2IIZscVkwZ1qchYyfPFKllqwWlvea3eu5iHHooSzYYc8g_Zj2OJOOLXLqU82PNQUorRMPt4BpePY1VtGssqEFQp3o_HesvU1rKo5pylRib5z5zxc6fLx5hxco_T07e71_UTXNE:1sl0sv:Zvhx_m0FGEIY3AElzjx2D5fmOg7NQ1jSZCOBv0MCwgk', '2024-09-16 06:49:57.989231'),
('s2uuy9qqj3au24gv62c5kcocuxojy7xu', '.eJxVjEFuwyAQRe_COkIwmHHiZfc9AxpgUtPGYAGuWlW9e2wpi2T73vv_T2yNa6aFxSR66XRr28r1O7VSxUk42vrsjsSluBf4yjyFL86HiJ-UP4oMJfeavDwS-bBNvpfIt7dH-3IwU5v3NQFch4FCtNaCUfrCRKjiiN4OoAhQo9We7W7AoN9b5tEHOBuFEYM_Thu3lkp2_LOm-ismo9QTTTl119PCrdOyOjHpUWtUYPEiBzSgzuP_HW73WB0:1rpi13:4rFnu-ewkWwUC7OuH15B5Xn7mFUZsCe3_GH6R22Gs6o', '2024-03-28 05:14:29.927226'),
('slxgsxll3thljh93ft0ka1s8wv32m1sa', '.eJxVj7FywyAQRP-F2tIIcyBw6T5deuYQh0UiIY9ARcbjfw_SqEjK23e7t_diFrcy2i3TaqNnN8bZ5a_mcPimtAP_hemxtMOSyhpdu6-0J83tx-Jpup-7_wJGzGN1BzJGhtDpXgYXEMGIrkrXqg2SOJBEJxXwDgm0HgYQymuO6I1TJKjfQzPlHJdkY4rFljhTLjg_LbvxHgQYEAJaro0yvbjUupP1FHCbiqVUYvmx816S3V7snLft-NgA9r1TqgEnfQPV0zjd8cahlqrzWoRB1_OnKU_bo5pKHSk1z3UEfT1-PnnCmSr_PDh7v38BFlp01A:1tzWWM:ES_2nB5toHesTY1c6q0eYTdY3RHIGMfLORdhzWs9Oh8', '2025-04-15 07:58:54.351754'),
('tgq3lltd7i2ccm04km142auc1wnkc9a3', '.eJxVULtuhDAQ_BfXB7KNn5Tp06W31ngJTsCcsFFyOt2_x5woctpq57GanTvZM24JFiQ9gbDERC7EwV4mdxAuhorzV8zD8I3pIMIXpM-1HdZUtujbQ9KebG7f14Dz26l9OTBBnqobhR-pFiNIO5iRBoHWGj6i5HUs1RokZ8qCERTGwDs_cIZUMVohxaQ5jmbMOa7J4e81bjfSd5T-Q2OKxZW4YC6wXB3pmZZcSyu0aoVhhilzqU_MLuAI-1wcphLLzS1HdNLfybnv-7MHK0Brr1QjvAyNqJ7GG8oaD0YqGkw3Dkeo05Tn_bOauh-45ea6TcLwZxEnfXb-MW2Ih4Q8Hn_vnIH2:1ucOo8:idVWmCurh4TvL5e4BJ3bI3pfa8Y8p5T9tPdVdz_Jj1M', '2025-07-17 13:42:56.496773'),
('tjiax40ekv2q8qpc0zvpvjilrf6de943', '.eJxVT8tuwyAQ_BfOsQUxzxxz7613tJglprVxZEBVFOXfiyMf2uPOa2eexEItk60ZNxs9uRBGTn8xB-M3pp3wX5Buaz-uqWzR9bukP9jcf6we5-uh_RcwQZ6aO6AxIgSqlQguAHAz0AadGzYKZBwFOCE5o4Bc63Hkg_SaAXjjJA6o9tCMOcc12ZhisSUumAssd0suTAmhFaWc9UJJo7g5tbqz9RigzsViKrE87LKXJJcnOe5a34sNB6WclB13wne8eTqnKescaCGp10MYdXt_mPJcb800_MAjd_dt4vr8nnzQCRZs9Oe0Ie4S8nr9AvebdYs:1upS0X:Azwz39QuEGfTl94jGOlbWzJR0SGgbZZtOjZCuHA41gA', '2025-09-05 13:40:41.896560'),
('tr8u1me8ggugkzmvprvzjahhfbr503w7', '.eJxVUDtvwyAQ_i_MsQUYDGTs3q07OsxR09o4MlhVFOW_FyIv0U33ve7xIEfGPcGK5ErArzGRC7FwlNk2wkZfcf6OOZh-MTXC_0D63vppS2WPrm-S_mRz_7l5XD5O7VvADHmubhQuUCUCSDPpQL1AYzQPKHktQ5UCydloQAsKwfPBTZwhHRmt0MikbqEZc45bsjHFYktcMRdYb5ZcmZJSGk2Z7M2gFWXiUtddrMcAx1IsphLL3a5tSXJ9kLM_jtfFRoBSbhw74aTvRPV0rmZ1DrQcqddDmNr405SX47uahj-45-62z0Lz18knfX73a94Rm4Q8n__Fr3pL:1uoJF2:L06dSE-uzy1DCjpbDe0RZpsck5qgkYBzWfaK-3yvyGE', '2025-09-02 10:06:56.162323'),
('trwn6gnr2rmih29yw38raw0rpqaowq7u', '.eJxVULtuxCAQ_Bfqs4Ux5uEyfbr0aDFLTGLjk8FKTqf798DJRU5b7TxWs3MnR8I9wopkJODWEMmFGDjybCphgis4e8UsTN8YK-G-IH5u7bTFvAfbVkl7sql93xwub6f25cAMaS5u5NZTyT0MelKeOo5aK-ZxYGU0lRIG1gkNilPwjvV2Yh1S0dECiW5Q9WjClMIWDf5ew34jY0_pPzTEkE0OK6YM69WQsZMD11Jq0beU6Z7zS_lhMQ49HEs2GHPIN7PW5GS8k3M_jmcNmoOUVoiG28E1vHgaq2jXWFCDoE71fqqZTlNajs9i6n_glprrPnPFnj2c9Fn5x7wjVgl5PP4AfZiBvQ:1ulhwB:YqQziEjal3OHHfalwCXBEI2VRIb_GIj7TIbeAB-D_XI', '2025-08-12 05:57:43.131666'),
('tvmlwg7l58juujdqn9022t7qt0smmnud', '.eJxVjMEOwiAQBf-FsyFAy1J69O43kAVWi1owhZ6M_26b9KDXN_PmzRyubXJrpcWlyEYG7PS7eQwPyjuId8y3wkPJbUme7wo_aOWXEul5Pty_wIR12t6o1LXvMUStteqEtIQIIhrwulcCFUjQ0pPeiOrAby6R8UENnYAIwe_RSrWmkl3KqbmWZqoN55djozRSgtCDNtwqsNZ8vu9_RYg:1rpis6:Cok58aDIo0c7svJJ2X_EggdvJ-vIHKGapGkDYeHyhB0', '2024-04-11 06:04:18.560417'),
('ut6ugv01r5fudeho5wg0l459vy9pesq0', '.eJxVjMEOwiAQBf-FsyELtAV69O43kAW2FrXUFEw0xn-3TXrQ68x782aPQkvGiVjPME4pswNz-Kij24RLceXyn3kMV8qbiBfM55mHOdcleb5N-G4LP82Rbsd9-xcYsYzr23Taa0LygL6xolUQLVIHGhXYqE0YBjKqNRqiFML7pqEAIDsBg2ww4BYtVEqas6PnPS0v1iuAH5pyqq6miUrF6e5YL7QAK6CVLVcWlOnU5wsi7FQx:1rmnz3:ff-AyHoR2KHkfcq_CXkYXcFW81yNY-ExDoRVNfazT5U', '2024-03-20 05:00:25.663604'),
('uvfa96myvbuycqois82hf4o5hbpe5dbj', '.eJxVkEFvhCAQhf8L59WAgILHvffWOxlkWGkVjWDazWb_e3HjoXuc7703mXkPsifcIsxIejJDdAu5EAN7Hs0hmOAKZ-_MwvCN8RDcF8TbUg9LzFuw9WGpTzXVH4vD6Xp63xaMkMaS9qi19J6qTnrrAYTmtKCmsEEiEyjBylYwCiiUGgbBW6cYgNO2RY7dsTRhSmGJBn_XsN1Jzyn9R0MM2eQwY8owr4b0rBMd11QIXmvaMCWbS3liMg497FM2GHPIdzMfp5P-Qc553189aAFdZ9u2Ela6SpRMZRVllQUlW-oU94MqR52hNO23EuI_cE_Vuo1CNa8iTvns_HPcEA8LeT7_AFUHg3g:1uFs4p:oL_SxJGBk0fQWCH6MAn3QcDWnpYvPCnmMQNNJY4Th4M', '2025-05-16 10:19:03.978012'),
('vo9173q6uwzp803nu2cxaizhc25oen5u', '.eJxVkL1uwzAMhN9Fc2xI0a89Zu_WXaAsKlZry4Elow2CvHvlwEMz8rs7grwH2TKuCWYkPZkh-YWciIWtjHYXbPSVs3fmYPjGtAv-C9J1aYcllTW6dre0h5rbj8XjdDm8bwtGyGNNB-w6GQI1WgYXAETHaUXnygaJTKAEJ5VgFFAYMwyCK28YgO-cQo56X5ox57gki7-3uN5Jzyn9R2OKxZY4Yy4w3yzpmRaaU62YaanhRp_NqT4xWY8BtqlYTCWWu53300n_IMe8ba8eOgFaO6Ua4aRvRM00zlDWODBSUW94GEw96gjlabvWEP-Be25u6yjM-VXEIR-df44r4m4hz-cfWx6Dgw:1uFWWw:yKIcy8_CBJUqdRQYJRobhJ0qJpFmwV7_4s78vlqO2Tk', '2025-05-15 11:18:38.095383'),
('vr0vgh9bb8xv7rr2ich5k6eghtxwlnxc', '.eJxVULtuxCAQ_Bfqs4Ux5uEyfbr0aDFLTGLjk8FKTqf798DJRU5b7TxWs3MnR8I9wopkJODWEMmFGDjybCphgis4e8UsTN8YK-G-IH5u7bTFvAfbVkl7sql93xwub6f25cAMaS5u5NZTyT0MelKeOo5aK-ZxYGU0lRIG1gkNilPwjvV2Yh1S0dECiW5Q9WjClMIWDf5ew34jY0_pPzTEkE0OK6YM69WQsZNcSMnowFuheyF7filPLMahh2PJBmMO-WbWGp2Md3Lux_HsQXOQ0grRcDu4hhdPYxXtGgtqENSp3k811GlKy_FZTP0P3FJz3Weu2LOIkz47_5h3xCohj8cf6vqB7g:1uDHCo:KLMN4SJs4yYZ1fezvFPPYA6HHz0Qu3js9he0JlbtQbA', '2025-05-09 06:32:34.955841'),
('vu3g2q9vtmzh3tnegku1li3jads2txx1', '.eJxVjDkOwyAURO9CHSHALMZl-pwBfeATkwUig6sod48tuUg03Xsz8yYO1j67teHiciQTEeT0yzyEO5ZdxBuUa6Whlr5kT_cKPWyjlxrxcT66fwcztHlbo_SJGZlA2TAmFiVaO4qESmyxzBhQgmsLo2SQohh8EByZ5mxDmqtxP23YWq7F5ZK76_mJrcPz5cjEjbBcGS0lNYORbJCfLztPRXc:1t1MtQ:zGGBfqPOzfLQHKVYd_DC0nGnMLRrVpEqMj8ourVXFUE', '2024-10-31 09:34:04.835273'),
('vxslw0pxst5bmzp0oho9mlasurs6id88', '.eJxVUD1vwyAQ_S_MsQUYMPbYvVt3dJijprVxZLDaKMp_L0QeGt107-P07t3JkXCPsCIZCbg1RHIhBo48m0qY4ArOXzEL0zfGSrgviJ9bO20x78G2VdKebGrfN4fL26l9OTBDmosbhfW0Fx7kMGlPncBh0Nyj5GUG2vcgOVMDaEHBO97ZiTOkitECKSZ1PZowpbBFg7_XsN_I2FH6Dw0xZJPDiinDejVkZL2UTAqhaaulYJ26lB8W49DDsWSDMYd8M2tNTsY7OffjeNYwCOh7q1QjrHSNKJ7GasoaC1oq6nTnp5rpNKXl-Cym7gduqbnus9D82cNJn5V_zDtilZDH4w911oGw:1umRrF:7GHtZwPknVlQPZVignB9FAyaDpbUPiEWI9ladZGvcss', '2025-08-14 06:59:41.455835'),
('wa1gdm4zr4a8z3g13rl9753aixfovcvb', '.eJxVkL1uwyAUhd-FObZwfMHgMXu37uhiLjGtjSOD1UZR3r048tCMfOdHl_NgW6I14kysZzNGt7ATM7jl0eyCCa7w5p1ZHL4p7oL7wnhd6mGJeQ223i31oab6Y3E0XQ7vW8GIaSxpT1oL77nqhLceEXTLCzoXNghqgARaIaHhSKDUMEArnWoQnbaSWur20kQphSUa-r2F9c76lvN_NMSQTQ4zpYzzzbC-6YRQoITUNWgNUsKpfGIyjjxuUzYUc8h3M--ns_7Bjve2vXbQgF1npazACldByVRW8aayWBq5U60fVDnqCKVpu5ZQ-4P3VN3WEdT5NcQhH5t_jivRbmHP5x9m54OX:1upMQD:g1X8pwbvfgnmCGtg-UBSwIbb006lLcACGwNPLGpZxDY', '2025-08-22 07:47:49.723280'),
('wrd4293flx3e1f2zy9wl2k3et13aqib2', '.eJxVT8tugzAQ_BefA8LgJ8fce-vdWtvr4BZMhI2qKMq_10Qc2uPOa2eexMBeJrNn3Ez0ZCSUXP5iFtw3poPwX5Bua-vWVLZo20PSnmxuP1aP8_XU_guYIE_VHVBrHkKnJA82ADA9dBXqK-Y4UoYcLBeMdoBMKefYILyiAF5bgQPKIzRjznFNJqZYTIkL5gLL3ZCRSiZ7OjCuWt1rqRS71Lqz8Rhgn4vBVGJ5mOUoScYnOe99fy_WDKS0QjTMct-w6mms6mhjQXHReTUEp-r705Tn_VZNww88cnPfJqb69-STTrBgpT-nDfGQkNfrF_nbdY8:1uF82F:soESJN9KWavIngck19_4Skf6g_5Xv4JkE3dm-svKBbs', '2025-05-28 09:04:19.106774'),
('wrr4yzkveyw6p7fhr1d60545str773i5', '.eJxVjktuxCAQRO_COkJ82hi8zH7OgBroGZPEYAEjJYpy99jRLDLbeq9K9c3unVrBjdjC6k4NR66lb1jwRo29MI_3sfpT8jkdzvScBYzvVE6Q3rDcKo-1jJYDPxX-oJ1faqKP14f7NLBiX4-2QanIXY1UIk4qmJgAtEwJVNIy2GsUB7DgwArQVtkZ9RScc2EOaET8G-3U-3He0-ee2xdbtBD_0lzy8CNv1Aduu2eLnKVwzgAIbu08gdA_vwxwWKQ:1rnAKm:9S38TsiZlitEHD_Sv1od9RsxCfYKjEFjYmvQAEZdQMg', '2024-03-21 04:52:20.903508'),
('xbd9y21kv69rhg0hgmnnnua3dx0yd9ia', '.eJxVTz1vwyAQ_S_MsQUYMHjM3q07OswR09o4MlhVFOW_F0ceWt109z7uvSexsJfJ7hk3Gz0ZCCeXvzcH4zemA_BfkG5rO66pbNG1B6U90dx-rB7n68n9ZzBBnqoahQu0FwGkGXWgXqAxmgeUvI6hfQ-SM2VACwrB886NnCFVjNaTYlIfphlzjmuyMcViS1wwF1julgysl0IoSZVoKTOUUX2pcWfrMcA-F4upxPKwyxGSDE9y7vv-bmwE9L1TqhFO-kZUTeM0ZY0DLRX1ugvj8f4U5Xm_VVH3A4_c3LdJaP6ufMIJFqzw57QhHhTyev0CpLZz4w:1ujYVc:D0NTu7SL3H-cFuZBhr0o8q3yj6z0P4-1SUnO9QzROeE', '2025-08-20 07:24:24.066549'),
('xnk1r6ayivwm6wwivquu8395cwje82ah', '.eJxVkL1uwzAMhN9Fc2zIsn49du_WXaAsKlZry4ElAw2CvHvlwEMDTryPR5D3IHvGLcGCZCDgl5jIhVjYy2QPYKOvOnvXHIw_mA7gvyFd13ZcU9mia4-R9qS5_Vw9zh_n7NuCCfJU3chdoIoHEGbUgXqOxmgWULBahioFgnXSgOYUgme9G1mHVHa0SrIT-liaMee4Jou_t7jdydBT-k-NKRZb4oK5wHKzZOgU5z3Xou9bKY0QSl_qE7P1GGCfi8VUYrnb5TidDA9y9vv-ysFwUMpJ2XAnfMOrp3Gado0DLST1ug_jcdRpyvN-raZSW0zNbZu4Zq8kTn6G_vXi5Pn8A_SUgT4:1u36jl:qJ6sqpYntyHuJVerv1_3vSJy8GTn0k9qVx4wQ3M_ee8', '2025-04-11 05:20:33.761229'),
('xq6lwllba2u76wmu2tx4x75xphldu0lk', '.eJxVjMsOwiAQRf-FtSHDowW6dO83kAGmFrXUFEw0xn_XJi50e86958luldaCM7GBYZpzYTvm8dYmvwmf04fLfxYwnqlsIp2wHBcel9LWHPg24V9b-WFJdNl_t3-BCev0edveBENIATBoJzoFySH1YFCBS8bGcSSrOmsgSSFC0JoigOwFjFJjxC1aqda8FE_3a14fbFAAPzSX3HzLM9WG89WzQRhwTlulgHeid51UrzcjwFQ9:1rilfm:owbcnLV6R7dii96rujjUrtBOqqsLCbsXe4VyUAusj6U', '2024-03-09 01:43:50.564532'),
('xr6t72s4pq9i1z654rgugc13u055v8m2', '.eJxVjMsOwiAQRf-FtSHDo4V26d5vIANMLWqpKZhojP9um3Sh23PuPW_2KLRknIj1DOOUMjswh486uk24FFcu_5nHcKW8iXjBfJ55mHNdkufbhO-28NMc6Xbct3-BEcu4vm1rvCEkD-h1JxoFsUNqwaCCLhobhoGsaqyBKIXwXmsKALIVMEiNAbdooVLSnB0972l5sV4B_NCUU3U1TVQqTnfHemEEWGkbC1yAUFbLzxcjElQt:1rmSfM:aEPTzrN9nRAmW-UL0wr1svOAHck9blCkbJGiSuIe4xo', '2024-03-19 06:14:40.150711'),
('y1tfvqh9sjsb1907zpgi8m89yf5huq03', '.eJxVUD1vwyAQ_S_MsQUYMHjs3q07OsxR09o4MlhtFOW_10QeGt107-P07t3JnnFLsCAZCPglJnIhFvYy2UrY6A-cv2IOxm9MlfBfkD7XdlxT2aJrq6Q92dy-rx7nt1P7cmCCPB1uFC7QXgSQZtSBeoHGaB5Q8mMM7XuQnCkDWlAInndu5AypYvSAFJO6Hs2Yc1yTxd9r3G5k6Cj9h8YUiy1xwVxguVoysF52XBnGWEupltL0l-OJ2XoMsM_FYiqx3OxSo5PhTs593589GAF975RqhJO-EYencZqyxoGWinrdhbGGOk153j8PU_cDt9xct0lo_izipM_OP6YNsUrI4_EH5GCB4w:1ueXO9:KElmWGonORzwFw2Bdbt_hgIZH4qZeIpPHd0Yk98b3iI', '2025-07-23 11:16:57.818566'),
('y9tn1e90a3ff4if0gxr5fim20fllgayb', '.eJxVT8tugzAQ_BefA8LgJ8fce-vdWtvr4BZMhI2qKMq_10Qc2uPOa2eexMBeJrNn3Ez0ZCSUXP5iFtw3poPwX5Bua-vWVLZo20PSnmxuP1aP8_XU_guYIE_VHVBrHkKnJA82ADA9dBXqK-Y4UoYcLBeMdoBMKefYILyiAF5bgQPKIzRjznFNJqZYTIkL5gLL3ZCRSi76btCStoJpzhW_1Lqz8Rhgn4vBVGJ5mOUoScYnOe99fy_WDKS0QjTMct-w6mms6mhjQXHReTUEp-r705Tn_VZNww88cnPfJqb69-STTrBgpT-nDfGQkNfrF_Z6dYk:1uqqsW:y6Xf1FnLl5E5jkn3jTGiPHpqHCFev6dsfIvLhvLNqco', '2025-09-09 10:26:12.031260'),
('ygza3iigi1v5mfg5plhk4b33pmykxo3i', '.eJxVT8tugzAQ_BefA8L4zTH33nq31ngd3IKJsFEVRfn3mohDe9x57cyTWNjLZPeMm42eDISSy1_MwfiN6SD8F6Tb2o5rKlt07SFpTza3H6vH-Xpq_wVMkKfqDmiMCKHTSgQXALhhXYX6io0CKUcBTkhOO0Cu9ThyJr2mAN44iQzVEZox57gmG1MstsQFc4HlbslAlZBGM2H6VgnGZddfat3Zegywz8ViKrE87HKUJMOTnPe-vxcbDko5KRvuhG949TROd7RxoIXsvGZh1PX9acrzfqsm9gOP3Ny3iev-PfmkEyxY6c9pQzwk5PX6BfaEdYg:1uu7h3:flDmzSjOsw9QEJPTNYC-y4T37OefArI5fy2r_cOQJjE', '2025-09-18 10:59:53.301254'),
('yi27ljm9f4xqqm3p3gcsu55c5otnxhkw', '.eJxVjU1uwyAQhe_CukKDARu87D5nQAMzrmliHBkiJap699hSFsnibd73fv7ErfJWcGExCqQll3Th7Sy-RMBbm8NBQ6Yd6k8vYjpzOQD9YvlZZVpL23KUR0S-aJWnlfjy_cp-DMxY570NXVTOd0ZZwxp2-Ymis0DKRUDbDzgNEyXrHJC2mHpjSE1gtfXM3sZjtHKteS2B79e8PcSoAd7cXHILLS9cGy7XIEY1wP7Yd9ZIPyijtP9_AvgYVdw:1reTmi:2ElzT_qt4_wvr-8Rl0mmdvtC0LUHYyxNJy9-4L4dt74', '2024-02-26 05:49:16.232018'),
('zhh1axjfq6aoo0dh7bm5t69din9ynxl4', '.eJxVkL1uwzAMhN9Fc2xItn49du_WXaAsKlZry4ElAw2CvHvlwEMDTryPR5D3IHvGLcGCZCDgl5jIhVjYy2QPYKOveveuORh_MB3Af0O6ru24prJF1x4j7Ulz-7l6nD_O2bcFE-SpupG7QBUPIMyoA_UcjdFdQNHVMlQpEB2TBjSnEHzXu7FjSCWjVZJM6GNpxpzjmiz-3uJ2J0NP6T81plhsiQvmAsvNkoGpXnIqNGctlYr25lJ_mK3HAPtcLKYSy90ux-VkeJCz3_dXDIaDUk7KhjvhG149jdOUNQ60kNTrPozHTacpz_u1mkptMTW3beK6ewVx8jPzrxcnz-cfemiA9g:1tVmTp:HOetGHUE-RcjkUkKLgpZi1hXDXlMQWyiw7npjLZ1FNU', '2025-01-09 07:02:21.122660'),
('zynqt38evfvrri5bqkkjefl0wmbz7h2f', '.eJxVUD1vwyAQ_S_MsQUYY_DYvVt3dJijprVxZLDaKMp_L0QeGt107-P07t3JkXCPsCIZCbg1RHIhBo48m0qY4ArOXzEL0zfGSrgviJ9bO20x78G2VdKebGrfN4fL26l9OTBDmosbhfV0EB56PSlPnUCtFffY8zKaDgP0nEkNSlDwjnd24gypZLRAkvWqHk2YUtiiwd9r2G9k7Cj9h4YYsslhxZRhvRoysqHvmJRU01YoyqW8lB8W49DDsWSDMYd8M2tNTsY7OffjeNagBQyDlbIRtneNKJ7GKsoaC6qX1KnOTzXTaUrL8VlM3Q_cUnPdZ6H4s4eTPiv_mHfEKiGPxx90CYGt:1ue6aR:-isySYLXuGF8QPkOEO5KngfaV3fc_zYp7hvXTomDNxU', '2025-07-22 06:39:51.988304');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `aix_absencedatemodel`
--
ALTER TABLE `aix_absencedatemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_absencedatemodel_entity_id_date_428814be_uniq` (`entity_id`,`date`),
  ADD KEY `aix_absence_created_134fa8_idx` (`created`),
  ADD KEY `aix_absence_updated_2b4ea8_idx` (`updated`),
  ADD KEY `aix_absence_date_f74f54_idx` (`date`);

--
-- Indexes for table `aix_absencetypemodel`
--
ALTER TABLE `aix_absencetypemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_absencetypemodel_entity_id_code_e94389ee_uniq` (`entity_id`,`code`),
  ADD KEY `aix_absence_created_7a3586_idx` (`created`),
  ADD KEY `aix_absence_updated_f457ac_idx` (`updated`),
  ADD KEY `aix_absence_name_d4d91a_idx` (`name`),
  ADD KEY `aix_absenc_descrip_1eccf7_idx` (`description`(768));

--
-- Indexes for table `aix_accountcodeprefixmodel`
--
ALTER TABLE `aix_accountcodeprefixmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_accountcodeprefixmodel_entity_id_prefixcode_3b790d55_uniq` (`entity_id`,`prefixcode`),
  ADD KEY `aix_account_created_eb87dd_idx` (`created`),
  ADD KEY `aix_account_updated_e3df06_idx` (`updated`),
  ADD KEY `aix_account_prefixc_63628e_idx` (`prefixcode`);

--
-- Indexes for table `aix_accountmodel`
--
ALTER TABLE `aix_accountmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_accountmodel_coa_id_code_449bf457_uniq` (`coa_id`,`code`),
  ADD KEY `aix_accountmodel_parent_id_4929e17a_fk_aix_accountmodel_uuid` (`parent_id`),
  ADD KEY `aix_account_role_231bca_idx` (`role`),
  ADD KEY `aix_account_balance_ac2527_idx` (`balance_type`),
  ADD KEY `aix_account_active_304081_idx` (`active`),
  ADD KEY `aix_account_coa_id_139ca7_idx` (`coa_id`),
  ADD KEY `aix_account_role_b98b33_idx` (`role`,`balance_type`,`active`);

--
-- Indexes for table `aix_aixitshandovermodel`
--
ALTER TABLE `aix_aixitshandovermodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_aixitshandovermodel_entity_id_equipment_id_s_8b2a61a4_uniq` (`entity_id`,`equipment_id`,`staff_id`,`status`),
  ADD KEY `aix_aixitsh_created_99a6cb_idx` (`created`),
  ADD KEY `aix_aixitsh_updated_4af488_idx` (`updated`),
  ADD KEY `aix_aixitshandovermo_staff_id_f112c157_fk_aix_emplo` (`staff_id`),
  ADD KEY `aix_aixitshandovermo_equipment_id_6d36ca1c_fk_aix_equip` (`equipment_id`);

--
-- Indexes for table `aix_aixitsstatusreportmodel`
--
ALTER TABLE `aix_aixitsstatusreportmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_aixitsstatusreportmo_entity_id_activity_statu_a180cd55_uniq` (`entity_id`,`activity`,`status`),
  ADD KEY `aix_aixitss_created_1900ba_idx` (`created`),
  ADD KEY `aix_aixitss_updated_7081b6_idx` (`updated`),
  ADD KEY `aix_aixitss_activit_314e97_idx` (`activity`);

--
-- Indexes for table `aix_announcementmodel`
--
ALTER TABLE `aix_announcementmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_announcementmodel_entity_id_value_a1a9f7ee_uniq` (`entity_id`,`value`),
  ADD KEY `aix_announc_created_5ef463_idx` (`created`),
  ADD KEY `aix_announc_updated_13f2bf_idx` (`updated`),
  ADD KEY `aix_announc_date_99d507_idx` (`date`),
  ADD KEY `aix_announc_value_b74194_idx` (`value`);

--
-- Indexes for table `aix_assetmodel`
--
ALTER TABLE `aix_assetmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `vehicle_id` (`vehicle_id`),
  ADD UNIQUE KEY `license_plate` (`license_plate`),
  ADD UNIQUE KEY `aix_assetmodel_entity_id_license_plate_fe2f34b5_uniq` (`entity_id`,`license_plate`),
  ADD KEY `aix_assetmo_license_fb1e1d_idx` (`license_plate`),
  ADD KEY `aix_assetmo_vehicle_163772_idx` (`vehicle_type_name`),
  ADD KEY `aix_assetmo_make_9a18f2_idx` (`make`),
  ADD KEY `aix_assetmo_model_8b3391_idx` (`model`);

--
-- Indexes for table `aix_attachedemailmodel`
--
ALTER TABLE `aix_attachedemailmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_attachedemailmodel_entity_id_data_270d24ca_uniq` (`entity_id`,`data`),
  ADD KEY `aix_attache_created_37dcb0_idx` (`created`),
  ADD KEY `aix_attache_updated_88d392_idx` (`updated`),
  ADD KEY `aix_attache_data_84348d_idx` (`data`);

--
-- Indexes for table `aix_bankaccountmodel`
--
ALTER TABLE `aix_bankaccountmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `ledger_id` (`ledger_id`),
  ADD UNIQUE KEY `aix_bankaccountmodel_cash_account_id_account__f9df8ddd_uniq` (`cash_account_id`,`account_number`,`routing_number`),
  ADD KEY `aix_bankacc_ledger__24c0bc_idx` (`ledger_id`),
  ADD KEY `aix_bankacc_account_2729a9_idx` (`account_type`),
  ADD KEY `aix_bankacc_cash_ac_4e0b47_idx` (`cash_account_id`,`account_type`);

--
-- Indexes for table `aix_benefitcalculationmodel`
--
ALTER TABLE `aix_benefitcalculationmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_benefitcalculationmodel_entity_id_code_8392b402_uniq` (`entity_id`,`code`),
  ADD KEY `aix_benefit_created_1e8ec8_idx` (`created`),
  ADD KEY `aix_benefit_updated_07de40_idx` (`updated`),
  ADD KEY `aix_benefit_name_ea3497_idx` (`name`),
  ADD KEY `aix_benefi_descrip_ec5c32_idx` (`description`(768));

--
-- Indexes for table `aix_benefitmodel`
--
ALTER TABLE `aix_benefitmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_benefitmodel_entity_id_value_caed2903_uniq` (`entity_id`,`value`),
  ADD KEY `aix_benefit_created_2a7102_idx` (`created`),
  ADD KEY `aix_benefit_updated_b70efa_idx` (`updated`),
  ADD KEY `aix_benefit_start_d_4b98eb_idx` (`start_date`),
  ADD KEY `aix_benefit_end_dat_e04f3f_idx` (`end_date`);

--
-- Indexes for table `aix_benefittypemodel`
--
ALTER TABLE `aix_benefittypemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_benefittypemodel_entity_id_code_ee76179e_uniq` (`entity_id`,`code`),
  ADD KEY `aix_benefit_created_eb5f70_idx` (`created`),
  ADD KEY `aix_benefit_updated_c65be2_idx` (`updated`),
  ADD KEY `aix_benefit_value_685eea_idx` (`value`(768)),
  ADD KEY `aix_benefi_descrip_924d83_idx` (`description`(768)),
  ADD KEY `aix_benefittypemode_benefit_calculation__fb16578d_fk_aix_bene` (`benefit_calculation_id`);

--
-- Indexes for table `aix_billmodel`
--
ALTER TABLE `aix_billmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `bill_number` (`bill_number`),
  ADD UNIQUE KEY `ledger_id` (`ledger_id`),
  ADD KEY `aix_billmodel_ce_model_id_2e73c454_fk_aix_estimatemodel_uuid` (`ce_model_id`),
  ADD KEY `aix_billmod_bill_st_39d2c6_idx` (`bill_status`),
  ADD KEY `aix_billmod_terms_13a487_idx` (`terms`),
  ADD KEY `aix_billmod_cash_ac_043479_idx` (`cash_account_id`),
  ADD KEY `aix_billmod_prepaid_ce3795_idx` (`prepaid_account_id`),
  ADD KEY `aix_billmod_unearne_c73460_idx` (`unearned_account_id`),
  ADD KEY `aix_billmod_due_dat_1cb629_idx` (`due_date`),
  ADD KEY `aix_billmod_draft_d_2aacaa_idx` (`draft_date`),
  ADD KEY `aix_billmod_in_revi_c6cce8_idx` (`in_review_date`),
  ADD KEY `aix_billmod_approve_4521ff_idx` (`approved_date`),
  ADD KEY `aix_billmod_paid_da_266c36_idx` (`paid_date`),
  ADD KEY `aix_billmod_cancele_3fe092_idx` (`canceled_date`),
  ADD KEY `aix_billmod_void_da_3e5963_idx` (`void_date`),
  ADD KEY `aix_billmod_vendor__8f3c0a_idx` (`vendor_id`),
  ADD KEY `aix_billmodel_xref_01ccb103` (`xref`);

--
-- Indexes for table `aix_businessindustrymodel`
--
ALTER TABLE `aix_businessindustrymodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_businessindustrymodel_entity_id_code_e368b604_uniq` (`entity_id`,`code`),
  ADD KEY `aix_busines_created_bf1b86_idx` (`created`),
  ADD KEY `aix_busines_updated_ab88da_idx` (`updated`),
  ADD KEY `aix_busines_name_1544e2_idx` (`name`),
  ADD KEY `aix_busine_descrip_d67288_idx` (`description`(768));

--
-- Indexes for table `aix_chartofaccountmodel`
--
ALTER TABLE `aix_chartofaccountmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `slug` (`slug`),
  ADD UNIQUE KEY `entity_id` (`entity_id`),
  ADD KEY `aix_chartof_entity__eb64c8_idx` (`entity_id`);

--
-- Indexes for table `aix_currencymodel`
--
ALTER TABLE `aix_currencymodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_currencymodel_entity_id_code_90235833_uniq` (`entity_id`,`code`),
  ADD KEY `aix_currenc_created_f7304e_idx` (`created`),
  ADD KEY `aix_currenc_updated_84e13c_idx` (`updated`),
  ADD KEY `aix_currenc_name_3842db_idx` (`name`);

--
-- Indexes for table `aix_currencyratemodel`
--
ALTER TABLE `aix_currencyratemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_currencyratemodel_entity_id_date_4992f3db_uniq` (`entity_id`,`date`),
  ADD KEY `aix_currenc_created_1ca4c2_idx` (`created`),
  ADD KEY `aix_currenc_updated_01b45f_idx` (`updated`),
  ADD KEY `aix_currenc_date_b10628_idx` (`date`);

--
-- Indexes for table `aix_customerlocationmodel`
--
ALTER TABLE `aix_customerlocationmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_customerlocationmode_entity_id_name_customer__46fd1e9d_uniq` (`entity_id`,`name`,`customer_id`),
  ADD KEY `aix_customerlocatio_customer_id_7eeea5d6_fk_aix_cust` (`customer_id`),
  ADD KEY `aix_custome_created_161d7f_idx` (`created`),
  ADD KEY `aix_custome_updated_f8262b_idx` (`updated`),
  ADD KEY `aix_custome_name_8a4bc4_idx` (`name`),
  ADD KEY `aix_custom_descrip_143eed_idx` (`description`(768)),
  ADD KEY `aix_customerlocationmodel_entity_id_7bd04fe1` (`entity_id`);

--
-- Indexes for table `aix_customermodel`
--
ALTER TABLE `aix_customermodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `user_id` (`user_id`),
  ADD UNIQUE KEY `aix_customermodel_entity_id_customer_name_f6a3ac21_uniq` (`entity_id`,`customer_name`),
  ADD KEY `aix_customermodel_nation_id_3c09bdeb_fk_aix_nationmodel_uuid` (`nation_id`),
  ADD KEY `aix_custome_created_9e452a_idx` (`created`),
  ADD KEY `aix_custome_updated_c47bed_idx` (`updated`),
  ADD KEY `aix_custome_active_52e2e0_idx` (`active`),
  ADD KEY `aix_custome_hidden_a42aab_idx` (`hidden`),
  ADD KEY `aix_customermodel_business_industry_id_f3b16fa8_fk_aix_busi` (`business_industry_id`);

--
-- Indexes for table `aix_departmentmodel`
--
ALTER TABLE `aix_departmentmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_departmentmodel_entity_id_code_28267129_uniq` (`entity_id`,`code`),
  ADD KEY `aix_departm_created_56ed8b_idx` (`created`),
  ADD KEY `aix_departm_updated_20802e_idx` (`updated`),
  ADD KEY `aix_departm_name_709d9e_idx` (`name`);

--
-- Indexes for table `aix_dependantmodel`
--
ALTER TABLE `aix_dependantmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_dependantmodel_entity_id_first_name_a3e7ce05_uniq` (`entity_id`,`first_name`),
  ADD KEY `aix_dependa_created_86fdee_idx` (`created`),
  ADD KEY `aix_dependa_updated_3ccc5f_idx` (`updated`),
  ADD KEY `aix_dependa_first_n_1941c1_idx` (`first_name`),
  ADD KEY `aix_dependa_last_na_a24c1a_idx` (`last_name`);

--
-- Indexes for table `aix_documentmodel`
--
ALTER TABLE `aix_documentmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_documentmodel_entity_id_name_updated_d527cbaa_uniq` (`entity_id`,`name`,`updated`),
  ADD KEY `aix_documen_created_78ba9e_idx` (`created`),
  ADD KEY `aix_documen_updated_e89819_idx` (`updated`),
  ADD KEY `aix_documen_name_2f4809_idx` (`name`),
  ADD KEY `aix_documen_name_on_054015_idx` (`name_on_file`),
  ADD KEY `aix_documentmodel_activity_id_a24cd5e5_fk_aix_worko` (`activity_id`),
  ADD KEY `aix_documentmodel_task_id_95a39bc6_fk_aix_worko` (`task_id`),
  ADD KEY `aix_documentmodel_work_order_id_90fdd9f1_fk_aix_worko` (`work_order_id`),
  ADD KEY `aix_documentmodel_entity_id_7185cd21` (`entity_id`);

--
-- Indexes for table `aix_documentstatusmodel`
--
ALTER TABLE `aix_documentstatusmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_documentstatusmodel_entity_id_code_878ec3b0_uniq` (`entity_id`,`code`),
  ADD KEY `aix_documen_created_7e8cf2_idx` (`created`),
  ADD KEY `aix_documen_updated_e77df9_idx` (`updated`),
  ADD KEY `aix_documen_name_18b93e_idx` (`name`);

--
-- Indexes for table `aix_documenttypemodel`
--
ALTER TABLE `aix_documenttypemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_documenttypemodel_entity_id_code_2465f877_uniq` (`entity_id`,`code`),
  ADD KEY `aix_documen_created_1ffba9_idx` (`created`),
  ADD KEY `aix_documen_updated_23d8db_idx` (`updated`),
  ADD KEY `aix_documen_name_971c02_idx` (`name`);

--
-- Indexes for table `aix_educationmodel`
--
ALTER TABLE `aix_educationmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_educationmodel_entity_id_specialization_14453223_uniq` (`entity_id`,`specialization`),
  ADD KEY `aix_educati_created_04fd95_idx` (`created`),
  ADD KEY `aix_educati_updated_062d01_idx` (`updated`),
  ADD KEY `aix_educati_special_d005c9_idx` (`specialization`),
  ADD KEY `aix_educati_start_d_0e99d5_idx` (`start_date`);

--
-- Indexes for table `aix_employeeassignmentmodel`
--
ALTER TABLE `aix_employeeassignmentmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_employeeassignmentmodel_entity_id_start_date_b0a5607a_uniq` (`entity_id`,`start_date`),
  ADD KEY `aix_employe_created_13e079_idx` (`created`),
  ADD KEY `aix_employe_updated_d53365_idx` (`updated`),
  ADD KEY `aix_employe_start_d_01b5a6_idx` (`start_date`),
  ADD KEY `aix_employe_end_dat_81d266_idx` (`end_date`);

--
-- Indexes for table `aix_employeeavatarmodel`
--
ALTER TABLE `aix_employeeavatarmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_employeeavatarmodel_entity_id_name_43098e0f_uniq` (`entity_id`,`name`),
  ADD KEY `aix_employe_created_c57b6e_idx` (`created`),
  ADD KEY `aix_employe_updated_56a276_idx` (`updated`),
  ADD KEY `aix_employe_name_5274c9_idx` (`name`),
  ADD KEY `aix_employe_extensi_e67ca6_idx` (`extension`);

--
-- Indexes for table `aix_employeecontractmodel`
--
ALTER TABLE `aix_employeecontractmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_employeecontractmodel_entity_id_start_date_327dcc23_uniq` (`entity_id`,`start_date`),
  ADD KEY `aix_employe_created_661e90_idx` (`created`),
  ADD KEY `aix_employe_updated_45db81_idx` (`updated`),
  ADD KEY `aix_employe_start_d_fe2c75_idx` (`start_date`),
  ADD KEY `aix_employe_end_dat_af595b_idx` (`end_date`);

--
-- Indexes for table `aix_employeecontracttypemodel`
--
ALTER TABLE `aix_employeecontracttypemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_employeecontracttypemodel_entity_id_code_186e847f_uniq` (`entity_id`,`code`),
  ADD KEY `aix_employe_created_9e51a6_idx` (`created`),
  ADD KEY `aix_employe_updated_8eda8e_idx` (`updated`),
  ADD KEY `aix_employe_name_58e885_idx` (`name`);

--
-- Indexes for table `aix_employeefawmodel`
--
ALTER TABLE `aix_employeefawmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_employeefawmodel_entity_id_faw_date_locat_36752edd_uniq` (`entity_id`,`faw_date`,`location_id`,`work_order_id`),
  ADD KEY `aix_employe_created_19c4c2_idx` (`created`),
  ADD KEY `aix_employe_updated_175664_idx` (`updated`),
  ADD KEY `aix_employeefawmodel_location_id_83a8c5e2_fk_aix_custo` (`location_id`),
  ADD KEY `aix_employeefawmodel_work_order_id_2d3fb326_fk_aix_worko` (`work_order_id`),
  ADD KEY `aix_employeefawmodel_entity_id_658689b0` (`entity_id`);

--
-- Indexes for table `aix_employeelanguagemodel`
--
ALTER TABLE `aix_employeelanguagemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_employeelanguagemodel_entity_id_read_2e787269_uniq` (`entity_id`,`read`),
  ADD KEY `aix_employe_created_9830a0_idx` (`created`),
  ADD KEY `aix_employe_updated_8e3249_idx` (`updated`),
  ADD KEY `aix_employe_read_773c84_idx` (`read`),
  ADD KEY `aix_employe_write_bc2e90_idx` (`write`),
  ADD KEY `aix_employe_speak_a1d39b_idx` (`speak`);

--
-- Indexes for table `aix_employeelicensedetailmodel`
--
ALTER TABLE `aix_employeelicensedetailmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_employeelicensedeta_entity_id_issue_date_cd89a039_uniq` (`entity_id`,`issue_date`),
  ADD KEY `aix_employe_created_196bf0_idx` (`created`),
  ADD KEY `aix_employe_updated_868cf0_idx` (`updated`),
  ADD KEY `aix_employe_issue_d_c32b38_idx` (`issue_date`),
  ADD KEY `aix_employe_expiry__25a8e4_idx` (`expiry_date`);

--
-- Indexes for table `aix_employeelicensetypemodel`
--
ALTER TABLE `aix_employeelicensetypemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_employeelicensetypemodel_entity_id_code_ac3c4f6b_uniq` (`entity_id`,`code`),
  ADD KEY `aix_employe_created_edebd8_idx` (`created`),
  ADD KEY `aix_employe_updated_63b92b_idx` (`updated`),
  ADD KEY `aix_employe_name_1d6f80_idx` (`name`),
  ADD KEY `aix_employ_descrip_7697b3_idx` (`description`(768));

--
-- Indexes for table `aix_employeemodel`
--
ALTER TABLE `aix_employeemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_employeemodel_entity_id_idnumber_username_id_cd473bb5_uniq` (`entity_id`,`idnumber`,`username_id`),
  ADD KEY `aix_employeemodel_username_id_71f6c345_fk_auth_user_id` (`username_id`),
  ADD KEY `aix_employe_created_581297_idx` (`created`),
  ADD KEY `aix_employe_updated_6b8b3b_idx` (`updated`),
  ADD KEY `aix_employe_idnumbe_a237f2_idx` (`idnumber`),
  ADD KEY `aix_employe_name_4dd804_idx` (`name`),
  ADD KEY `aix_employeemodel_department_id_0bd1eb92_fk_aix_depa` (`department_id`);

--
-- Indexes for table `aix_employeeoftheweekmodel`
--
ALTER TABLE `aix_employeeoftheweekmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_employeeoftheweekmodel_entity_id_week_number_d4a74f23_uniq` (`entity_id`,`week_number`),
  ADD KEY `aix_employe_created_767c69_idx` (`created`),
  ADD KEY `aix_employe_updated_6a10e2_idx` (`updated`);

--
-- Indexes for table `aix_employeepayrollbenefitmodel`
--
ALTER TABLE `aix_employeepayrollbenefitmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_employeepayrollbene_entity_id_polarity_4fb065e4_uniq` (`entity_id`,`polarity`),
  ADD KEY `aix_employe_created_6262e9_idx` (`created`),
  ADD KEY `aix_employe_updated_a69f2a_idx` (`updated`);

--
-- Indexes for table `aix_employeepayrollmodel`
--
ALTER TABLE `aix_employeepayrollmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_employeepayrollmode_entity_id_start_date_emp_4b01d2c6_uniq` (`entity_id`,`start_date`,`employee_id`),
  ADD KEY `aix_employe_created_494813_idx` (`created`),
  ADD KEY `aix_employe_updated_410ff0_idx` (`updated`),
  ADD KEY `aix_employe_start_d_0f55cb_idx` (`start_date`);

--
-- Indexes for table `aix_employeetransactionmodel`
--
ALTER TABLE `aix_employeetransactionmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_employeetransaction_entity_id_account_name_af4a9fe6_uniq` (`entity_id`,`account_name`),
  ADD KEY `aix_employe_created_d73986_idx` (`created`),
  ADD KEY `aix_employe_updated_62e531_idx` (`updated`),
  ADD KEY `aix_employe_account_f0222b_idx` (`account_name`);

--
-- Indexes for table `aix_entitymanagementmodel`
--
ALTER TABLE `aix_entitymanagementmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD KEY `aix_entitym_entity__19fb49_idx` (`entity_id`,`user_id`),
  ADD KEY `aix_entitym_user_id_da80a0_idx` (`user_id`,`entity_id`);

--
-- Indexes for table `aix_entitymodel`
--
ALTER TABLE `aix_entitymodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `slug` (`slug`),
  ADD KEY `aix_entitym_admin_i_5978bb_idx` (`admin_id`);

--
-- Indexes for table `aix_entityunitmodel`
--
ALTER TABLE `aix_entityunitmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_entityunitmodel_entity_id_slug_85d51efb_uniq` (`entity_id`,`slug`),
  ADD KEY `aix_entityu_active_1e197d_idx` (`active`),
  ADD KEY `aix_entityu_hidden_5a41fe_idx` (`hidden`),
  ADD KEY `aix_entityu_entity__910739_idx` (`entity_id`),
  ADD KEY `aix_entityunitmodel_parent_id_57347d13_fk_aix_enti` (`parent_id`),
  ADD KEY `aix_entityunitmodel_slug_88247c13` (`slug`);

--
-- Indexes for table `aix_equipmentassignmentmodel`
--
ALTER TABLE `aix_equipmentassignmentmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_equipmentassignmentm_entity_id_date_equipment_5c9374d0_uniq` (`entity_id`,`date`,`equipment_id`,`operator_id`),
  ADD KEY `aix_equipmentassignm_equipment_id_502d5060_fk_aix_equip` (`equipment_id`),
  ADD KEY `aix_equipmentassignm_operator_id_5eb92ab8_fk_aix_emplo` (`operator_id`),
  ADD KEY `aix_equipme_created_a8b458_idx` (`created`),
  ADD KEY `aix_equipme_updated_d6e6d6_idx` (`updated`),
  ADD KEY `aix_equipme_is_acti_272633_idx` (`is_active`);

--
-- Indexes for table `aix_equipmentaxlemodel`
--
ALTER TABLE `aix_equipmentaxlemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_equipmentaxlemodel_entity_id_code_3e2d8a29_uniq` (`entity_id`,`code`),
  ADD KEY `aix_equipme_created_cbe96c_idx` (`created`),
  ADD KEY `aix_equipme_updated_c43da8_idx` (`updated`),
  ADD KEY `aix_equipme_name_c69081_idx` (`name`);

--
-- Indexes for table `aix_equipmentfetmodel`
--
ALTER TABLE `aix_equipmentfetmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_equipmentfetmodel_entity_id_fet_date_locat_ef270137_uniq` (`entity_id`,`fet_date`,`location_id`,`work_order_id`),
  ADD KEY `aix_equipme_created_b86074_idx` (`created`),
  ADD KEY `aix_equipme_updated_37167f_idx` (`updated`),
  ADD KEY `aix_equipmentfetmode_location_id_273d8eec_fk_aix_custo` (`location_id`),
  ADD KEY `aix_equipmentfetmode_work_order_id_c82a8661_fk_aix_worko` (`work_order_id`);

--
-- Indexes for table `aix_equipmentfuelmodel`
--
ALTER TABLE `aix_equipmentfuelmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_equipmentfuelmodel_entity_id_fuel_date_equi_f9b87d3d_uniq` (`entity_id`,`fuel_date`,`equipment_id`,`work_order_id`,`StartLocation`),
  ADD KEY `aix_equipmentfuelmod_work_order_id_569313e4_fk_aix_worko` (`work_order_id`),
  ADD KEY `aix_equipme_fuel_da_9a4dee_idx` (`fuel_date`),
  ADD KEY `aix_equipme_equipme_c1d551_idx` (`equipment_id`),
  ADD KEY `aix_equipme_StartLo_4314de_idx` (`StartLocation`),
  ADD KEY `aix_equipme_EndLoca_e9836c_idx` (`EndLocation`),
  ADD KEY `aix_equipme_status_58f7af_idx` (`status`),
  ADD KEY `aix_equipmentfuelmod_fuel_reciept_id_a961ac4e_fk_aix_docum` (`fuel_reciept_id`);

--
-- Indexes for table `aix_equipmenthandovermodel`
--
ALTER TABLE `aix_equipmenthandovermodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_equipmenthandovermod_entity_id_ho_date_equipm_8ac72d86_uniq` (`entity_id`,`ho_date`,`equipment_id`,`handover_by_id`,`received_by_id`),
  ADD KEY `aix_equipmenthandove_equipment_id_d3541d1c_fk_aix_equip` (`equipment_id`),
  ADD KEY `aix_equipmenthandove_handover_by_id_51a6270d_fk_aix_emplo` (`handover_by_id`),
  ADD KEY `aix_equipmenthandove_location_id_aa906c11_fk_aix_custo` (`location_id`),
  ADD KEY `aix_equipmenthandove_received_by_id_760d21ec_fk_aix_emplo` (`received_by_id`),
  ADD KEY `aix_equipme_created_aa3bbf_idx` (`created`),
  ADD KEY `aix_equipme_updated_b50d04_idx` (`updated`),
  ADD KEY `aix_equipme_is_acti_dc8718_idx` (`is_active`),
  ADD KEY `aix_equipmenthandove_approved_by_hr_id_ba311600_fk_aix_emplo` (`approved_by_hr_id`),
  ADD KEY `aix_equipmenthandove_approved_by_ict_id_2e172361_fk_aix_emplo` (`approved_by_ict_id`);

--
-- Indexes for table `aix_equipmentjoinmodel`
--
ALTER TABLE `aix_equipmentjoinmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_equipmentjoinmodel_entity_id_date_eq_primar_0ebd45ca_uniq` (`entity_id`,`date`,`eq_primary_id`,`eq_secondary_id`,`is_active`),
  ADD KEY `aix_equipmentjoinmod_eq_primary_id_c34d2cea_fk_aix_equip` (`eq_primary_id`),
  ADD KEY `aix_equipmentjoinmod_eq_secondary_id_78d06edc_fk_aix_equip` (`eq_secondary_id`),
  ADD KEY `aix_equipme_created_328d84_idx` (`created`),
  ADD KEY `aix_equipme_updated_366182_idx` (`updated`),
  ADD KEY `aix_equipme_is_acti_cef0af_idx` (`is_active`);

--
-- Indexes for table `aix_equipmentmanufacturermodel`
--
ALTER TABLE `aix_equipmentmanufacturermodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_equipmentmanufacturermodel_entity_id_code_77c03e78_uniq` (`entity_id`,`code`),
  ADD KEY `aix_equipme_created_ff2342_idx` (`created`),
  ADD KEY `aix_equipme_updated_cb1265_idx` (`updated`),
  ADD KEY `aix_equipme_name_a51cd4_idx` (`name`);

--
-- Indexes for table `aix_equipmentmodel`
--
ALTER TABLE `aix_equipmentmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `serial` (`serial`),
  ADD UNIQUE KEY `code` (`code`),
  ADD UNIQUE KEY `aix_equipmentmodel_entity_id_reg_no_d1eb2074_uniq` (`entity_id`,`reg_no`),
  ADD KEY `aix_equipmentmodel_eq_type_id_f20ea336_fk_aix_equip` (`eq_type_id`),
  ADD KEY `aix_equipme_created_af845b_idx` (`created`),
  ADD KEY `aix_equipme_updated_d4b5a2_idx` (`updated`),
  ADD KEY `aix_equipmentmodel_eq_manufacturer_id_d3ae55a5_fk_aix_equip` (`eq_manufacturer_id`),
  ADD KEY `aix_equipme_active_6e1580_idx` (`active`),
  ADD KEY `aix_equipmentmodel_asset_id_fec36e0e_fk_aix_assetmodel_uuid` (`asset_id`);

--
-- Indexes for table `aix_equipmenttypemodel`
--
ALTER TABLE `aix_equipmenttypemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_equipmenttypemodel_entity_id_code_fa2882f6_uniq` (`entity_id`,`code`),
  ADD KEY `aix_equipme_created_1897a8_idx` (`created`),
  ADD KEY `aix_equipme_updated_d89575_idx` (`updated`),
  ADD KEY `aix_equipme_name_515932_idx` (`name`);

--
-- Indexes for table `aix_estimatemodel`
--
ALTER TABLE `aix_estimatemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_estimatemodel_entity_id_estimate_number_1160d659_uniq` (`entity_id`,`estimate_number`),
  ADD KEY `aix_estimat_status_45d7d1_idx` (`status`),
  ADD KEY `aix_estimat_custome_87fd12_idx` (`customer_id`),
  ADD KEY `aix_estimat_terms_83ab0d_idx` (`terms`),
  ADD KEY `aix_estimat_entity__5e658f_idx` (`entity_id`),
  ADD KEY `aix_estimat_date_dr_e0bfc6_idx` (`date_draft`),
  ADD KEY `aix_estimat_date_in_20455f_idx` (`date_in_review`),
  ADD KEY `aix_estimat_date_ap_dbb3dc_idx` (`date_approved`),
  ADD KEY `aix_estimat_date_ca_a0fc01_idx` (`date_canceled`),
  ADD KEY `aix_estimat_date_vo_33cd77_idx` (`date_void`),
  ADD KEY `aix_estimatemodel_estimate_number_c94257cb` (`estimate_number`);

--
-- Indexes for table `aix_generalnotificationmodel`
--
ALTER TABLE `aix_generalnotificationmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_generalnotificationmodel_entity_id_title_4cc485fe_uniq` (`entity_id`,`title`) USING HASH,
  ADD KEY `aix_general_created_72fc3b_idx` (`created`),
  ADD KEY `aix_general_updated_bba59c_idx` (`updated`),
  ADD KEY `aix_general_link_94139e_idx` (`link`(768)),
  ADD KEY `aix_genera_title_fb944b_idx` (`title`(768));

--
-- Indexes for table `aix_holidaymodel`
--
ALTER TABLE `aix_holidaymodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_holidaymodel_entity_id_code_261068a2_uniq` (`entity_id`,`code`),
  ADD KEY `aix_holiday_created_b2d38e_idx` (`created`),
  ADD KEY `aix_holiday_updated_bf63cc_idx` (`updated`),
  ADD KEY `aix_holiday_name_0b12f9_idx` (`name`);

--
-- Indexes for table `aix_immigrationdetailmodel`
--
ALTER TABLE `aix_immigrationdetailmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_immigrationdetailmo_entity_id_passport_numbe_e70d8f48_uniq` (`entity_id`,`passport_number`),
  ADD KEY `aix_immigra_created_d93dcb_idx` (`created`),
  ADD KEY `aix_immigra_updated_1ba683_idx` (`updated`),
  ADD KEY `aix_immigra_passpor_4a3f6c_idx` (`passport_number`),
  ADD KEY `aix_immigra_issue_d_e49b8f_idx` (`issue_date`),
  ADD KEY `aix_immigrationdeta_employee_id_825e8e30_fk_aix_empl` (`employee_id`);

--
-- Indexes for table `aix_importjobmodel`
--
ALTER TABLE `aix_importjobmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD KEY `aix_importj_ledger__ac0705_idx` (`ledger_id`);

--
-- Indexes for table `aix_incomingdocumenthandlermodel`
--
ALTER TABLE `aix_incomingdocumenthandlermodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_incomingdocumenthan_entity_id_employee_id_in_44c7f700_uniq` (`entity_id`,`employee_id`,`incoming_document_id`),
  ADD KEY `aix_incomin_created_59981f_idx` (`created`),
  ADD KEY `aix_incomin_updated_c40245_idx` (`updated`);

--
-- Indexes for table `aix_incomingdocumentmodel`
--
ALTER TABLE `aix_incomingdocumentmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_incomingdocumentmodel_entity_id_doc_from_4d558467_uniq` (`entity_id`,`doc_from`),
  ADD KEY `aix_incomin_created_e7af39_idx` (`created`),
  ADD KEY `aix_incomin_updated_058bea_idx` (`updated`),
  ADD KEY `aix_incomin_doc_fro_0b1f58_idx` (`doc_from`),
  ADD KEY `aix_incomin_subject_bec1ce_idx` (`subject`);

--
-- Indexes for table `aix_incomingdocumenttypemodel`
--
ALTER TABLE `aix_incomingdocumenttypemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_incomingdocumenttypemodel_entity_id_code_56946482_uniq` (`entity_id`,`code`),
  ADD KEY `aix_incomin_created_fd2ca2_idx` (`created`),
  ADD KEY `aix_incomin_updated_284db4_idx` (`updated`),
  ADD KEY `aix_incomin_name_d92a7b_idx` (`name`);

--
-- Indexes for table `aix_insurancedetailmodel`
--
ALTER TABLE `aix_insurancedetailmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_insurancedetailmodel_entity_id_policy_name_611e2ea2_uniq` (`entity_id`,`policy_name`),
  ADD KEY `aix_insuran_created_76db84_idx` (`created`),
  ADD KEY `aix_insuran_updated_04dea6_idx` (`updated`),
  ADD KEY `aix_insuran_policy__104aac_idx` (`policy_name`),
  ADD KEY `aix_insuran_company_b0de5c_idx` (`company_name`);

--
-- Indexes for table `aix_invoiceactionmodel`
--
ALTER TABLE `aix_invoiceactionmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_invoiceactionmodel_entity_id_comment_83ade445_uniq` (`entity_id`,`comment`) USING HASH,
  ADD KEY `aix_invoice_created_1e4209_idx` (`created`),
  ADD KEY `aix_invoice_updated_7a83db_idx` (`updated`),
  ADD KEY `aix_invoice_comment_687d2d_idx` (`comment`(768));

--
-- Indexes for table `aix_invoicemodel`
--
ALTER TABLE `aix_invoicemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `invoice_number` (`invoice_number`),
  ADD UNIQUE KEY `ledger_id` (`ledger_id`),
  ADD KEY `aix_invoice_due_dat_23794c_idx` (`due_date`),
  ADD KEY `aix_invoice_invoice_7a8c04_idx` (`invoice_status`),
  ADD KEY `aix_invoice_terms_06c667_idx` (`terms`),
  ADD KEY `aix_invoice_custome_891b39_idx` (`customer_id`),
  ADD KEY `aix_invoice_cash_ac_24da67_idx` (`cash_account_id`),
  ADD KEY `aix_invoice_prepaid_6fde5d_idx` (`prepaid_account_id`),
  ADD KEY `aix_invoice_unearne_be876a_idx` (`unearned_account_id`),
  ADD KEY `aix_invoice_draft_d_7cfaa1_idx` (`draft_date`),
  ADD KEY `aix_invoice_in_revi_da7959_idx` (`in_review_date`),
  ADD KEY `aix_invoice_approve_b9a556_idx` (`approved_date`),
  ADD KEY `aix_invoice_paid_da_f78691_idx` (`paid_date`),
  ADD KEY `aix_invoice_void_da_6bd4e3_idx` (`void_date`),
  ADD KEY `aix_invoice_cancele_f8300c_idx` (`canceled_date`),
  ADD KEY `aix_invoicemodel_ce_model_id_9e913a14_fk_aix_esti` (`ce_model_id`);

--
-- Indexes for table `aix_invoicestatusmodel`
--
ALTER TABLE `aix_invoicestatusmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_invoicestatusmodel_entity_id_code_78f9c35b_uniq` (`entity_id`,`code`),
  ADD KEY `aix_invoice_created_a8150d_idx` (`created`),
  ADD KEY `aix_invoice_updated_8d39f0_idx` (`updated`),
  ADD KEY `aix_invoice_name_f05fde_idx` (`name`);

--
-- Indexes for table `aix_invoicetypemodel`
--
ALTER TABLE `aix_invoicetypemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_invoicetypemodel_entity_id_code_c8754f6e_uniq` (`entity_id`,`code`),
  ADD KEY `aix_invoice_created_617a7b_idx` (`created`),
  ADD KEY `aix_invoice_updated_92a13a_idx` (`updated`),
  ADD KEY `aix_invoice_name_9a78a0_idx` (`name`);

--
-- Indexes for table `aix_itemfawmodel`
--
ALTER TABLE `aix_itemfawmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD KEY `aix_itemfaw_is_acti_1baf49_idx` (`is_active`),
  ADD KEY `aix_itemfaw_attenda_fae22a_idx` (`attendance_code`),
  ADD KEY `aix_itemfaw_entity__df2a15_idx` (`entity_id`,`attendance_code`);

--
-- Indexes for table `aix_itemfawthroughmodel`
--
ALTER TABLE `aix_itemfawthroughmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD KEY `aix_itemfaw_faw_ite_8abca4_idx` (`faw_item_status`),
  ADD KEY `aix_itemfawthroughmo_entity_unit_id_65d92892_fk_aix_entit` (`entity_unit_id`),
  ADD KEY `aix_itemfawthroughmo_parent_id_036645c4_fk_aix_itemf` (`parent_id`),
  ADD KEY `aix_itemfawthroughmo_employee_model_id_61a12ca1_fk_aix_emplo` (`employee_model_id`),
  ADD KEY `aix_itemfawthroughmodel_faw_model_id_e6568dea` (`faw_model_id`),
  ADD KEY `aix_itemfaw_faw_mod_4af1f1_idx` (`faw_model_id`,`employee_model_id`);

--
-- Indexes for table `aix_itemfetmodel`
--
ALTER TABLE `aix_itemfetmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD KEY `aix_itemfet_is_acti_0fbc39_idx` (`is_active`),
  ADD KEY `aix_itemfet_attenda_d11497_idx` (`attendance_code`),
  ADD KEY `aix_itemfet_entity__a3e965_idx` (`entity_id`,`attendance_code`);

--
-- Indexes for table `aix_itemfetthroughmodel`
--
ALTER TABLE `aix_itemfetthroughmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD KEY `aix_itemfet_fet_mod_d9f02a_idx` (`fet_model_id`,`equipment_model_id`),
  ADD KEY `aix_itemfet_fet_ite_01b431_idx` (`fet_item_status`),
  ADD KEY `aix_itemfetthroughmo_entity_unit_id_4b04bb90_fk_aix_entit` (`entity_unit_id`),
  ADD KEY `aix_itemfetthroughmo_equipment_model_id_e2ff9dd8_fk_aix_equip` (`equipment_model_id`),
  ADD KEY `aix_itemfetthroughmo_parent_id_64ed8fb9_fk_aix_itemf` (`parent_id`);

--
-- Indexes for table `aix_itemmodel`
--
ALTER TABLE `aix_itemmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD KEY `aix_itemmodel_uom_id_eafbae0d_fk_aix_unitofmeasuremodel_uuid` (`uom_id`),
  ADD KEY `aix_itemmod_invento_2ab7ec_idx` (`inventory_account_id`),
  ADD KEY `aix_itemmod_cogs_ac_08bbd0_idx` (`cogs_account_id`),
  ADD KEY `aix_itemmod_earning_220a27_idx` (`earnings_account_id`),
  ADD KEY `aix_itemmod_expense_3a6cc4_idx` (`expense_account_id`),
  ADD KEY `aix_itemmod_for_inv_ab246d_idx` (`for_inventory`),
  ADD KEY `aix_itemmod_is_prod_5952bb_idx` (`is_product_or_service`),
  ADD KEY `aix_itemmod_is_acti_1d2096_idx` (`is_active`),
  ADD KEY `aix_itemmod_item_ty_77015f_idx` (`item_type`),
  ADD KEY `aix_itemmod_entity__e6c7d2_idx` (`entity_id`,`sku`),
  ADD KEY `aix_itemmod_entity__b26e8c_idx` (`entity_id`,`upc`),
  ADD KEY `aix_itemmod_entity__6bfd25_idx` (`entity_id`,`item_id`);

--
-- Indexes for table `aix_itemthroughmodel`
--
ALTER TABLE `aix_itemthroughmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD KEY `aix_itemthroughmode_parent_id_cc95962e_fk_aix_item` (`parent_id`),
  ADD KEY `aix_itemthr_bill_mo_556cbf_idx` (`bill_model_id`,`item_model_id`),
  ADD KEY `aix_itemthr_invoice_5d78cb_idx` (`invoice_model_id`,`item_model_id`),
  ADD KEY `aix_itemthr_po_mode_55525e_idx` (`po_model_id`,`item_model_id`),
  ADD KEY `aix_itemthr_jcd_mod_f2d64c_idx` (`jcd_model_id`,`item_model_id`),
  ADD KEY `aix_itemthr_ce_mode_83caba_idx` (`ce_model_id`,`item_model_id`),
  ADD KEY `aix_itemthr_po_item_1e656e_idx` (`po_item_status`),
  ADD KEY `aix_itemthr_jcd_ite_38f056_idx` (`jcd_item_status`),
  ADD KEY `aix_itemthroughmode_entity_unit_id_c024cf30_fk_aix_enti` (`entity_unit_id`),
  ADD KEY `aix_itemthroughmode_item_model_id_a331218d_fk_aix_item` (`item_model_id`);

--
-- Indexes for table `aix_jobapplicantmodel`
--
ALTER TABLE `aix_jobapplicantmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_jobapplicantmodel_entity_id_date_job_id_ap_54d1fe64_uniq` (`entity_id`,`date`,`job_id`,`applicant_id`,`is_active`),
  ADD KEY `aix_jobappl_created_263415_idx` (`created`),
  ADD KEY `aix_jobappl_updated_6df9f8_idx` (`updated`),
  ADD KEY `aix_jobappl_is_acti_1e1020_idx` (`is_active`);

--
-- Indexes for table `aix_jobcategorymodel`
--
ALTER TABLE `aix_jobcategorymodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_jobcategorymodel_entity_id_code_5904824b_uniq` (`entity_id`,`code`),
  ADD KEY `aix_jobcate_created_96565f_idx` (`created`),
  ADD KEY `aix_jobcate_updated_28d540_idx` (`updated`),
  ADD KEY `aix_jobcate_name_372800_idx` (`name`);

--
-- Indexes for table `aix_jobmodel`
--
ALTER TABLE `aix_jobmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_jobmodel_entity_id_title_category_id_ab92e44a_uniq` (`entity_id`,`title`,`category_id`),
  ADD KEY `aix_jobmode_created_0e341d_idx` (`created`),
  ADD KEY `aix_jobmode_updated_aed800_idx` (`updated`),
  ADD KEY `aix_jobmode_title_8b272d_idx` (`title`);

--
-- Indexes for table `aix_journalentrymodel`
--
ALTER TABLE `aix_journalentrymodel`
  ADD PRIMARY KEY (`uuid`),
  ADD KEY `aix_journal_date_96d252_idx` (`date`),
  ADD KEY `aix_journal_activit_9fc661_idx` (`activity`),
  ADD KEY `aix_journal_parent__193d55_idx` (`parent_id`),
  ADD KEY `aix_journal_entity__d666f8_idx` (`entity_unit_id`),
  ADD KEY `aix_journal_ledger__68474f_idx` (`ledger_id`,`posted`),
  ADD KEY `aix_journal_locked_69f792_idx` (`locked`);

--
-- Indexes for table `aix_kpihsemodel`
--
ALTER TABLE `aix_kpihsemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `code` (`code`),
  ADD UNIQUE KEY `aix_kpihsemodel_entity_id_code_4a055e3a_uniq` (`entity_id`,`code`),
  ADD KEY `aix_kpihsem_activit_bf58c0_idx` (`activity_date`),
  ADD KEY `aix_kpihsem_status_23e7e8_idx` (`status`);

--
-- Indexes for table `aix_kpionoffmodel`
--
ALTER TABLE `aix_kpionoffmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `code` (`code`),
  ADD UNIQUE KEY `aix_kpionoffmodel_entity_id_code_165a03cc_uniq` (`entity_id`,`code`),
  ADD KEY `aix_kpionof_activit_5a4e78_idx` (`activity_date`),
  ADD KEY `aix_kpionof_activit_f7bc47_idx` (`activity_description`(768)),
  ADD KEY `aix_kpionof_status_62c8d0_idx` (`status`),
  ADD KEY `aix_kpionoffmodel_task_id_762a15f5_fk_aix_work` (`task_id`);

--
-- Indexes for table `aix_kpiopsmodel`
--
ALTER TABLE `aix_kpiopsmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `code` (`code`),
  ADD KEY `aix_kpiopsm_activit_831ef3_idx` (`activity_date`),
  ADD KEY `aix_kpiopsm_activit_e34a60_idx` (`activity_description`(768)),
  ADD KEY `aix_kpiopsm_status_e6ffed_idx` (`status`),
  ADD KEY `aix_kpiopsmodel_equipment_id_4177f6db_fk_aix_assetmodel_uuid` (`equipment_id`);

--
-- Indexes for table `aix_kpipobmodel`
--
ALTER TABLE `aix_kpipobmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `code` (`code`),
  ADD UNIQUE KEY `aix_kpipobmodel_entity_id_code_c2f921f9_uniq` (`entity_id`,`code`),
  ADD KEY `aix_kpipobm_activit_5f2a55_idx` (`activity_date`),
  ADD KEY `aix_kpipobm_activit_590108_idx` (`activity_description`(768)),
  ADD KEY `aix_kpipobm_status_3f7eca_idx` (`status`),
  ADD KEY `aix_kpipobmodel_task_id_16fe7a38_fk_aix_work` (`task_id`),
  ADD KEY `aix_kpipobmodel_activity_location_id_52919f19` (`activity_location_id`);

--
-- Indexes for table `aix_languagemodel`
--
ALTER TABLE `aix_languagemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_languagemodel_entity_id_code_ae0bad8a_uniq` (`entity_id`,`code`),
  ADD KEY `aix_languag_created_f0fdba_idx` (`created`),
  ADD KEY `aix_languag_updated_338412_idx` (`updated`),
  ADD KEY `aix_languag_name_69a907_idx` (`name`);

--
-- Indexes for table `aix_leavecardcarriedovermodel`
--
ALTER TABLE `aix_leavecardcarriedovermodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_leavecardcarriedovermodel_entity_id_days_3cd918a4_uniq` (`entity_id`,`days`),
  ADD KEY `aix_leaveca_created_1a3ed4_idx` (`created`),
  ADD KEY `aix_leaveca_updated_c5c81c_idx` (`updated`);

--
-- Indexes for table `aix_leavecarddetailmodel`
--
ALTER TABLE `aix_leavecarddetailmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_leavecarddetailmodel_entity_id_credit_12f08f8b_uniq` (`entity_id`,`credit`),
  ADD KEY `aix_leaveca_created_eafb91_idx` (`created`),
  ADD KEY `aix_leaveca_updated_d3adb7_idx` (`updated`);

--
-- Indexes for table `aix_leavecardmodel`
--
ALTER TABLE `aix_leavecardmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_leavecardmodel_entity_id_start_date_3836de8a_uniq` (`entity_id`,`start_date`),
  ADD KEY `aix_leaveca_created_976679_idx` (`created`),
  ADD KEY `aix_leaveca_updated_48cb44_idx` (`updated`),
  ADD KEY `aix_leaveca_start_d_dc0f9f_idx` (`start_date`),
  ADD KEY `aix_leaveca_end_dat_de51fc_idx` (`end_date`);

--
-- Indexes for table `aix_leaverequestactionmodel`
--
ALTER TABLE `aix_leaverequestactionmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_leaverequestactionmodel_entity_id_comment_9b2d938a_uniq` (`entity_id`,`comment`),
  ADD KEY `aix_leaverequestact_leave_request_id_fef91b98_fk_aix_leav` (`leave_request_id`),
  ADD KEY `aix_leaverequestact_leave_request_status_76b20aa4_fk_aix_leav` (`leave_request_status_id`),
  ADD KEY `aix_leavere_created_2cee00_idx` (`created`),
  ADD KEY `aix_leavere_updated_87e753_idx` (`updated`),
  ADD KEY `aix_leavere_comment_d087d3_idx` (`comment`),
  ADD KEY `aix_leaverequestact_employee_id_bc5a2f68_fk_aix_empl` (`employee_id`);

--
-- Indexes for table `aix_leaverequestdetailmodel`
--
ALTER TABLE `aix_leaverequestdetailmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_leaverequestdetailmodel_entity_id_start_date_86e54b08_uniq` (`entity_id`,`start_date`),
  ADD KEY `aix_leavere_created_897c97_idx` (`created`),
  ADD KEY `aix_leavere_updated_9b3444_idx` (`updated`),
  ADD KEY `aix_leavere_start_d_7094f4_idx` (`start_date`),
  ADD KEY `aix_leavere_end_dat_c5d322_idx` (`end_date`);

--
-- Indexes for table `aix_leaverequestmodel`
--
ALTER TABLE `aix_leaverequestmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_leaverequestmodel_entity_id_number_883938a9_uniq` (`entity_id`,`number`),
  ADD KEY `aix_leaverequestmod_leave_request_status_77d49825_fk_aix_leav` (`leave_request_status_id`),
  ADD KEY `aix_leaverequestmod_supervisor_id_8a5caae3_fk_aix_empl` (`supervisor_id`),
  ADD KEY `aix_leavere_created_09ed84_idx` (`created`),
  ADD KEY `aix_leavere_updated_62556f_idx` (`updated`),
  ADD KEY `aix_leavere_number_ba274f_idx` (`number`),
  ADD KEY `aix_leaverequestmod_employee_id_c4d4c3c0_fk_aix_empl` (`employee_id`);

--
-- Indexes for table `aix_leaverequeststatusmodel`
--
ALTER TABLE `aix_leaverequeststatusmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_leaverequeststatusmodel_entity_id_code_1526dc37_uniq` (`entity_id`,`code`),
  ADD KEY `aix_leavere_created_0f3d2e_idx` (`created`),
  ADD KEY `aix_leavere_updated_d628f1_idx` (`updated`),
  ADD KEY `aix_leavere_name_13714a_idx` (`name`);

--
-- Indexes for table `aix_leaverequestworkflowactionmodel`
--
ALTER TABLE `aix_leaverequestworkflowactionmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_leaverequestworkflo_entity_id_name_a424801f_uniq` (`entity_id`,`name`),
  ADD KEY `aix_leavere_created_8c1e0b_idx` (`created`),
  ADD KEY `aix_leavere_updated_277da3_idx` (`updated`),
  ADD KEY `aix_leavere_name_6a4b16_idx` (`name`);

--
-- Indexes for table `aix_leaverequestworkflowmodel`
--
ALTER TABLE `aix_leaverequestworkflowmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_leaverequestworkflo_entity_id_workflow_id_wo_6e005b18_uniq` (`entity_id`,`workflow_id`,`workflow_status_id`,`leave_request_id`),
  ADD KEY `aix_leavere_created_adf88f_idx` (`created`),
  ADD KEY `aix_leavere_updated_77d229_idx` (`updated`);

--
-- Indexes for table `aix_ledgermodel`
--
ALTER TABLE `aix_ledgermodel`
  ADD PRIMARY KEY (`uuid`),
  ADD KEY `aix_ledgerm_entity__626a18_idx` (`entity_id`),
  ADD KEY `aix_ledgerm_entity__b1f18b_idx` (`entity_id`,`posted`),
  ADD KEY `aix_ledgerm_entity__ec4310_idx` (`entity_id`,`locked`);

--
-- Indexes for table `aix_locationmodel`
--
ALTER TABLE `aix_locationmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_locationmodel_entity_id_code_53d959e2_uniq` (`entity_id`,`code`),
  ADD KEY `aix_locatio_created_528612_idx` (`created`),
  ADD KEY `aix_locatio_updated_29d19d_idx` (`updated`),
  ADD KEY `aix_locatio_name_6c6ee7_idx` (`name`);

--
-- Indexes for table `aix_maritalstatusmodel`
--
ALTER TABLE `aix_maritalstatusmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_maritalstatusmodel_entity_id_code_9040b8c6_uniq` (`entity_id`,`code`),
  ADD KEY `aix_marital_created_f59558_idx` (`created`),
  ADD KEY `aix_marital_updated_711b39_idx` (`updated`),
  ADD KEY `aix_marital_name_a6d360_idx` (`name`);

--
-- Indexes for table `aix_nationmodel`
--
ALTER TABLE `aix_nationmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_nationmodel_entity_id_code_deef8744_uniq` (`entity_id`,`code`),
  ADD KEY `aix_nationm_created_c5ae7f_idx` (`created`),
  ADD KEY `aix_nationm_updated_c000b0_idx` (`updated`),
  ADD KEY `aix_nationm_name_56a341_idx` (`name`),
  ADD KEY `aix_nation_descrip_5a8078_idx` (`description`(768));

--
-- Indexes for table `aix_notificationexternaltypemodel`
--
ALTER TABLE `aix_notificationexternaltypemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_notificationexternaltypemodel_entity_id_code_6e65f12b_uniq` (`entity_id`,`code`),
  ADD KEY `aix_notific_created_cf6d33_idx` (`created`),
  ADD KEY `aix_notific_updated_f6fa10_idx` (`updated`),
  ADD KEY `aix_notific_name_49a98c_idx` (`name`);

--
-- Indexes for table `aix_notificationmodel`
--
ALTER TABLE `aix_notificationmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_notificationmodel_entity_id_params_5898a28b_uniq` (`entity_id`,`params`) USING HASH,
  ADD KEY `aix_notific_created_096411_idx` (`created`),
  ADD KEY `aix_notific_updated_616159_idx` (`updated`);

--
-- Indexes for table `aix_notificationtrackermodel`
--
ALTER TABLE `aix_notificationtrackermodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_notificationtracker_entity_id_next_notificat_6b4fe14d_uniq` (`entity_id`,`next_notification`),
  ADD KEY `aix_notific_created_16bb3d_idx` (`created`),
  ADD KEY `aix_notific_updated_172b19_idx` (`updated`);

--
-- Indexes for table `aix_paymentmodemodel`
--
ALTER TABLE `aix_paymentmodemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_paymentmodemodel_entity_id_code_810cbf72_uniq` (`entity_id`,`code`),
  ADD KEY `aix_payment_created_f0763c_idx` (`created`),
  ADD KEY `aix_payment_updated_1d83e9_idx` (`updated`);

--
-- Indexes for table `aix_payrolladvancemodel`
--
ALTER TABLE `aix_payrolladvancemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_payrolladvancemodel_entity_id_period_1c7e8cbf_uniq` (`entity_id`,`period`),
  ADD KEY `aix_payroll_created_5ad9ee_idx` (`created`),
  ADD KEY `aix_payroll_updated_2d0a0e_idx` (`updated`);

--
-- Indexes for table `aix_payrolladvancerequestactionmodel`
--
ALTER TABLE `aix_payrolladvancerequestactionmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_payrolladvancereque_entity_id_comment_7611bb42_uniq` (`entity_id`,`comment`),
  ADD KEY `aix_payrolladvancer_pa_request_id_dcacb0dd_fk_aix_payr` (`pa_request_id`),
  ADD KEY `aix_payrolladvancer_par_status_id_9b0a9fb7_fk_aix_payr` (`par_status_id`),
  ADD KEY `aix_payroll_created_283cf2_idx` (`created`),
  ADD KEY `aix_payroll_updated_9d9890_idx` (`updated`),
  ADD KEY `aix_payroll_comment_e69839_idx` (`comment`),
  ADD KEY `aix_payrolladvancer_employee_id_719747f3_fk_aix_empl` (`employee_id`);

--
-- Indexes for table `aix_payrolladvancerequestdetailmodel`
--
ALTER TABLE `aix_payrolladvancerequestdetailmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_payrolladvancereque_entity_id_period_eb53c540_uniq` (`entity_id`,`period`),
  ADD KEY `aix_payroll_created_0e5a36_idx` (`created`),
  ADD KEY `aix_payroll_updated_1b3c87_idx` (`updated`),
  ADD KEY `aix_payroll_period_850797_idx` (`period`);

--
-- Indexes for table `aix_payrolladvancerequestmodel`
--
ALTER TABLE `aix_payrolladvancerequestmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_payrolladvancerequestmodel_entity_id_number_7c4f70cd_uniq` (`entity_id`,`number`),
  ADD KEY `aix_payrolladvancer_par_status_id_f86b2fba_fk_aix_payr` (`par_status_id`),
  ADD KEY `aix_payrolladvancer_supervisor_id_37d10083_fk_aix_empl` (`supervisor_id`),
  ADD KEY `aix_payroll_created_15a9fc_idx` (`created`),
  ADD KEY `aix_payroll_updated_3b5dfd_idx` (`updated`),
  ADD KEY `aix_payroll_number_afaa24_idx` (`number`),
  ADD KEY `aix_payroll_date_cf395b_idx` (`date`),
  ADD KEY `aix_payrolladvancer_employee_id_a68b50df_fk_aix_empl` (`employee_id`);

--
-- Indexes for table `aix_payrolladvancerequeststatusmodel`
--
ALTER TABLE `aix_payrolladvancerequeststatusmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_payrolladvancereque_entity_id_code_2bcccb14_uniq` (`entity_id`,`code`),
  ADD KEY `aix_payroll_created_26e96e_idx` (`created`),
  ADD KEY `aix_payroll_updated_9acbd8_idx` (`updated`),
  ADD KEY `aix_payroll_name_c9e9ce_idx` (`name`);

--
-- Indexes for table `aix_payrolladvancerequestworkflowactionmodel`
--
ALTER TABLE `aix_payrolladvancerequestworkflowactionmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_payrolladvancereque_entity_id_code_d4397165_uniq` (`entity_id`,`code`),
  ADD KEY `aix_payroll_created_25ece6_idx` (`created`),
  ADD KEY `aix_payroll_updated_143b2f_idx` (`updated`);

--
-- Indexes for table `aix_payrolladvancerequestworkflowmodel`
--
ALTER TABLE `aix_payrolladvancerequestworkflowmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_payrolladvancereque_entity_id_workflow_id_pa_a56eeae8_uniq` (`entity_id`,`workflow_id`,`pa_request_id`),
  ADD KEY `aix_payroll_created_f34e47_idx` (`created`),
  ADD KEY `aix_payroll_updated_a4413b_idx` (`updated`);

--
-- Indexes for table `aix_purchaseordermodel`
--
ALTER TABLE `aix_purchaseordermodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `po_number` (`po_number`),
  ADD UNIQUE KEY `aix_purchaseordermodel_entity_id_po_number_cbd68c88_uniq` (`entity_id`,`po_number`),
  ADD KEY `aix_purchas_entity__44daae_idx` (`entity_id`),
  ADD KEY `aix_purchas_po_stat_a85563_idx` (`po_status`),
  ADD KEY `aix_purchas_ce_mode_615dc4_idx` (`ce_model_id`),
  ADD KEY `aix_purchas_draft_d_c666d4_idx` (`draft_date`),
  ADD KEY `aix_purchas_in_revi_f1f9ea_idx` (`in_review_date`),
  ADD KEY `aix_purchas_approve_fe62bd_idx` (`approved_date`),
  ADD KEY `aix_purchas_fulfill_112808_idx` (`fulfillment_date`),
  ADD KEY `aix_purchas_cancele_6a380e_idx` (`canceled_date`),
  ADD KEY `aix_purchas_void_da_5d25b8_idx` (`void_date`);

--
-- Indexes for table `aix_qualificationmodel`
--
ALTER TABLE `aix_qualificationmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_qualificationmodel_entity_id_code_f973a4cc_uniq` (`entity_id`,`code`),
  ADD KEY `aix_qualifi_created_200562_idx` (`created`),
  ADD KEY `aix_qualifi_updated_3c6296_idx` (`updated`),
  ADD KEY `aix_qualifi_name_6f8556_idx` (`name`);

--
-- Indexes for table `aix_receivedemaildocumentmodel`
--
ALTER TABLE `aix_receivedemaildocumentmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_receivedemaildocumentmodel_entity_id_doc_from_ac682431_uniq` (`entity_id`,`doc_from`) USING HASH,
  ADD KEY `aix_receive_created_a474e3_idx` (`created`),
  ADD KEY `aix_receive_updated_fe0769_idx` (`updated`),
  ADD KEY `aix_receive_doc_fro_98fa39_idx` (`doc_from`(768)),
  ADD KEY `aix_receive_doc_sub_0f9529_idx` (`doc_subject`(768));

--
-- Indexes for table `aix_relationshipmodel`
--
ALTER TABLE `aix_relationshipmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_relationshipmodel_entity_id_code_17657260_uniq` (`entity_id`,`code`),
  ADD KEY `aix_relatio_created_c2fc0a_idx` (`created`),
  ADD KEY `aix_relatio_updated_12d0fb_idx` (`updated`),
  ADD KEY `aix_relatio_name_b2c31e_idx` (`name`);

--
-- Indexes for table `aix_reportmodel`
--
ALTER TABLE `aix_reportmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_reportmodel_entity_id_rpt_name_82f6593c_uniq` (`entity_id`,`rpt_name`),
  ADD KEY `aix_reportm_created_c2ad38_idx` (`created`),
  ADD KEY `aix_reportm_updated_d8c46a_idx` (`updated`);

--
-- Indexes for table `aix_requisitionactionmodel`
--
ALTER TABLE `aix_requisitionactionmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_requisitionactionmodel_entity_id_comment_05261d1f_uniq` (`entity_id`,`comment`),
  ADD KEY `aix_requisitionacti_requisition_id_fb6b8c6d_fk_aix_requ` (`requisition_id`),
  ADD KEY `aix_requisitionacti_requisition_status_i_59f07672_fk_aix_requ` (`requisition_status_id`),
  ADD KEY `aix_requisi_created_d1c76e_idx` (`created`),
  ADD KEY `aix_requisi_updated_dd0e83_idx` (`updated`),
  ADD KEY `aix_requisi_comment_1a5e04_idx` (`comment`),
  ADD KEY `aix_requisitionacti_employee_id_daefa427_fk_aix_empl` (`employee_id`);

--
-- Indexes for table `aix_requisitioncategorymodel`
--
ALTER TABLE `aix_requisitioncategorymodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_requisitioncategorymodel_entity_id_code_fbaa1138_uniq` (`entity_id`,`code`),
  ADD KEY `aix_requisi_created_eaca6f_idx` (`created`),
  ADD KEY `aix_requisi_updated_1e7208_idx` (`updated`),
  ADD KEY `aix_requisi_name_22edaa_idx` (`name`);

--
-- Indexes for table `aix_requisitionflowtypemodel`
--
ALTER TABLE `aix_requisitionflowtypemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_requisitionflowtypemodel_entity_id_code_8c5861a0_uniq` (`entity_id`,`code`),
  ADD KEY `aix_requisi_created_dcda53_idx` (`created`),
  ADD KEY `aix_requisi_updated_152619_idx` (`updated`),
  ADD KEY `aix_requisi_name_a76ff1_idx` (`name`);

--
-- Indexes for table `aix_requisitionmodel`
--
ALTER TABLE `aix_requisitionmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_requisitionmodel_entity_id_date_48bbbcbb_uniq` (`entity_id`,`date`),
  ADD KEY `aix_requisitionmode_requisition_status_i_23a54b37_fk_aix_requ` (`requisition_status_id`),
  ADD KEY `aix_requisitionmode_supervisor_id_c3834490_fk_aix_empl` (`supervisor_id`),
  ADD KEY `aix_requisi_created_3378bb_idx` (`created`),
  ADD KEY `aix_requisi_updated_bf21df_idx` (`updated`),
  ADD KEY `aix_requisitionmode_currency_id_b3ec7191_fk_aix_curr` (`currency_id`),
  ADD KEY `aix_requisitionmode_employee_id_2542c611_fk_aix_empl` (`employee_id`),
  ADD KEY `aix_requisitionmode_requisition_category_40cacbd7_fk_aix_requ` (`requisition_category_id`);

--
-- Indexes for table `aix_requisitionstatusmodel`
--
ALTER TABLE `aix_requisitionstatusmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_requisitionstatusmodel_entity_id_code_86a19524_uniq` (`entity_id`,`code`),
  ADD KEY `aix_requisi_created_2cc4ec_idx` (`created`),
  ADD KEY `aix_requisi_updated_300e1d_idx` (`updated`),
  ADD KEY `aix_requisi_name_9449bd_idx` (`name`);

--
-- Indexes for table `aix_requisitionworkflowactionmodel`
--
ALTER TABLE `aix_requisitionworkflowactionmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_requisitionworkflowactionmodel_entity_id_code_503ea61a_uniq` (`entity_id`,`code`),
  ADD KEY `aix_requisi_created_8a6ef9_idx` (`created`),
  ADD KEY `aix_requisi_updated_76702c_idx` (`updated`);

--
-- Indexes for table `aix_requisitionworkflowmodel`
--
ALTER TABLE `aix_requisitionworkflowmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_requisitionworkflow_entity_id_requisition_id_fae2f68e_uniq` (`entity_id`,`requisition_id`),
  ADD KEY `aix_requisi_created_c7d8ca_idx` (`created`),
  ADD KEY `aix_requisi_updated_62a9ff_idx` (`updated`);

--
-- Indexes for table `aix_routesurveyinfomodel`
--
ALTER TABLE `aix_routesurveyinfomodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_routesurveyinfomodel_entity_id_south_coordina_ba596e02_uniq` (`entity_id`,`south_coordinate`,`east_coordinate`,`route_survey_id`),
  ADD KEY `aix_routesu_created_e96eb5_idx` (`created`),
  ADD KEY `aix_routesu_updated_ff2cb1_idx` (`updated`),
  ADD KEY `aix_routesu_south_c_c5b56f_idx` (`south_coordinate`),
  ADD KEY `aix_routesu_east_co_f2b58a_idx` (`east_coordinate`),
  ADD KEY `aix_routesurveyinfom_route_survey_id_40d6e05b_fk_aix_route` (`route_survey_id`);

--
-- Indexes for table `aix_routesurveymodel`
--
ALTER TABLE `aix_routesurveymodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `name` (`name`),
  ADD UNIQUE KEY `aix_routesurveymodel_entity_id_start_date_end_7adca9c5_uniq` (`entity_id`,`start_date`,`end_date`,`start_place`,`end_place`),
  ADD KEY `aix_routesu_created_4ff5b0_idx` (`created`),
  ADD KEY `aix_routesu_updated_4a8786_idx` (`updated`),
  ADD KEY `aix_routesu_start_g_6bbec2_idx` (`start_gps`),
  ADD KEY `aix_routesu_end_gps_b68e87_idx` (`end_gps`);

--
-- Indexes for table `aix_salarymodel`
--
ALTER TABLE `aix_salarymodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_salarymodel_entity_id_start_date_85c05db8_uniq` (`entity_id`,`start_date`),
  ADD KEY `aix_salarym_created_516904_idx` (`created`),
  ADD KEY `aix_salarym_updated_4c6bcd_idx` (`updated`),
  ADD KEY `aix_salarym_start_d_75d7c0_idx` (`start_date`),
  ADD KEY `aix_salarym_end_dat_9ad987_idx` (`end_date`);

--
-- Indexes for table `aix_skillmodel`
--
ALTER TABLE `aix_skillmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_skillmodel_entity_id_name_1d996734_uniq` (`entity_id`,`name`),
  ADD KEY `aix_skillmo_created_eebfef_idx` (`created`),
  ADD KEY `aix_skillmo_updated_c4f28d_idx` (`updated`);

--
-- Indexes for table `aix_stagedtransactionmodel`
--
ALTER TABLE `aix_stagedtransactionmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `tx_id` (`tx_id`),
  ADD KEY `aix_stagedt_import__38e8f7_idx` (`import_job_id`);

--
-- Indexes for table `aix_taskassigneemodel`
--
ALTER TABLE `aix_taskassigneemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_taskassigneemodel_entity_id_task_id_employ_746b154d_uniq` (`entity_id`,`task_id`,`employee_id`),
  ADD KEY `aix_taskass_created_9bd63d_idx` (`created`),
  ADD KEY `aix_taskass_updated_ab77cd_idx` (`updated`);

--
-- Indexes for table `aix_taskmodel`
--
ALTER TABLE `aix_taskmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_taskmodel_entity_id_task_name_d298b11b_uniq` (`entity_id`,`task_name`),
  ADD KEY `aix_taskmod_created_243c3d_idx` (`created`),
  ADD KEY `aix_taskmod_updated_126208_idx` (`updated`);

--
-- Indexes for table `aix_taskstatusmodel`
--
ALTER TABLE `aix_taskstatusmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_taskstatusmodel_entity_id_code_74834cc2_uniq` (`entity_id`,`code`),
  ADD KEY `aix_tasksta_created_c3b19c_idx` (`created`),
  ADD KEY `aix_tasksta_updated_c2f621_idx` (`updated`);

--
-- Indexes for table `aix_taxmodel`
--
ALTER TABLE `aix_taxmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_taxmodel_entity_id_code_1527c6bf_uniq` (`entity_id`,`code`),
  ADD KEY `aix_taxmode_created_8eec78_idx` (`created`),
  ADD KEY `aix_taxmode_updated_ceaf1f_idx` (`updated`);

--
-- Indexes for table `aix_transactionmodel`
--
ALTER TABLE `aix_transactionmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD KEY `aix_transac_tx_type_c38ffc_idx` (`tx_type`),
  ADD KEY `aix_transac_account_2176ef_idx` (`account_id`),
  ADD KEY `aix_transac_journal_3b6526_idx` (`journal_entry_id`),
  ADD KEY `aix_transac_created_0b6d29_idx` (`created`),
  ADD KEY `aix_transac_updated_d034f9_idx` (`updated`);

--
-- Indexes for table `aix_unitofmeasuremodel`
--
ALTER TABLE `aix_unitofmeasuremodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_unitofmeasuremodel_entity_id_unit_abbr_c74330f9_uniq` (`entity_id`,`unit_abbr`),
  ADD KEY `aix_unitofm_entity__e97572_idx` (`entity_id`);

--
-- Indexes for table `aix_userallocationmodel`
--
ALTER TABLE `aix_userallocationmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_userallocationmodel_entity_id_work_order_id__cb70308a_uniq` (`entity_id`,`work_order_id`,`task_id`),
  ADD KEY `aix_userall_created_bb5f71_idx` (`created`),
  ADD KEY `aix_userall_updated_25fad9_idx` (`updated`),
  ADD KEY `aix_userallocationmodel_allocation_id_09ebd713_fk_auth_user_id` (`allocation_id`),
  ADD KEY `aix_userallocationmodel_work_order_id_303e1f79` (`work_order_id`),
  ADD KEY `aix_userallocationmodel_task_id_b3f2b5e7` (`task_id`);

--
-- Indexes for table `aix_vendormodel`
--
ALTER TABLE `aix_vendormodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_vendormodel_entity_id_vendor_name_537d30e4_uniq` (`entity_id`,`vendor_name`),
  ADD KEY `aix_vendorm_created_06f17a_idx` (`created`),
  ADD KEY `aix_vendorm_updated_b3d6d6_idx` (`updated`),
  ADD KEY `aix_vendorm_active_9b5286_idx` (`active`),
  ADD KEY `aix_vendorm_hidden_3c8f92_idx` (`hidden`);

--
-- Indexes for table `aix_visamodel`
--
ALTER TABLE `aix_visamodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_visamodel_entity_id_visa_number_6148ecf8_uniq` (`entity_id`,`visa_number`),
  ADD KEY `aix_visamod_created_17df5b_idx` (`created`),
  ADD KEY `aix_visamod_updated_2e938c_idx` (`updated`),
  ADD KEY `aix_visamod_visa_nu_6163b4_idx` (`visa_number`);

--
-- Indexes for table `aix_weekendmodel`
--
ALTER TABLE `aix_weekendmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_weekendmodel_entity_id_code_e5e42dc9_uniq` (`entity_id`,`code`),
  ADD KEY `aix_weekend_created_0810a6_idx` (`created`),
  ADD KEY `aix_weekend_updated_3b7ec4_idx` (`updated`),
  ADD KEY `aix_weekend_name_a8065d_idx` (`name`);

--
-- Indexes for table `aix_weeklyemployeemodel`
--
ALTER TABLE `aix_weeklyemployeemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_weeklyemployeemodel_entity_id_employee_id_3c8fa7ca_uniq` (`entity_id`,`employee_id`),
  ADD KEY `aix_weeklye_created_bc3d1b_idx` (`created`),
  ADD KEY `aix_weeklye_updated_62346e_idx` (`updated`);

--
-- Indexes for table `aix_weeklyemployeeprocessedmodel`
--
ALTER TABLE `aix_weeklyemployeeprocessedmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_weeklyemployeeproce_entity_id_employee_id_800a0f87_uniq` (`entity_id`,`employee_id`),
  ADD KEY `aix_weeklye_created_c3ec00_idx` (`created`),
  ADD KEY `aix_weeklye_updated_52be4d_idx` (`updated`);

--
-- Indexes for table `aix_workcategorymodel`
--
ALTER TABLE `aix_workcategorymodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_workcategorymodel_entity_id_code_b81c6619_uniq` (`entity_id`,`code`),
  ADD KEY `aix_workcat_created_48a75c_idx` (`created`),
  ADD KEY `aix_workcat_updated_ab42de_idx` (`updated`),
  ADD KEY `aix_workcat_name_b07c67_idx` (`name`),
  ADD KEY `aix_workca_descrip_3a39d0_idx` (`description`(768));

--
-- Indexes for table `aix_workflowactionmodel`
--
ALTER TABLE `aix_workflowactionmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_workflowactionmodel_entity_id_title_cdcbc11c_uniq` (`entity_id`,`title`) USING HASH,
  ADD KEY `aix_workflo_created_1c2dd4_idx` (`created`),
  ADD KEY `aix_workflo_updated_a3b8ea_idx` (`updated`),
  ADD KEY `aix_workflo_title_dbe4bb_idx` (`title`(768));

--
-- Indexes for table `aix_workflowactiontypemodel`
--
ALTER TABLE `aix_workflowactiontypemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_workflowactiontypemodel_entity_id_code_0cbd8101_uniq` (`entity_id`,`code`),
  ADD KEY `aix_workflo_created_a6c382_idx` (`created`),
  ADD KEY `aix_workflo_updated_bbd036_idx` (`updated`),
  ADD KEY `aix_workflo_name_724ce0_idx` (`name`);

--
-- Indexes for table `aix_workflowmodel`
--
ALTER TABLE `aix_workflowmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_workflowmodel_entity_id_version_ce42854f_uniq` (`entity_id`,`version`),
  ADD KEY `aix_workflo_created_9f4214_idx` (`created`),
  ADD KEY `aix_workflo_updated_5a364a_idx` (`updated`),
  ADD KEY `aix_workflo_version_3b6a92_idx` (`version`);

--
-- Indexes for table `aix_workflowstatusmodel`
--
ALTER TABLE `aix_workflowstatusmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_workflowstatusmodel_entity_id_title_0bb7a129_uniq` (`entity_id`,`title`) USING HASH,
  ADD KEY `aix_workflo_created_11f0f2_idx` (`created`),
  ADD KEY `aix_workflo_updated_69e6d2_idx` (`updated`),
  ADD KEY `aix_workflo_title_49bb9c_idx` (`title`(768)),
  ADD KEY `aix_workfl_descrip_825c90_idx` (`description`(768));

--
-- Indexes for table `aix_workflowtypemodel`
--
ALTER TABLE `aix_workflowtypemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_workflowtypemodel_entity_id_code_0784227c_uniq` (`entity_id`,`code`),
  ADD KEY `aix_workflo_created_bc83c4_idx` (`created`),
  ADD KEY `aix_workflo_updated_9ab026_idx` (`updated`),
  ADD KEY `aix_workflo_name_ed88b9_idx` (`name`);

--
-- Indexes for table `aix_workorderactivityassetmodel`
--
ALTER TABLE `aix_workorderactivityassetmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_workorderactivityass_entity_id_start_date_end_deff37c6_uniq` (`entity_id`,`start_date`,`end_date`,`activity_id`,`asset_id`),
  ADD KEY `aix_workord_start_d_16812d_idx` (`start_date`),
  ADD KEY `aix_workord_end_dat_79c848_idx` (`end_date`),
  ADD KEY `aix_workord_status_9a703e_idx` (`status`),
  ADD KEY `aix_workorderactivit_activity_id_f693742d_fk_aix_worko` (`activity_id`),
  ADD KEY `aix_workorderactivit_asset_id_2acfc5a3_fk_aix_asset` (`asset_id`);

--
-- Indexes for table `aix_workorderactivitydocumentmodel`
--
ALTER TABLE `aix_workorderactivitydocumentmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_workorderactivitydoc_entity_id_doc_date_activ_3e3b7cf5_uniq` (`entity_id`,`doc_date`,`activity_id`,`document_id`,`status`),
  ADD KEY `aix_workorderactivit_activity_id_8f6f374e_fk_aix_worko` (`activity_id`),
  ADD KEY `aix_workorderactivit_document_id_68318321_fk_aix_docum` (`document_id`),
  ADD KEY `aix_workord_doc_dat_adb9d6_idx` (`doc_date`),
  ADD KEY `aix_workord_descrip_4371e3_idx` (`description`(768)),
  ADD KEY `aix_workord_status_2caead_idx` (`status`);

--
-- Indexes for table `aix_workorderactivityliftingmodel`
--
ALTER TABLE `aix_workorderactivityliftingmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_workorderactivitylif_entity_id_activity_id_tr_07f22d94_uniq` (`entity_id`,`activity_id`,`trip_code`,`operator_id`,`equipment_id`),
  ADD KEY `aix_workorderactivit_activity_id_b3983fdf_fk_aix_worko` (`activity_id`),
  ADD KEY `aix_workorderactivit_equipment_id_79c9b8d1_fk_aix_asset` (`equipment_id`),
  ADD KEY `aix_workorderactivit_FromLocation_56e819c7_fk_aix_custo` (`FromLocation`),
  ADD KEY `aix_workorderactivit_operator_id_7269b65f_fk_aix_emplo` (`operator_id`),
  ADD KEY `aix_workorderactivit_supervisor_id_7a8eb3fa_fk_aix_emplo` (`supervisor_id`),
  ADD KEY `aix_workorderactivit_ToLocation_65cf694a_fk_aix_custo` (`ToLocation`),
  ADD KEY `aix_workord_trip_co_e78ae8_idx` (`trip_code`),
  ADD KEY `aix_workord_comment_0d85ad_idx` (`comments`(768)),
  ADD KEY `aix_workord_status_69d1b5_idx` (`status`);

--
-- Indexes for table `aix_workorderactivityliftingmodel_operators`
--
ALTER TABLE `aix_workorderactivityliftingmodel_operators`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `aix_workorderactivitylif_workorderactivitylifting_05146b18_uniq` (`workorderactivityliftingmodel_id`,`employeemodel_id`),
  ADD KEY `aix_workorderactivit_employeemodel_id_5a62d27e_fk_aix_emplo` (`employeemodel_id`);

--
-- Indexes for table `aix_workorderactivitymodel`
--
ALTER TABLE `aix_workorderactivitymodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `code` (`code`),
  ADD UNIQUE KEY `aix_workorderactivitymod_entity_id_activity_date__4cb1c06b_uniq` (`entity_id`,`activity_date`,`FromLocation`,`ToLocation`,`task_id`),
  ADD KEY `aix_workord_activit_5db10b_idx` (`activity_date`),
  ADD KEY `aix_workord_activit_bf3976_idx` (`activity_description`(768)),
  ADD KEY `aix_workord_comment_87cf9b_idx` (`comments`),
  ADD KEY `aix_workord_status_b3a933_idx` (`status`),
  ADD KEY `aix_workorderactivit_FromLocation_23df7c2f_fk_aix_custo` (`FromLocation`),
  ADD KEY `aix_workorderactivit_task_id_c6049b12_fk_aix_worko` (`task_id`),
  ADD KEY `aix_workorderactivit_ToLocation_b30bd43f_fk_aix_custo` (`ToLocation`);

--
-- Indexes for table `aix_workorderactivitypersonnelmodel`
--
ALTER TABLE `aix_workorderactivitypersonnelmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_workorderactivityper_entity_id_start_date_end_76698f61_uniq` (`entity_id`,`start_date`,`end_date`,`activity_id`,`employee_id`),
  ADD KEY `aix_workord_start_d_da91ca_idx` (`start_date`),
  ADD KEY `aix_workord_end_dat_97b4ae_idx` (`end_date`),
  ADD KEY `aix_workord_status_1e4382_idx` (`status`),
  ADD KEY `aix_workorderactivit_activity_id_10f5727a_fk_aix_worko` (`activity_id`),
  ADD KEY `aix_workorderactivit_employee_id_99cddfb1_fk_aix_emplo` (`employee_id`);

--
-- Indexes for table `aix_workorderactivitytransportmodel`
--
ALTER TABLE `aix_workorderactivitytransportmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_workorderactivitytra_entity_id_activity_id_tr_e991dada_uniq` (`entity_id`,`activity_id`,`trip_code`,`driver_id`,`vehicle_id`),
  ADD KEY `aix_workorderactivit_activity_id_03e2ce19_fk_aix_worko` (`activity_id`),
  ADD KEY `aix_workorderactivit_driver_id_6cb0184a_fk_aix_emplo` (`driver_id`),
  ADD KEY `aix_workorderactivit_FromLocation_ad626162_fk_aix_custo` (`FromLocation`),
  ADD KEY `aix_workorderactivit_ToLocation_9695cc9c_fk_aix_custo` (`ToLocation`),
  ADD KEY `aix_workorderactivit_vehicle_id_0c2bb572_fk_aix_asset` (`vehicle_id`),
  ADD KEY `aix_workord_trip_co_ef770b_idx` (`trip_code`),
  ADD KEY `aix_workord_comment_20a9bc_idx` (`comments`(768)),
  ADD KEY `aix_workord_status_abfaaa_idx` (`status`);

--
-- Indexes for table `aix_workorderactivitytransportmodel_assistants`
--
ALTER TABLE `aix_workorderactivitytransportmodel_assistants`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `aix_workorderactivitytra_workorderactivitytranspo_61a620ea_uniq` (`workorderactivitytransportmodel_id`,`employeemodel_id`),
  ADD KEY `aix_workorderactivit_employeemodel_id_3904677d_fk_aix_emplo` (`employeemodel_id`);

--
-- Indexes for table `aix_workorderassetmodel`
--
ALTER TABLE `aix_workorderassetmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_workorderassetmodel_entity_id_startDate_endD_8a9fb630_uniq` (`entity_id`,`startDate`,`endDate`,`work_order_id`,`asset_id`),
  ADD KEY `aix_workord_startDa_45dd56_idx` (`startDate`),
  ADD KEY `aix_workord_endDate_af05e6_idx` (`endDate`),
  ADD KEY `aix_workord_status_11167b_idx` (`status`),
  ADD KEY `aix_workor_descrip_5790ff_idx` (`description`),
  ADD KEY `aix_workorderassetm_asset_id_2b2d5ce0_fk_aix_asse` (`asset_id`),
  ADD KEY `aix_workorderassetm_work_order_id_816a8972_fk_aix_work` (`work_order_id`);

--
-- Indexes for table `aix_workorderjobcardmodel`
--
ALTER TABLE `aix_workorderjobcardmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `jcd_number` (`jcd_number`),
  ADD UNIQUE KEY `aix_workorderjobcardmodel_entity_id_jcd_number_afb393a9_uniq` (`entity_id`,`jcd_number`),
  ADD KEY `aix_workorderjobcar_work_order_id_f4bb71eb_fk_aix_work` (`work_order_id`),
  ADD KEY `aix_workord_entity__bc66a9_idx` (`entity_id`),
  ADD KEY `aix_workord_jcd_sta_7cc680_idx` (`jcd_status`),
  ADD KEY `aix_workord_draft_d_c328f3_idx` (`draft_date`),
  ADD KEY `aix_workord_in_revi_f78062_idx` (`in_review_date`),
  ADD KEY `aix_workord_approve_aaec43_idx` (`approved_date`),
  ADD KEY `aix_workord_fulfill_cd2507_idx` (`fulfillment_date`),
  ADD KEY `aix_workord_cancele_8a1ab7_idx` (`canceled_date`),
  ADD KEY `aix_workord_void_da_11fd67_idx` (`void_date`),
  ADD KEY `aix_workorderjobcar_handler_id_26c54de0_fk_aix_empl` (`handler_id`);

--
-- Indexes for table `aix_workorderjobcardstatusmodel`
--
ALTER TABLE `aix_workorderjobcardstatusmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_workorderjobcardstatusmodel_entity_id_code_a2eea103_uniq` (`entity_id`,`code`),
  ADD KEY `aix_workord_created_e1f5d6_idx` (`created`),
  ADD KEY `aix_workord_updated_50f186_idx` (`updated`),
  ADD KEY `aix_workord_code_59cb32_idx` (`code`),
  ADD KEY `aix_workor_descrip_7c8bee_idx` (`description`(768)),
  ADD KEY `aix_workorderjobcar_jobcard_id_f997ba50_fk_aix_work` (`jobcard_id`),
  ADD KEY `aix_workorderjobcar_status_id_c402eeaa_fk_aix_work` (`status_id`);

--
-- Indexes for table `aix_workordermodel`
--
ALTER TABLE `aix_workordermodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `order_no` (`order_no`),
  ADD UNIQUE KEY `aix_workordermodel_entity_id_order_no_4e30516e_uniq` (`entity_id`,`order_no`),
  ADD KEY `aix_workordermodel_wo_type_id_09952eeb_fk_aix_work` (`wo_type_id`),
  ADD KEY `aix_workord_created_3cd4f2_idx` (`created`),
  ADD KEY `aix_workord_updated_f263f7_idx` (`updated`),
  ADD KEY `aix_workord_is_acti_0b6506_idx` (`is_active`),
  ADD KEY `aix_workordermodel_category_id_ca4c793e_fk_aix_work` (`category_id`),
  ADD KEY `aix_workordermodel_currency_id_641e96f1_fk_aix_curr` (`currency_id`),
  ADD KEY `aix_workordermodel_customer_id_e14465c4_fk_aix_cust` (`customer_id`);

--
-- Indexes for table `aix_workorderpersonnelmodel`
--
ALTER TABLE `aix_workorderpersonnelmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_workorderpersonnelm_entity_id_startDate_endD_5ed748f3_uniq` (`entity_id`,`startDate`,`endDate`,`work_order_id`,`employee_id`),
  ADD KEY `aix_workord_startDa_f14e1c_idx` (`startDate`),
  ADD KEY `aix_workord_endDate_b7d62d_idx` (`endDate`),
  ADD KEY `aix_workord_status_7999fe_idx` (`status`),
  ADD KEY `aix_workord_woStatu_722877_idx` (`woStatus`),
  ADD KEY `aix_workorderperson_employee_id_4d47f560_fk_aix_empl` (`employee_id`),
  ADD KEY `aix_workorderperson_work_order_id_4316f4eb_fk_aix_work` (`work_order_id`);

--
-- Indexes for table `aix_workorderstatusmodel`
--
ALTER TABLE `aix_workorderstatusmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_workorderstatusmodel_entity_id_code_c9fb99ec_uniq` (`entity_id`,`code`),
  ADD KEY `aix_workord_created_127857_idx` (`created`),
  ADD KEY `aix_workord_updated_e83d03_idx` (`updated`),
  ADD KEY `aix_workord_name_856f32_idx` (`name`),
  ADD KEY `aix_workor_descrip_60c91b_idx` (`description`(768));

--
-- Indexes for table `aix_workordertaskassetmodel`
--
ALTER TABLE `aix_workordertaskassetmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_workordertaskassetm_entity_id_startDate_endD_89cc2adf_uniq` (`entity_id`,`startDate`,`endDate`,`task_id`,`asset_id`),
  ADD KEY `aix_workord_startDa_38b6f3_idx` (`startDate`),
  ADD KEY `aix_workord_endDate_e7eeec_idx` (`endDate`),
  ADD KEY `aix_workord_status_9bc75c_idx` (`status`),
  ADD KEY `aix_workor_descrip_1dc1ea_idx` (`description`(768)),
  ADD KEY `aix_workordertaskas_asset_id_6d2b8a28_fk_aix_asse` (`asset_id`),
  ADD KEY `aix_workordertaskas_task_id_0ebf9eec_fk_aix_work` (`task_id`);

--
-- Indexes for table `aix_workordertaskmodel`
--
ALTER TABLE `aix_workordertaskmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_workordertaskmodel_entity_id_startDate_endD_a88ad8b6_uniq` (`entity_id`,`startDate`,`endDate`,`work_order_id`,`StartLocation`,`EndLocation`),
  ADD KEY `aix_workord_startDa_4abbd7_idx` (`startDate`),
  ADD KEY `aix_workord_endDate_00e053_idx` (`endDate`),
  ADD KEY `aix_workord_current_651ce9_idx` (`currentStatus`),
  ADD KEY `aix_workor_descrip_08a970_idx` (`description`),
  ADD KEY `aix_workordertaskmo_EndLocation_78739987_fk_aix_cust` (`EndLocation`),
  ADD KEY `aix_workordertaskmo_StartLocation_3578751f_fk_aix_cust` (`StartLocation`),
  ADD KEY `aix_workordertaskmo_work_order_id_1aeef779_fk_aix_work` (`work_order_id`);

--
-- Indexes for table `aix_workordertaskpersonnelmodel`
--
ALTER TABLE `aix_workordertaskpersonnelmodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_workordertaskperson_entity_id_startDate_endD_0165b383_uniq` (`entity_id`,`startDate`,`endDate`,`task_id`,`employee_id`),
  ADD KEY `aix_workord_startDa_481899_idx` (`startDate`),
  ADD KEY `aix_workord_endDate_2a25b2_idx` (`endDate`),
  ADD KEY `aix_workor_duties_9da298_idx` (`duties`(768)),
  ADD KEY `aix_workord_status_45d32f_idx` (`status`),
  ADD KEY `aix_workordertaskpe_employee_id_f84adda6_fk_aix_empl` (`employee_id`),
  ADD KEY `aix_workordertaskpe_task_id_b8caebad_fk_aix_work` (`task_id`);

--
-- Indexes for table `aix_workordertypemodel`
--
ALTER TABLE `aix_workordertypemodel`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `aix_workordertypemodel_entity_id_code_f34fcde4_uniq` (`entity_id`,`code`),
  ADD KEY `aix_workord_created_4ade1a_idx` (`created`),
  ADD KEY `aix_workord_updated_c0972a_idx` (`updated`),
  ADD KEY `aix_workord_name_074da2_idx` (`name`),
  ADD KEY `aix_workor_descrip_b4eeca_idx` (`description`(768));

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `aix_workorderactivityliftingmodel_operators`
--
ALTER TABLE `aix_workorderactivityliftingmodel_operators`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `aix_workorderactivitytransportmodel_assistants`
--
ALTER TABLE `aix_workorderactivitytransportmodel_assistants`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1621;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=641;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=161;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=93;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `aix_absencetypemodel`
--
ALTER TABLE `aix_absencetypemodel`
  ADD CONSTRAINT `aix_absencetypemode_entity_id_fc5c9cc4_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_accountmodel`
--
ALTER TABLE `aix_accountmodel`
  ADD CONSTRAINT `aix_accountmodel_coa_id_125ddb81_fk_aix_char` FOREIGN KEY (`coa_id`) REFERENCES `aix_chartofaccountmodel` (`uuid`),
  ADD CONSTRAINT `aix_accountmodel_parent_id_4929e17a_fk_aix_accountmodel_uuid` FOREIGN KEY (`parent_id`) REFERENCES `aix_accountmodel` (`uuid`);

--
-- Constraints for table `aix_aixitshandovermodel`
--
ALTER TABLE `aix_aixitshandovermodel`
  ADD CONSTRAINT `aix_aixitshandovermo_entity_id_76e1b6a0_fk_aix_entit` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_aixitshandovermo_equipment_id_6d36ca1c_fk_aix_equip` FOREIGN KEY (`equipment_id`) REFERENCES `aix_equipmentmodel` (`uuid`),
  ADD CONSTRAINT `aix_aixitshandovermo_staff_id_f112c157_fk_aix_emplo` FOREIGN KEY (`staff_id`) REFERENCES `aix_employeemodel` (`uuid`);

--
-- Constraints for table `aix_aixitsstatusreportmodel`
--
ALTER TABLE `aix_aixitsstatusreportmodel`
  ADD CONSTRAINT `aix_aixitsstatusrepo_entity_id_132bb1a1_fk_aix_entit` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_assetmodel`
--
ALTER TABLE `aix_assetmodel`
  ADD CONSTRAINT `aix_assetmodel_entity_id_59b7c1f1_fk_aix_entitymodel_uuid` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_benefitcalculationmodel`
--
ALTER TABLE `aix_benefitcalculationmodel`
  ADD CONSTRAINT `aix_benefitcalculat_entity_id_6b07b4a6_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_benefittypemodel`
--
ALTER TABLE `aix_benefittypemodel`
  ADD CONSTRAINT `aix_benefittypemode_benefit_calculation__fb16578d_fk_aix_bene` FOREIGN KEY (`benefit_calculation_id`) REFERENCES `aix_benefitcalculationmodel` (`uuid`),
  ADD CONSTRAINT `aix_benefittypemode_entity_id_8ddcbf0e_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_billmodel`
--
ALTER TABLE `aix_billmodel`
  ADD CONSTRAINT `aix_billmodel_cash_account_id_e1d96aab_fk_aix_acco` FOREIGN KEY (`cash_account_id`) REFERENCES `aix_accountmodel` (`uuid`),
  ADD CONSTRAINT `aix_billmodel_ce_model_id_2e73c454_fk_aix_estimatemodel_uuid` FOREIGN KEY (`ce_model_id`) REFERENCES `aix_estimatemodel` (`uuid`),
  ADD CONSTRAINT `aix_billmodel_ledger_id_bfa54e35_fk_aix_ledgermodel_uuid` FOREIGN KEY (`ledger_id`) REFERENCES `aix_ledgermodel` (`uuid`),
  ADD CONSTRAINT `aix_billmodel_prepaid_account_id_ddbdbaf5_fk_aix_acco` FOREIGN KEY (`prepaid_account_id`) REFERENCES `aix_accountmodel` (`uuid`),
  ADD CONSTRAINT `aix_billmodel_unearned_account_id_5df5b095_fk_aix_acco` FOREIGN KEY (`unearned_account_id`) REFERENCES `aix_accountmodel` (`uuid`),
  ADD CONSTRAINT `aix_billmodel_vendor_id_cfe631d6_fk_aix_vendormodel_uuid` FOREIGN KEY (`vendor_id`) REFERENCES `aix_vendormodel` (`uuid`);

--
-- Constraints for table `aix_businessindustrymodel`
--
ALTER TABLE `aix_businessindustrymodel`
  ADD CONSTRAINT `aix_businessindustr_entity_id_a7a688c3_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_currencymodel`
--
ALTER TABLE `aix_currencymodel`
  ADD CONSTRAINT `aix_currencymodel_entity_id_3627daeb_fk_aix_entitymodel_uuid` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_customerlocationmodel`
--
ALTER TABLE `aix_customerlocationmodel`
  ADD CONSTRAINT `aix_customerlocatio_customer_id_7eeea5d6_fk_aix_cust` FOREIGN KEY (`customer_id`) REFERENCES `aix_customermodel` (`uuid`),
  ADD CONSTRAINT `aix_customerlocatio_entity_id_2f7f60a0_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_customermodel`
--
ALTER TABLE `aix_customermodel`
  ADD CONSTRAINT `aix_customermodel_business_industry_id_f3b16fa8_fk_aix_busi` FOREIGN KEY (`business_industry_id`) REFERENCES `aix_businessindustrymodel` (`uuid`),
  ADD CONSTRAINT `aix_customermodel_entity_id_dc7346bb_fk_aix_entitymodel_uuid` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_customermodel_nation_id_3c09bdeb_fk_aix_nationmodel_uuid` FOREIGN KEY (`nation_id`) REFERENCES `aix_nationmodel` (`uuid`),
  ADD CONSTRAINT `aix_customermodel_user_id_18efdba9_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `aix_departmentmodel`
--
ALTER TABLE `aix_departmentmodel`
  ADD CONSTRAINT `aix_departmentmodel_entity_id_96bdf006_fk_aix_entitymodel_uuid` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_documentmodel`
--
ALTER TABLE `aix_documentmodel`
  ADD CONSTRAINT `aix_documentmodel_activity_id_a24cd5e5_fk_aix_worko` FOREIGN KEY (`activity_id`) REFERENCES `aix_workorderactivitymodel` (`uuid`),
  ADD CONSTRAINT `aix_documentmodel_task_id_95a39bc6_fk_aix_worko` FOREIGN KEY (`task_id`) REFERENCES `aix_workordertaskmodel` (`uuid`),
  ADD CONSTRAINT `aix_documentmodel_work_order_id_90fdd9f1_fk_aix_worko` FOREIGN KEY (`work_order_id`) REFERENCES `aix_workordermodel` (`uuid`);

--
-- Constraints for table `aix_employeefawmodel`
--
ALTER TABLE `aix_employeefawmodel`
  ADD CONSTRAINT `aix_employeefawmodel_entity_id_658689b0_fk_aix_entitymodel_uuid` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_employeefawmodel_location_id_83a8c5e2_fk_aix_custo` FOREIGN KEY (`location_id`) REFERENCES `aix_customerlocationmodel` (`uuid`),
  ADD CONSTRAINT `aix_employeefawmodel_work_order_id_2d3fb326_fk_aix_worko` FOREIGN KEY (`work_order_id`) REFERENCES `aix_workordermodel` (`uuid`);

--
-- Constraints for table `aix_employeemodel`
--
ALTER TABLE `aix_employeemodel`
  ADD CONSTRAINT `aix_employeemodel_department_id_0bd1eb92_fk_aix_depa` FOREIGN KEY (`department_id`) REFERENCES `aix_departmentmodel` (`uuid`),
  ADD CONSTRAINT `aix_employeemodel_entity_id_d55a967c_fk_aix_entitymodel_uuid` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_employeemodel_username_id_71f6c345_fk_auth_user_id` FOREIGN KEY (`username_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `aix_entitymanagementmodel`
--
ALTER TABLE `aix_entitymanagementmodel`
  ADD CONSTRAINT `aix_entitymanagemen_entity_id_0e540e71_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_entitymanagementmodel_user_id_092f7ab3_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `aix_entitymodel`
--
ALTER TABLE `aix_entitymodel`
  ADD CONSTRAINT `aix_entitymodel_admin_id_c16d0b98_fk_auth_user_id` FOREIGN KEY (`admin_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `aix_entityunitmodel`
--
ALTER TABLE `aix_entityunitmodel`
  ADD CONSTRAINT `aix_entityunitmodel_entity_id_228c815d_fk_aix_entitymodel_uuid` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_entityunitmodel_parent_id_57347d13_fk_aix_enti` FOREIGN KEY (`parent_id`) REFERENCES `aix_entityunitmodel` (`uuid`);

--
-- Constraints for table `aix_equipmentassignmentmodel`
--
ALTER TABLE `aix_equipmentassignmentmodel`
  ADD CONSTRAINT `aix_equipmentassignm_entity_id_b6e63528_fk_aix_entit` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_equipmentassignm_equipment_id_502d5060_fk_aix_equip` FOREIGN KEY (`equipment_id`) REFERENCES `aix_equipmentmodel` (`uuid`),
  ADD CONSTRAINT `aix_equipmentassignm_operator_id_5eb92ab8_fk_aix_emplo` FOREIGN KEY (`operator_id`) REFERENCES `aix_employeemodel` (`uuid`);

--
-- Constraints for table `aix_equipmentaxlemodel`
--
ALTER TABLE `aix_equipmentaxlemodel`
  ADD CONSTRAINT `aix_equipmentaxlemod_entity_id_69e0df82_fk_aix_entit` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_equipmentfetmodel`
--
ALTER TABLE `aix_equipmentfetmodel`
  ADD CONSTRAINT `aix_equipmentfetmode_location_id_273d8eec_fk_aix_custo` FOREIGN KEY (`location_id`) REFERENCES `aix_customerlocationmodel` (`uuid`),
  ADD CONSTRAINT `aix_equipmentfetmode_work_order_id_c82a8661_fk_aix_worko` FOREIGN KEY (`work_order_id`) REFERENCES `aix_workordermodel` (`uuid`),
  ADD CONSTRAINT `aix_equipmentfetmodel_entity_id_3f7822d9_fk_aix_entitymodel_uuid` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_equipmentfuelmodel`
--
ALTER TABLE `aix_equipmentfuelmodel`
  ADD CONSTRAINT `aix_equipmentfuelmod_EndLocation_58ee9edd_fk_aix_custo` FOREIGN KEY (`EndLocation`) REFERENCES `aix_customerlocationmodel` (`uuid`),
  ADD CONSTRAINT `aix_equipmentfuelmod_StartLocation_852f7a38_fk_aix_custo` FOREIGN KEY (`StartLocation`) REFERENCES `aix_customerlocationmodel` (`uuid`),
  ADD CONSTRAINT `aix_equipmentfuelmod_entity_id_e530c9c5_fk_aix_entit` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_equipmentfuelmod_equipment_id_1dd6c111_fk_aix_equip` FOREIGN KEY (`equipment_id`) REFERENCES `aix_equipmentmodel` (`uuid`),
  ADD CONSTRAINT `aix_equipmentfuelmod_fuel_reciept_id_a961ac4e_fk_aix_docum` FOREIGN KEY (`fuel_reciept_id`) REFERENCES `aix_documentmodel` (`uuid`),
  ADD CONSTRAINT `aix_equipmentfuelmod_work_order_id_569313e4_fk_aix_worko` FOREIGN KEY (`work_order_id`) REFERENCES `aix_workordermodel` (`uuid`);

--
-- Constraints for table `aix_equipmenthandovermodel`
--
ALTER TABLE `aix_equipmenthandovermodel`
  ADD CONSTRAINT `aix_equipmenthandove_approved_by_hr_id_ba311600_fk_aix_emplo` FOREIGN KEY (`approved_by_hr_id`) REFERENCES `aix_employeemodel` (`uuid`),
  ADD CONSTRAINT `aix_equipmenthandove_approved_by_ict_id_2e172361_fk_aix_emplo` FOREIGN KEY (`approved_by_ict_id`) REFERENCES `aix_employeemodel` (`uuid`),
  ADD CONSTRAINT `aix_equipmenthandove_entity_id_6a993747_fk_aix_entit` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_equipmenthandove_equipment_id_d3541d1c_fk_aix_equip` FOREIGN KEY (`equipment_id`) REFERENCES `aix_equipmentmodel` (`uuid`),
  ADD CONSTRAINT `aix_equipmenthandove_handover_by_id_51a6270d_fk_aix_emplo` FOREIGN KEY (`handover_by_id`) REFERENCES `aix_employeemodel` (`uuid`),
  ADD CONSTRAINT `aix_equipmenthandove_location_id_aa906c11_fk_aix_custo` FOREIGN KEY (`location_id`) REFERENCES `aix_customerlocationmodel` (`uuid`),
  ADD CONSTRAINT `aix_equipmenthandove_received_by_id_760d21ec_fk_aix_emplo` FOREIGN KEY (`received_by_id`) REFERENCES `aix_employeemodel` (`uuid`);

--
-- Constraints for table `aix_equipmentjoinmodel`
--
ALTER TABLE `aix_equipmentjoinmodel`
  ADD CONSTRAINT `aix_equipmentjoinmod_entity_id_1f9e7352_fk_aix_entit` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_equipmentjoinmod_eq_primary_id_c34d2cea_fk_aix_equip` FOREIGN KEY (`eq_primary_id`) REFERENCES `aix_equipmentmodel` (`uuid`),
  ADD CONSTRAINT `aix_equipmentjoinmod_eq_secondary_id_78d06edc_fk_aix_equip` FOREIGN KEY (`eq_secondary_id`) REFERENCES `aix_equipmentmodel` (`uuid`);

--
-- Constraints for table `aix_equipmentmanufacturermodel`
--
ALTER TABLE `aix_equipmentmanufacturermodel`
  ADD CONSTRAINT `aix_equipmentmanufac_entity_id_66450ecd_fk_aix_entit` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_equipmentmodel`
--
ALTER TABLE `aix_equipmentmodel`
  ADD CONSTRAINT `aix_equipmentmodel_asset_id_fec36e0e_fk_aix_assetmodel_uuid` FOREIGN KEY (`asset_id`) REFERENCES `aix_assetmodel` (`uuid`),
  ADD CONSTRAINT `aix_equipmentmodel_entity_id_98187a80_fk_aix_entitymodel_uuid` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_equipmentmodel_eq_manufacturer_id_d3ae55a5_fk_aix_equip` FOREIGN KEY (`eq_manufacturer_id`) REFERENCES `aix_equipmentmanufacturermodel` (`uuid`),
  ADD CONSTRAINT `aix_equipmentmodel_eq_type_id_f20ea336_fk_aix_equip` FOREIGN KEY (`eq_type_id`) REFERENCES `aix_equipmenttypemodel` (`uuid`);

--
-- Constraints for table `aix_equipmenttypemodel`
--
ALTER TABLE `aix_equipmenttypemodel`
  ADD CONSTRAINT `aix_equipmenttypemod_entity_id_ca1f67a0_fk_aix_entit` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_estimatemodel`
--
ALTER TABLE `aix_estimatemodel`
  ADD CONSTRAINT `aix_estimatemodel_customer_id_b4a0331a_fk_aix_cust` FOREIGN KEY (`customer_id`) REFERENCES `aix_customermodel` (`uuid`),
  ADD CONSTRAINT `aix_estimatemodel_entity_id_42cfcfe5_fk_aix_entitymodel_uuid` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_immigrationdetailmodel`
--
ALTER TABLE `aix_immigrationdetailmodel`
  ADD CONSTRAINT `aix_immigrationdeta_employee_id_825e8e30_fk_aix_empl` FOREIGN KEY (`employee_id`) REFERENCES `aix_employeemodel` (`uuid`),
  ADD CONSTRAINT `aix_immigrationdeta_entity_id_03463698_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_importjobmodel`
--
ALTER TABLE `aix_importjobmodel`
  ADD CONSTRAINT `aix_importjobmodel_ledger_id_316cad29_fk_aix_ledgermodel_uuid` FOREIGN KEY (`ledger_id`) REFERENCES `aix_ledgermodel` (`uuid`);

--
-- Constraints for table `aix_invoicemodel`
--
ALTER TABLE `aix_invoicemodel`
  ADD CONSTRAINT `aix_invoicemodel_cash_account_id_464cb43f_fk_aix_acco` FOREIGN KEY (`cash_account_id`) REFERENCES `aix_accountmodel` (`uuid`),
  ADD CONSTRAINT `aix_invoicemodel_ce_model_id_9e913a14_fk_aix_esti` FOREIGN KEY (`ce_model_id`) REFERENCES `aix_estimatemodel` (`uuid`),
  ADD CONSTRAINT `aix_invoicemodel_customer_id_22ca565c_fk_aix_cust` FOREIGN KEY (`customer_id`) REFERENCES `aix_customermodel` (`uuid`),
  ADD CONSTRAINT `aix_invoicemodel_ledger_id_a6ec5856_fk_aix_ledgermodel_uuid` FOREIGN KEY (`ledger_id`) REFERENCES `aix_ledgermodel` (`uuid`),
  ADD CONSTRAINT `aix_invoicemodel_prepaid_account_id_6ff9e5ae_fk_aix_acco` FOREIGN KEY (`prepaid_account_id`) REFERENCES `aix_accountmodel` (`uuid`),
  ADD CONSTRAINT `aix_invoicemodel_unearned_account_id_c55e32dd_fk_aix_acco` FOREIGN KEY (`unearned_account_id`) REFERENCES `aix_accountmodel` (`uuid`);

--
-- Constraints for table `aix_itemfawmodel`
--
ALTER TABLE `aix_itemfawmodel`
  ADD CONSTRAINT `aix_itemfawmodel_entity_id_6ac107b5_fk_aix_entitymodel_uuid` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_itemfawthroughmodel`
--
ALTER TABLE `aix_itemfawthroughmodel`
  ADD CONSTRAINT `aix_itemfawthroughmo_employee_model_id_61a12ca1_fk_aix_emplo` FOREIGN KEY (`employee_model_id`) REFERENCES `aix_employeemodel` (`uuid`),
  ADD CONSTRAINT `aix_itemfawthroughmo_entity_unit_id_65d92892_fk_aix_entit` FOREIGN KEY (`entity_unit_id`) REFERENCES `aix_entityunitmodel` (`uuid`),
  ADD CONSTRAINT `aix_itemfawthroughmo_faw_model_id_e6568dea_fk_aix_emplo` FOREIGN KEY (`faw_model_id`) REFERENCES `aix_employeefawmodel` (`uuid`),
  ADD CONSTRAINT `aix_itemfawthroughmo_parent_id_036645c4_fk_aix_itemf` FOREIGN KEY (`parent_id`) REFERENCES `aix_itemfawthroughmodel` (`uuid`);

--
-- Constraints for table `aix_itemfetmodel`
--
ALTER TABLE `aix_itemfetmodel`
  ADD CONSTRAINT `aix_itemfetmodel_entity_id_6da25cd4_fk_aix_entitymodel_uuid` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_itemfetthroughmodel`
--
ALTER TABLE `aix_itemfetthroughmodel`
  ADD CONSTRAINT `aix_itemfetthroughmo_entity_unit_id_4b04bb90_fk_aix_entit` FOREIGN KEY (`entity_unit_id`) REFERENCES `aix_entityunitmodel` (`uuid`),
  ADD CONSTRAINT `aix_itemfetthroughmo_equipment_model_id_e2ff9dd8_fk_aix_equip` FOREIGN KEY (`equipment_model_id`) REFERENCES `aix_equipmentmodel` (`uuid`),
  ADD CONSTRAINT `aix_itemfetthroughmo_fet_model_id_b4acefe5_fk_aix_equip` FOREIGN KEY (`fet_model_id`) REFERENCES `aix_equipmentfetmodel` (`uuid`),
  ADD CONSTRAINT `aix_itemfetthroughmo_parent_id_64ed8fb9_fk_aix_itemf` FOREIGN KEY (`parent_id`) REFERENCES `aix_itemfetthroughmodel` (`uuid`);

--
-- Constraints for table `aix_itemmodel`
--
ALTER TABLE `aix_itemmodel`
  ADD CONSTRAINT `aix_itemmodel_cogs_account_id_22e05118_fk_aix_acco` FOREIGN KEY (`cogs_account_id`) REFERENCES `aix_accountmodel` (`uuid`),
  ADD CONSTRAINT `aix_itemmodel_earnings_account_id_b4dfecc3_fk_aix_acco` FOREIGN KEY (`earnings_account_id`) REFERENCES `aix_accountmodel` (`uuid`),
  ADD CONSTRAINT `aix_itemmodel_entity_id_69d90b6f_fk_aix_entitymodel_uuid` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_itemmodel_expense_account_id_3920c1f9_fk_aix_acco` FOREIGN KEY (`expense_account_id`) REFERENCES `aix_accountmodel` (`uuid`),
  ADD CONSTRAINT `aix_itemmodel_inventory_account_id_fb982dd1_fk_aix_acco` FOREIGN KEY (`inventory_account_id`) REFERENCES `aix_accountmodel` (`uuid`),
  ADD CONSTRAINT `aix_itemmodel_uom_id_eafbae0d_fk_aix_unitofmeasuremodel_uuid` FOREIGN KEY (`uom_id`) REFERENCES `aix_unitofmeasuremodel` (`uuid`);

--
-- Constraints for table `aix_itemthroughmodel`
--
ALTER TABLE `aix_itemthroughmodel`
  ADD CONSTRAINT `aix_itemthroughmode_bill_model_id_f38801cb_fk_aix_bill` FOREIGN KEY (`bill_model_id`) REFERENCES `aix_billmodel` (`uuid`),
  ADD CONSTRAINT `aix_itemthroughmode_ce_model_id_387b5972_fk_aix_esti` FOREIGN KEY (`ce_model_id`) REFERENCES `aix_estimatemodel` (`uuid`),
  ADD CONSTRAINT `aix_itemthroughmode_entity_unit_id_c024cf30_fk_aix_enti` FOREIGN KEY (`entity_unit_id`) REFERENCES `aix_entityunitmodel` (`uuid`),
  ADD CONSTRAINT `aix_itemthroughmode_invoice_model_id_cc9db523_fk_aix_invo` FOREIGN KEY (`invoice_model_id`) REFERENCES `aix_invoicemodel` (`uuid`),
  ADD CONSTRAINT `aix_itemthroughmode_item_model_id_a331218d_fk_aix_item` FOREIGN KEY (`item_model_id`) REFERENCES `aix_itemmodel` (`uuid`),
  ADD CONSTRAINT `aix_itemthroughmode_jcd_model_id_8854fd0f_fk_aix_work` FOREIGN KEY (`jcd_model_id`) REFERENCES `aix_workorderjobcardmodel` (`uuid`),
  ADD CONSTRAINT `aix_itemthroughmode_parent_id_cc95962e_fk_aix_item` FOREIGN KEY (`parent_id`) REFERENCES `aix_itemthroughmodel` (`uuid`),
  ADD CONSTRAINT `aix_itemthroughmode_po_model_id_8193ad06_fk_aix_purc` FOREIGN KEY (`po_model_id`) REFERENCES `aix_purchaseordermodel` (`uuid`);

--
-- Constraints for table `aix_jobcategorymodel`
--
ALTER TABLE `aix_jobcategorymodel`
  ADD CONSTRAINT `aix_jobcategorymode_entity_id_109e26ef_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_journalentrymodel`
--
ALTER TABLE `aix_journalentrymodel`
  ADD CONSTRAINT `aix_journalentrymod_entity_unit_id_e2544ac0_fk_aix_enti` FOREIGN KEY (`entity_unit_id`) REFERENCES `aix_entityunitmodel` (`uuid`),
  ADD CONSTRAINT `aix_journalentrymod_ledger_id_0083be9c_fk_aix_ledg` FOREIGN KEY (`ledger_id`) REFERENCES `aix_ledgermodel` (`uuid`),
  ADD CONSTRAINT `aix_journalentrymod_parent_id_a17e3690_fk_aix_jour` FOREIGN KEY (`parent_id`) REFERENCES `aix_journalentrymodel` (`uuid`);

--
-- Constraints for table `aix_kpionoffmodel`
--
ALTER TABLE `aix_kpionoffmodel`
  ADD CONSTRAINT `aix_kpionoffmodel_task_id_762a15f5_fk_aix_work` FOREIGN KEY (`task_id`) REFERENCES `aix_workordertaskmodel` (`uuid`);

--
-- Constraints for table `aix_kpiopsmodel`
--
ALTER TABLE `aix_kpiopsmodel`
  ADD CONSTRAINT `aix_kpiopsmodel_equipment_id_4177f6db_fk_aix_assetmodel_uuid` FOREIGN KEY (`equipment_id`) REFERENCES `aix_assetmodel` (`uuid`);

--
-- Constraints for table `aix_kpipobmodel`
--
ALTER TABLE `aix_kpipobmodel`
  ADD CONSTRAINT `aix_kpipobmodel_activity_location_id_52919f19_fk_aix_cust` FOREIGN KEY (`activity_location_id`) REFERENCES `aix_customerlocationmodel` (`uuid`),
  ADD CONSTRAINT `aix_kpipobmodel_task_id_16fe7a38_fk_aix_work` FOREIGN KEY (`task_id`) REFERENCES `aix_workordertaskmodel` (`uuid`);

--
-- Constraints for table `aix_leaverequestactionmodel`
--
ALTER TABLE `aix_leaverequestactionmodel`
  ADD CONSTRAINT `aix_leaverequestact_employee_id_bc5a2f68_fk_aix_empl` FOREIGN KEY (`employee_id`) REFERENCES `aix_employeemodel` (`uuid`),
  ADD CONSTRAINT `aix_leaverequestact_entity_id_65047595_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_leaverequestact_leave_request_id_fef91b98_fk_aix_leav` FOREIGN KEY (`leave_request_id`) REFERENCES `aix_leaverequestmodel` (`uuid`),
  ADD CONSTRAINT `aix_leaverequestact_leave_request_status_76b20aa4_fk_aix_leav` FOREIGN KEY (`leave_request_status_id`) REFERENCES `aix_leaverequeststatusmodel` (`uuid`);

--
-- Constraints for table `aix_leaverequestmodel`
--
ALTER TABLE `aix_leaverequestmodel`
  ADD CONSTRAINT `aix_leaverequestmod_employee_id_c4d4c3c0_fk_aix_empl` FOREIGN KEY (`employee_id`) REFERENCES `aix_employeemodel` (`uuid`),
  ADD CONSTRAINT `aix_leaverequestmod_entity_id_89cdddc0_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_leaverequestmod_leave_request_status_77d49825_fk_aix_leav` FOREIGN KEY (`leave_request_status_id`) REFERENCES `aix_leaverequeststatusmodel` (`uuid`),
  ADD CONSTRAINT `aix_leaverequestmod_supervisor_id_8a5caae3_fk_aix_empl` FOREIGN KEY (`supervisor_id`) REFERENCES `aix_employeemodel` (`uuid`);

--
-- Constraints for table `aix_notificationexternaltypemodel`
--
ALTER TABLE `aix_notificationexternaltypemodel`
  ADD CONSTRAINT `aix_notificationext_entity_id_5810f3c3_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_payrolladvancerequestactionmodel`
--
ALTER TABLE `aix_payrolladvancerequestactionmodel`
  ADD CONSTRAINT `aix_payrolladvancer_employee_id_719747f3_fk_aix_empl` FOREIGN KEY (`employee_id`) REFERENCES `aix_employeemodel` (`uuid`),
  ADD CONSTRAINT `aix_payrolladvancer_entity_id_118ac706_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_payrolladvancer_pa_request_id_dcacb0dd_fk_aix_payr` FOREIGN KEY (`pa_request_id`) REFERENCES `aix_payrolladvancerequestmodel` (`uuid`),
  ADD CONSTRAINT `aix_payrolladvancer_par_status_id_9b0a9fb7_fk_aix_payr` FOREIGN KEY (`par_status_id`) REFERENCES `aix_payrolladvancerequeststatusmodel` (`uuid`);

--
-- Constraints for table `aix_payrolladvancerequestmodel`
--
ALTER TABLE `aix_payrolladvancerequestmodel`
  ADD CONSTRAINT `aix_payrolladvancer_employee_id_a68b50df_fk_aix_empl` FOREIGN KEY (`employee_id`) REFERENCES `aix_employeemodel` (`uuid`),
  ADD CONSTRAINT `aix_payrolladvancer_entity_id_78809a92_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_payrolladvancer_par_status_id_f86b2fba_fk_aix_payr` FOREIGN KEY (`par_status_id`) REFERENCES `aix_payrolladvancerequeststatusmodel` (`uuid`),
  ADD CONSTRAINT `aix_payrolladvancer_supervisor_id_37d10083_fk_aix_empl` FOREIGN KEY (`supervisor_id`) REFERENCES `aix_employeemodel` (`uuid`);

--
-- Constraints for table `aix_requisitionactionmodel`
--
ALTER TABLE `aix_requisitionactionmodel`
  ADD CONSTRAINT `aix_requisitionacti_employee_id_daefa427_fk_aix_empl` FOREIGN KEY (`employee_id`) REFERENCES `aix_employeemodel` (`uuid`),
  ADD CONSTRAINT `aix_requisitionacti_entity_id_bc622321_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_requisitionacti_requisition_id_fb6b8c6d_fk_aix_requ` FOREIGN KEY (`requisition_id`) REFERENCES `aix_requisitionmodel` (`uuid`),
  ADD CONSTRAINT `aix_requisitionacti_requisition_status_i_59f07672_fk_aix_requ` FOREIGN KEY (`requisition_status_id`) REFERENCES `aix_requisitionstatusmodel` (`uuid`);

--
-- Constraints for table `aix_requisitioncategorymodel`
--
ALTER TABLE `aix_requisitioncategorymodel`
  ADD CONSTRAINT `aix_requisitioncate_entity_id_ecd2938f_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_requisitionmodel`
--
ALTER TABLE `aix_requisitionmodel`
  ADD CONSTRAINT `aix_requisitionmode_currency_id_b3ec7191_fk_aix_curr` FOREIGN KEY (`currency_id`) REFERENCES `aix_currencymodel` (`uuid`),
  ADD CONSTRAINT `aix_requisitionmode_employee_id_2542c611_fk_aix_empl` FOREIGN KEY (`employee_id`) REFERENCES `aix_employeemodel` (`uuid`),
  ADD CONSTRAINT `aix_requisitionmode_entity_id_d403b656_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_requisitionmode_requisition_category_40cacbd7_fk_aix_requ` FOREIGN KEY (`requisition_category_id`) REFERENCES `aix_requisitioncategorymodel` (`uuid`),
  ADD CONSTRAINT `aix_requisitionmode_requisition_status_i_23a54b37_fk_aix_requ` FOREIGN KEY (`requisition_status_id`) REFERENCES `aix_requisitionstatusmodel` (`uuid`),
  ADD CONSTRAINT `aix_requisitionmode_supervisor_id_c3834490_fk_aix_empl` FOREIGN KEY (`supervisor_id`) REFERENCES `aix_employeemodel` (`uuid`);

--
-- Constraints for table `aix_routesurveyinfomodel`
--
ALTER TABLE `aix_routesurveyinfomodel`
  ADD CONSTRAINT `aix_routesurveyinfom_entity_id_845efed1_fk_aix_entit` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_routesurveyinfom_route_survey_id_40d6e05b_fk_aix_route` FOREIGN KEY (`route_survey_id`) REFERENCES `aix_routesurveymodel` (`uuid`);

--
-- Constraints for table `aix_routesurveymodel`
--
ALTER TABLE `aix_routesurveymodel`
  ADD CONSTRAINT `aix_routesurveymodel_entity_id_bfe1821d_fk_aix_entitymodel_uuid` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_userallocationmodel`
--
ALTER TABLE `aix_userallocationmodel`
  ADD CONSTRAINT `aix_userallocationm_entity_id_c02ee7d6_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_userallocationm_task_id_b3f2b5e7_fk_aix_work` FOREIGN KEY (`task_id`) REFERENCES `aix_workordertaskmodel` (`uuid`),
  ADD CONSTRAINT `aix_userallocationm_work_order_id_303e1f79_fk_aix_work` FOREIGN KEY (`work_order_id`) REFERENCES `aix_workordermodel` (`uuid`),
  ADD CONSTRAINT `aix_userallocationmodel_allocation_id_09ebd713_fk_auth_user_id` FOREIGN KEY (`allocation_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `aix_workcategorymodel`
--
ALTER TABLE `aix_workcategorymodel`
  ADD CONSTRAINT `aix_workcategorymod_entity_id_b6859eb8_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_workflowtypemodel`
--
ALTER TABLE `aix_workflowtypemodel`
  ADD CONSTRAINT `aix_workflowtypemod_entity_id_475c99ef_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_workorderactivityassetmodel`
--
ALTER TABLE `aix_workorderactivityassetmodel`
  ADD CONSTRAINT `aix_workorderactivit_activity_id_f693742d_fk_aix_worko` FOREIGN KEY (`activity_id`) REFERENCES `aix_workorderactivitymodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderactivit_asset_id_2acfc5a3_fk_aix_asset` FOREIGN KEY (`asset_id`) REFERENCES `aix_assetmodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderactivit_entity_id_947b568f_fk_aix_entit` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_workorderactivitydocumentmodel`
--
ALTER TABLE `aix_workorderactivitydocumentmodel`
  ADD CONSTRAINT `aix_workorderactivit_activity_id_8f6f374e_fk_aix_worko` FOREIGN KEY (`activity_id`) REFERENCES `aix_workorderactivitymodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderactivit_document_id_68318321_fk_aix_docum` FOREIGN KEY (`document_id`) REFERENCES `aix_documentmodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderactivit_entity_id_01164906_fk_aix_entit` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_workorderactivityliftingmodel`
--
ALTER TABLE `aix_workorderactivityliftingmodel`
  ADD CONSTRAINT `aix_workorderactivit_FromLocation_56e819c7_fk_aix_custo` FOREIGN KEY (`FromLocation`) REFERENCES `aix_customerlocationmodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderactivit_ToLocation_65cf694a_fk_aix_custo` FOREIGN KEY (`ToLocation`) REFERENCES `aix_customerlocationmodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderactivit_activity_id_b3983fdf_fk_aix_worko` FOREIGN KEY (`activity_id`) REFERENCES `aix_workorderactivitymodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderactivit_entity_id_f44f5bda_fk_aix_entit` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderactivit_equipment_id_79c9b8d1_fk_aix_asset` FOREIGN KEY (`equipment_id`) REFERENCES `aix_assetmodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderactivit_operator_id_7269b65f_fk_aix_emplo` FOREIGN KEY (`operator_id`) REFERENCES `aix_employeemodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderactivit_supervisor_id_7a8eb3fa_fk_aix_emplo` FOREIGN KEY (`supervisor_id`) REFERENCES `aix_employeemodel` (`uuid`);

--
-- Constraints for table `aix_workorderactivityliftingmodel_operators`
--
ALTER TABLE `aix_workorderactivityliftingmodel_operators`
  ADD CONSTRAINT `aix_workorderactivit_employeemodel_id_5a62d27e_fk_aix_emplo` FOREIGN KEY (`employeemodel_id`) REFERENCES `aix_employeemodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderactivit_workorderactivitylif_ebeef5b1_fk_aix_worko` FOREIGN KEY (`workorderactivityliftingmodel_id`) REFERENCES `aix_workorderactivityliftingmodel` (`uuid`);

--
-- Constraints for table `aix_workorderactivitymodel`
--
ALTER TABLE `aix_workorderactivitymodel`
  ADD CONSTRAINT `aix_workorderactivit_FromLocation_23df7c2f_fk_aix_custo` FOREIGN KEY (`FromLocation`) REFERENCES `aix_customerlocationmodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderactivit_ToLocation_b30bd43f_fk_aix_custo` FOREIGN KEY (`ToLocation`) REFERENCES `aix_customerlocationmodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderactivit_entity_id_4e48fc04_fk_aix_entit` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderactivit_task_id_c6049b12_fk_aix_worko` FOREIGN KEY (`task_id`) REFERENCES `aix_workordertaskmodel` (`uuid`);

--
-- Constraints for table `aix_workorderactivitypersonnelmodel`
--
ALTER TABLE `aix_workorderactivitypersonnelmodel`
  ADD CONSTRAINT `aix_workorderactivit_activity_id_10f5727a_fk_aix_worko` FOREIGN KEY (`activity_id`) REFERENCES `aix_workorderactivitymodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderactivit_employee_id_99cddfb1_fk_aix_emplo` FOREIGN KEY (`employee_id`) REFERENCES `aix_employeemodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderactivit_entity_id_6c543d8a_fk_aix_entit` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_workorderactivitytransportmodel`
--
ALTER TABLE `aix_workorderactivitytransportmodel`
  ADD CONSTRAINT `aix_workorderactivit_FromLocation_ad626162_fk_aix_custo` FOREIGN KEY (`FromLocation`) REFERENCES `aix_customerlocationmodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderactivit_ToLocation_9695cc9c_fk_aix_custo` FOREIGN KEY (`ToLocation`) REFERENCES `aix_customerlocationmodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderactivit_activity_id_03e2ce19_fk_aix_worko` FOREIGN KEY (`activity_id`) REFERENCES `aix_workorderactivitymodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderactivit_driver_id_6cb0184a_fk_aix_emplo` FOREIGN KEY (`driver_id`) REFERENCES `aix_employeemodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderactivit_entity_id_38759014_fk_aix_entit` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderactivit_vehicle_id_0c2bb572_fk_aix_asset` FOREIGN KEY (`vehicle_id`) REFERENCES `aix_assetmodel` (`uuid`);

--
-- Constraints for table `aix_workorderactivitytransportmodel_assistants`
--
ALTER TABLE `aix_workorderactivitytransportmodel_assistants`
  ADD CONSTRAINT `aix_workorderactivit_employeemodel_id_3904677d_fk_aix_emplo` FOREIGN KEY (`employeemodel_id`) REFERENCES `aix_employeemodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderactivit_workorderactivitytra_50c09235_fk_aix_worko` FOREIGN KEY (`workorderactivitytransportmodel_id`) REFERENCES `aix_workorderactivitytransportmodel` (`uuid`);

--
-- Constraints for table `aix_workorderassetmodel`
--
ALTER TABLE `aix_workorderassetmodel`
  ADD CONSTRAINT `aix_workorderassetm_asset_id_2b2d5ce0_fk_aix_asse` FOREIGN KEY (`asset_id`) REFERENCES `aix_assetmodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderassetm_entity_id_1b4b2efc_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderassetm_work_order_id_816a8972_fk_aix_work` FOREIGN KEY (`work_order_id`) REFERENCES `aix_workordermodel` (`uuid`);

--
-- Constraints for table `aix_workorderjobcardmodel`
--
ALTER TABLE `aix_workorderjobcardmodel`
  ADD CONSTRAINT `aix_workorderjobcar_entity_id_d2ecbf5d_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderjobcar_handler_id_26c54de0_fk_aix_empl` FOREIGN KEY (`handler_id`) REFERENCES `aix_employeemodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderjobcar_work_order_id_f4bb71eb_fk_aix_work` FOREIGN KEY (`work_order_id`) REFERENCES `aix_workordermodel` (`uuid`);

--
-- Constraints for table `aix_workorderjobcardstatusmodel`
--
ALTER TABLE `aix_workorderjobcardstatusmodel`
  ADD CONSTRAINT `aix_workorderjobcar_entity_id_45ebb5e2_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderjobcar_jobcard_id_f997ba50_fk_aix_work` FOREIGN KEY (`jobcard_id`) REFERENCES `aix_workorderjobcardmodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderjobcar_status_id_c402eeaa_fk_aix_work` FOREIGN KEY (`status_id`) REFERENCES `aix_workorderstatusmodel` (`uuid`);

--
-- Constraints for table `aix_workordermodel`
--
ALTER TABLE `aix_workordermodel`
  ADD CONSTRAINT `aix_workordermodel_category_id_ca4c793e_fk_aix_work` FOREIGN KEY (`category_id`) REFERENCES `aix_workcategorymodel` (`uuid`),
  ADD CONSTRAINT `aix_workordermodel_currency_id_641e96f1_fk_aix_curr` FOREIGN KEY (`currency_id`) REFERENCES `aix_currencymodel` (`uuid`),
  ADD CONSTRAINT `aix_workordermodel_customer_id_e14465c4_fk_aix_cust` FOREIGN KEY (`customer_id`) REFERENCES `aix_customermodel` (`uuid`),
  ADD CONSTRAINT `aix_workordermodel_entity_id_132a7231_fk_aix_entitymodel_uuid` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_workordermodel_wo_type_id_09952eeb_fk_aix_work` FOREIGN KEY (`wo_type_id`) REFERENCES `aix_workordertypemodel` (`uuid`);

--
-- Constraints for table `aix_workorderpersonnelmodel`
--
ALTER TABLE `aix_workorderpersonnelmodel`
  ADD CONSTRAINT `aix_workorderperson_employee_id_4d47f560_fk_aix_empl` FOREIGN KEY (`employee_id`) REFERENCES `aix_employeemodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderperson_entity_id_8d81b882_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_workorderperson_work_order_id_4316f4eb_fk_aix_work` FOREIGN KEY (`work_order_id`) REFERENCES `aix_workordermodel` (`uuid`);

--
-- Constraints for table `aix_workorderstatusmodel`
--
ALTER TABLE `aix_workorderstatusmodel`
  ADD CONSTRAINT `aix_workorderstatus_entity_id_8f275e90_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `aix_workordertaskassetmodel`
--
ALTER TABLE `aix_workordertaskassetmodel`
  ADD CONSTRAINT `aix_workordertaskas_asset_id_6d2b8a28_fk_aix_asse` FOREIGN KEY (`asset_id`) REFERENCES `aix_assetmodel` (`uuid`),
  ADD CONSTRAINT `aix_workordertaskas_entity_id_c1e2a759_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_workordertaskas_task_id_0ebf9eec_fk_aix_work` FOREIGN KEY (`task_id`) REFERENCES `aix_workordertaskmodel` (`uuid`);

--
-- Constraints for table `aix_workordertaskmodel`
--
ALTER TABLE `aix_workordertaskmodel`
  ADD CONSTRAINT `aix_workordertaskmo_EndLocation_78739987_fk_aix_cust` FOREIGN KEY (`EndLocation`) REFERENCES `aix_customerlocationmodel` (`uuid`),
  ADD CONSTRAINT `aix_workordertaskmo_StartLocation_3578751f_fk_aix_cust` FOREIGN KEY (`StartLocation`) REFERENCES `aix_customerlocationmodel` (`uuid`),
  ADD CONSTRAINT `aix_workordertaskmo_entity_id_790a25ec_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_workordertaskmo_work_order_id_1aeef779_fk_aix_work` FOREIGN KEY (`work_order_id`) REFERENCES `aix_workordermodel` (`uuid`);

--
-- Constraints for table `aix_workordertaskpersonnelmodel`
--
ALTER TABLE `aix_workordertaskpersonnelmodel`
  ADD CONSTRAINT `aix_workordertaskpe_employee_id_f84adda6_fk_aix_empl` FOREIGN KEY (`employee_id`) REFERENCES `aix_employeemodel` (`uuid`),
  ADD CONSTRAINT `aix_workordertaskpe_entity_id_ff08c710_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`),
  ADD CONSTRAINT `aix_workordertaskpe_task_id_b8caebad_fk_aix_work` FOREIGN KEY (`task_id`) REFERENCES `aix_workordertaskmodel` (`uuid`);

--
-- Constraints for table `aix_workordertypemodel`
--
ALTER TABLE `aix_workordertypemodel`
  ADD CONSTRAINT `aix_workordertypemo_entity_id_1d76fb91_fk_aix_enti` FOREIGN KEY (`entity_id`) REFERENCES `aix_entitymodel` (`uuid`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
