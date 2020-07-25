--
-- PostgreSQL database dump
--

-- Dumped from database version 12.3
-- Dumped by pg_dump version 12.3

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

--
-- Name: update_datetime(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.update_datetime() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    NEW.updated_date = timezone('utc'::text, now());
    RETURN NEW;   
END;
$$;


ALTER FUNCTION public.update_datetime() OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: category; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.category (
    category_id integer NOT NULL,
    category_name character varying(50),
    city_id character varying(50)
);


ALTER TABLE public.category OWNER TO postgres;

--
-- Name: category_category_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.category_category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.category_category_id_seq OWNER TO postgres;

--
-- Name: category_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.category_category_id_seq OWNED BY public.category.category_id;


--
-- Name: city; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.city (
    city_id character varying(50) NOT NULL,
    city_name character varying(50),
    country character varying(30)
);


ALTER TABLE public.city OWNER TO postgres;

--
-- Name: merchant; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.merchant (
    username character varying(50) NOT NULL,
    firstname character varying(30),
    lastname character varying(100),
    city_id character varying(50),
    country character varying(30),
    phone character varying(10),
    location character varying(50),
    email character varying(50)
);


ALTER TABLE public.merchant OWNER TO postgres;

--
-- Name: product; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.product (
    product_id integer NOT NULL,
    product_name character varying(30),
    product_desc character varying(80),
    city_id character varying(50) NOT NULL,
    username character varying(50) NOT NULL,
    category_id integer,
    category_name character varying(50),
    created_date timestamp without time zone DEFAULT timezone('utc'::text, now()),
    updated_date timestamp without time zone DEFAULT timezone('utc'::text, now()),
    price real,
    active boolean,
    merchant_name character varying(80),
    merchant_location character varying(50),
    merchant_phone character varying(10),
    product_image bytea,
    product_condition character varying(30)
);


ALTER TABLE public.product OWNER TO postgres;

--
-- Name: product_product_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.product_product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.product_product_id_seq OWNER TO postgres;

--
-- Name: product_product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.product_product_id_seq OWNED BY public.product.product_id;


--
-- Name: category category_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category ALTER COLUMN category_id SET DEFAULT nextval('public.category_category_id_seq'::regclass);


--
-- Name: product product_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product ALTER COLUMN product_id SET DEFAULT nextval('public.product_product_id_seq'::regclass);


--
-- Name: category category_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category
    ADD CONSTRAINT category_pkey PRIMARY KEY (category_id);


--
-- Name: city city_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.city
    ADD CONSTRAINT city_pkey PRIMARY KEY (city_id);


--
-- Name: merchant merchant_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.merchant
    ADD CONSTRAINT merchant_pkey PRIMARY KEY (username);


--
-- Name: product product_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pkey PRIMARY KEY (product_id);


--
-- Name: product product_update_datetime; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER product_update_datetime BEFORE UPDATE ON public.product FOR EACH ROW EXECUTE FUNCTION public.update_datetime();


--
-- Name: product fk_category; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT fk_category FOREIGN KEY (category_id) REFERENCES public.category(category_id);


--
-- Name: category fk_city; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category
    ADD CONSTRAINT fk_city FOREIGN KEY (city_id) REFERENCES public.city(city_id);


--
-- Name: merchant fk_city; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.merchant
    ADD CONSTRAINT fk_city FOREIGN KEY (city_id) REFERENCES public.city(city_id);


--
-- Name: product fk_city; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT fk_city FOREIGN KEY (city_id) REFERENCES public.city(city_id);


--
-- Name: product fk_username; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT fk_username FOREIGN KEY (username) REFERENCES public.merchant(username);


--
-- PostgreSQL database dump complete
--

