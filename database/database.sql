--
-- PostgreSQL database dump
--

-- Dumped from database version 13.5 (Raspbian 13.5-0+deb11u1)
-- Dumped by pg_dump version 13.5 (Raspbian 13.5-0+deb11u1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: medicine1; Type: TABLE; Schema: public; Owner: pi
--

CREATE TABLE public.medicine1 (
    id integer NOT NULL,
    medname character varying,
    datefilled character varying,
    quantity character varying,
    refillsleft character varying,
    imagepath character varying,
    folderpath character varying,
    timesperday character varying,
    timesperweek character varying,
    refilldate character varying
);


ALTER TABLE public.medicine1 OWNER TO pi;

--
-- Name: medicines; Type: TABLE; Schema: public; Owner: pi
--

CREATE TABLE public.medicines (
    id integer,
    name character varying
);


ALTER TABLE public.medicines OWNER TO pi;

--
-- Name: reminders; Type: TABLE; Schema: public; Owner: pi
--

CREATE TABLE public.reminders (
    id integer NOT NULL,
    medid integer NOT NULL,
    remindertime character varying,
    finalreminderdate character varying
);


ALTER TABLE public.reminders OWNER TO pi;

--
-- Name: reportmetrics; Type: TABLE; Schema: public; Owner: pi
--

CREATE TABLE public.reportmetrics (
    id integer NOT NULL,
    medid integer NOT NULL,
    reminderid integer NOT NULL,
    timetaken character varying,
    askedaftertakencount character varying,
    askedbeforetakencount character varying,
    date integer
);


ALTER TABLE public.reportmetrics OWNER TO pi;

--
-- Data for Name: medicine1; Type: TABLE DATA; Schema: public; Owner: pi
--

COPY public.medicine1 (id, medname, datefilled, quantity, refillsleft, imagepath, folderpath, timesperday, timesperweek, refilldate) FROM stdin;
1	MedicineNameNone	not found..!	99	9	FolderPathNone	/home/pi/Desktop/EVA/capturedImages/pillbottle1	\N	\N	\N
2	MedicineNameNone	not found..!	99	9	FolderPathNone	/home/pi/Desktop/EVA/capturedImages/pillbottle2	\N	\N	\N
3	MedicineNameNone	not found..!	5	9	FolderPathNone	/home/pi/Desktop/EVA/capturedImages/pillbottle3	\N	\N	\N
4	MedicineNameNone	not found..!	99	9	FolderPathNone	/home/pi/Desktop/EVA/capturedImages/pillbottle4	\N	\N	\N
5	MedicineNameNone	not found..!	30	9	FolderPathNone	/home/pi/Desktop/EVA/capturedImages/pillbottle5	\N	\N	\N
6	MedicineNameNone	not found..!	2	9	FolderPathNone	/home/pi/Desktop/EVA/capturedImages/pillbottle6	\N	\N	\N
7	MedicineNameNone	not found..!	30	9	FolderPathNone	/home/pi/Desktop/EVA/capturedImages/pillbottle7	\N	\N	\N
8	ROSUVASTATIN	2022-04-01 00:00:00	30	9	/home/pi/Desktop/EVA/capturedImages/pillbottle8/Image1.png	/home/pi/Desktop/EVA/capturedImages/pillbottle8	\N	\N	\N
9	docusate sodium 100 MG capsule	not found..!	7390	9	/home/pi/Desktop/EVA/capturedImages/pillbottle9/Image1.png	/home/pi/Desktop/EVA/capturedImages/pillbottle9	\N	\N	\N
10	ROSUVASTATIN	6/2/22	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle4/Image4.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle4	1	\N	\N
11	Cyclobenzaprine	not found..!	fgg	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle5/Image2.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle5	not found	\N	\N
12	ROSUVASTATIN	6/2/22	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle6/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle6	1	\N	\N
13	ROSUVASTATIN	6/2/22	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle7/Image2.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle7	1	\N	\N
14	Ibuprofen Tablet	not found..!	not found	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle8/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle8	not found	\N	\N
15	ROSUVASTATIN	6/2/22	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle9/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle9	1	\N	\N
16	Ibuprofen Tablet	not found..!	not found	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle10/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle10	not found	\N	\N
17	ROSUVASTATIN	6/2/22	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle11/Image2.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle11	1	\N	\N
18	ROSUVASTATIN	6/2/22	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle12/Image2.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle12	1	\N	\N
19	ROSUVASTATIN	6/2/22	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle13/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle13	1	\N	\N
20	ROSUVASTATIN	6/2/22	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle14/Image2.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle14	1	\N	\N
21	not found	sddffgghj	not found	not found	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle15	not found	\N	\N
22	Tamsulosin Hcl	11/03/2021	90	3	/home/pi/Desktop/EVA/expoEva-main/pillbottle16/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle16	1	\N	\N
23	not found	asrd	not found	not found	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle17	not found	\N	\N
24	not found	not found..!	not found	not found	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle18	not found	\N	\N
25	not found	not found..!	not found	not found	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle19	not found	\N	\N
26	Docusate sodium	not found..!	1	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle20/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle20	not found	\N	\N
38	ROSUVASTATIN	6/2/22	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle32/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle32	1	\N	\N
27	Docusate sodium	agfytd	not found	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle21/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle21	not found	\N	\N
28	not found	not found..!	not found	not found	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle22	not found	\N	\N
29	Docusate sodium	not found..!	not found	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle23/Image2.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle23	not found	\N	\N
30	not found	not found..!	not found	not found	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle24	not found	\N	\N
31	ROSUVASTATIN	6/2/22	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle25/Image2.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle25	1	\N	\N
32	Tamsulosin Hcl	11/03/2021	90	3	/home/pi/Desktop/EVA/expoEva-main/pillbottle26/Image3.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle26	1	\N	\N
33	not found	not found..!	not found	not found	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle27	not found	\N	\N
34	not found	not found..!	not found	not found	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle28	not found	\N	\N
35	ROSUVASTATIN	6/2/22	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle29/Image3.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle29	1	\N	\N
36	Ibuprofen Tablet	not found..!	not found	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle30/Image3.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle30	not found	\N	\N
37	ROSUVASTATIN	6/2/22	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle31/Image2.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle31	1	\N	\N
39	ROSUVASTATIN	6/2/22	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle33/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle33	1	\N	\N
40	ROSUVASTATIN	6/2/22	30	4	/home/pi/Desktop/EVA/expoEva-main/pillbottle34/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle34	1	\N	\N
41	ROSUVASTATIN	6/2/22	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle35/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle35	2	\N	\N
42	ROSUVASTATIN	6/2/22	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle36/Image2.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle36	2	\N	\N
43	ROSUVASTATIN	6/2/22	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle37/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle37	2	\N	\N
44	ROSUVASTATIN	6/2/22	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle38/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle38	1	\N	\N
45	ROSUVASTATIN	6/2/22	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle39/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle39	2	\N	\N
46	ROSUVASTATIN	6/2/22	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle40/Image2.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle40	2	\N	\N
47	Ibuprofen Tablet	not found..!	7	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle41/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle41	not found	\N	\N
48	ROSUVASTATIN	6/2/22	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle42/Image2.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle42	1	\N	\N
49	metroNIDAZOLE	03/11/2022	30	0	/home/pi/Desktop/EVA/expoEva-main/pillbottle43/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle43	3	\N	\N
50	Ibuprofen Tablet	not found..!	not found	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle44/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle44	not found	\N	\N
51	Tamsulosin Hcl	11/03/2021	90	3	/home/pi/Desktop/EVA/expoEva-main/pillbottle45/Image2.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle45	1	\N	\N
52	METFORMIN HCL	not found..!	not found	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle46/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle46	not found	\N	\N
53	Ibuprofen Tablet	not found..!	not found	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle47/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle47	not found	\N	\N
54	METFORMIN HCL	01/04/2022	180	1	/home/pi/Desktop/EVA/expoEva-main/pillbottle48/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle48	2	\N	\N
55	ROSUVASTATIN	6/2/22	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle49/Image2.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle49	1	\N	\N
56	metroNIDAZOLE	03/11/2022	30	0	/home/pi/Desktop/EVA/expoEva-main/pillbottle50/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle50	3	\N	\N
57	Tamsulosin Hcl	11/03/2021	90	3	/home/pi/Desktop/EVA/expoEva-main/pillbottle51/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle51	1	\N	\N
58	Ciprofloxacin	03/11/2022	20	0	/home/pi/Desktop/EVA/expoEva-main/pillbottle52/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle52	2	\N	\N
59	ROSUVASTATIN	uffggllkk	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle53/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle53	1	\N	\N
60	ROSUVASTATIN	6/2/22	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle54/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle54	1	\N	\N
61	ROSUVASTATIN	6/2/22	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle55/Image3.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle55	1	\N	\N
62	ROSUVASTATIN	6/2/22	30	ggv	/home/pi/Desktop/EVA/expoEva-main/pillbottle56/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle56	1	\N	\N
63	metroNIDAZOLE	03/11/2022	30	0	/home/pi/Desktop/EVA/expoEva-main/pillbottle57/Image2.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle57	3	\N	\N
64	METFORMIN HCL	01/04/2022	180	ffvb	/home/pi/Desktop/EVA/expoEva-main/pillbottle58/Image2.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle58	2	\N	\N
65	ROSUVASTATIN	06/02/21	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle59/Image2.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle59	1	\N	\N
66	Tamsulosin Hcl	11/03/2021	90	3	/home/pi/Desktop/EVA/expoEva-main/pillbottle60/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle60	1	\N	\N
67	Tamsulosin Hcl	11/03/2021	90	3	/home/pi/Desktop/EVA/expoEva-main/pillbottle61/Image3.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle61	1	\N	\N
68	Tamsulosin Hcl	11/03/2021	90	3	/home/pi/Desktop/EVA/expoEva-main/pillbottle62/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle62	1	\N	\N
69	Ibuprofen Tablet	not found..!	cdfym	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle63/Image3.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle63	not found	\N	\N
70	Ciprofloxacin	03/11/2022	20	0	/home/pi/Desktop/EVA/expoEva-main/pillbottle64/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle64	2	\N	\N
71	ROSUVASTATIN	6/2/22	30	5	/home/pi/Desktop/EVA/expoEva-main/pillbottle65/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle65	1	\N	\N
72	Tamsulosin Hcl	11/03/2021	90	3	/home/pi/Desktop/EVA/expoEva-main/pillbottle66/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle66	1	\N	\N
73		11/03/2021	90	2	/home/pi/Desktop/EVA/expoEva-main/pillbottle67/Image1.png	/home/pi/Desktop/EVA/expoEva-main/pillbottle67	1	\N	\N
74	not found	not found..!	not found	not found	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle68	not found	\N	\N
75	not found	not found..!	not found	not found	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle69	not found	\N	\N
76	not found	not found..!	not found	not found	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle70	not found	\N	\N
77	not found	not found..!	not found	not found	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle71	not found	\N	\N
78	not found	not found..!	not found	not found	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle72	not found	\N	\N
79	not found	not found..!	not found	not found	not found	/home/pi/Desktop/EVA/expoEva-main/pillbottle74	not found	\N	\N
\.


--
-- Data for Name: medicines; Type: TABLE DATA; Schema: public; Owner: pi
--

COPY public.medicines (id, name) FROM stdin;
1	ROSUVASTATIN
2	Tamsulosin Hcl
3	Cyclobenzaprine
4	Docusate sodium
5	Ibuprofen Tablet
6	Ciprofloxacin
7	metroNIDAZOLE
8	METFORMIN HCL
\.


--
-- Data for Name: reminders; Type: TABLE DATA; Schema: public; Owner: pi
--

COPY public.reminders (id, medid, remindertime, finalreminderdate) FROM stdin;
\.


--
-- Data for Name: reportmetrics; Type: TABLE DATA; Schema: public; Owner: pi
--

COPY public.reportmetrics (id, medid, reminderid, timetaken, askedaftertakencount, askedbeforetakencount, date) FROM stdin;
\.


--
-- Name: medicine1 medicine1_pkey; Type: CONSTRAINT; Schema: public; Owner: pi
--

ALTER TABLE ONLY public.medicine1
    ADD CONSTRAINT medicine1_pkey PRIMARY KEY (id);


--
-- Name: reminders reminders_pkey; Type: CONSTRAINT; Schema: public; Owner: pi
--

ALTER TABLE ONLY public.reminders
    ADD CONSTRAINT reminders_pkey PRIMARY KEY (id);


--
-- Name: reportmetrics reportmetrics_pkey; Type: CONSTRAINT; Schema: public; Owner: pi
--

ALTER TABLE ONLY public.reportmetrics
    ADD CONSTRAINT reportmetrics_pkey PRIMARY KEY (id);


--
-- Name: reminders reminders_medid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: pi
--

ALTER TABLE ONLY public.reminders
    ADD CONSTRAINT reminders_medid_fkey FOREIGN KEY (medid) REFERENCES public.medicine1(id);


--
-- Name: reportmetrics reportmetrics_medid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: pi
--

ALTER TABLE ONLY public.reportmetrics
    ADD CONSTRAINT reportmetrics_medid_fkey FOREIGN KEY (medid) REFERENCES public.medicine1(id);


--
-- Name: reportmetrics reportmetrics_reminderid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: pi
--

ALTER TABLE ONLY public.reportmetrics
    ADD CONSTRAINT reportmetrics_reminderid_fkey FOREIGN KEY (reminderid) REFERENCES public.reminders(id);


--
-- PostgreSQL database dump complete
--

