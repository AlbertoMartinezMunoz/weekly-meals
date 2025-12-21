# System Design

## Introduction

## System Context

The Meal Planner application is a web-based system that allows a user to create and manage a weekly meal plan using a web form. Once the plan is completed, the system formats the information and sends it to a set of remote users through an external messaging service (e.g., WhatsApp). Remote users can also view the plans by logging into the web application.

The diagram below shows the system boundaries and its interactions with external actors. The Meal Planner User interacts directly with the web application to define the meal schedule, while remote users receive the final plan as a message and do not interact with the system directly. Message delivery is delegated to an external messaging platform, which abstracts communication details and enables reliable distribution of the meal plan.

**Meal Planning Application - System Context Diagram**

![Image cannot be displayed](../c4/1-c4-system-context.svg "Meal Planning Application - System Context Diagram")

This C4 Context diagram illustrates the high-level system landscape for the Meal Planning Application. The diagram shows two primary user roles: the Meal Planner who creates and manages weekly meal plans through a web interface, and Remote Users who receive and view these plans. The core Meal Planning Application integrates with several external systems for distributing meal plans. Communication between different users and the application occurs over HTTPS, ensuring secure data transmission.

## High-Level Architecture

The Meal Planner application is composed of several containers, each with a clearly defined responsibility. The Web Frontend provides the user interface and web form used to create and manage weekly meal plans. It communicates with the Backend Application through a RESTful API over HTTPS.

The Backend Application, implemented in Python, contains the core business logic of the system. It validates meal plans, persists data to the database, and coordinates the delivery of meal plans to remote users. Meal plans, user information, and delivery status are stored in a relational database to ensure persistence and traceability.

Message delivery is handled by a dedicated Message Sender container, which encapsulates integration with an external messaging service such as WhatsApp. This separation isolates third-party dependencies from the core application and allows message delivery to be implemented synchronously or asynchronously. Remote users receive the weekly meal plan through the external messaging platform and do not interact directly with the application.

**Meal Planning Application - Container Diagram**

![Image cannot be displayed](../c4/2-c4-container.svg "Meal Planning Application - Container Diagram")

This diagram shows the high-level runtime containers that make up the Meal Planner application, including the web frontend, backend services, persistence layer, and messaging integration, as well as their interactions with users and external systems

Below is a **Component Design** section you can drop directly into your system design document.
It follows naturally from the **C4 Container diagram** and stays at the right level of detail for a design doc (clear responsibilities, interfaces, and boundaries—without turning into code).

## Component Design

### Overview

This section describes the internal components of the Meal Planner application and how responsibilities are distributed within each container. The goal of this decomposition is to keep the system modular, testable, and easy to evolve, while clearly separating user interface concerns, business logic, persistence, and external integrations.

The component design focuses primarily on the **Backend Application**, as it contains the core business logic of the system.

### Web Frontend

The Web Frontend is responsible for user interaction and presentation. It does not contain business logic beyond basic input validation.

### Backend Application

The Backend Application contains the core business logic and orchestration of the system.

### Database

The Database is the persistence layer.

### Message Sender

The Message Sender container encapsulates all messaging-related logic and external dependencies.

**Main components:**

* **Message Formatter**

  * Converts a weekly meal plan into a human-readable message
* **Messaging Client**

  * Handles communication with the external messaging API (e.g., WhatsApp)
* **Retry & Error Handler**

  * Manages retries, failures, and logging of delivery issues

**Responsibilities:**

* Format messages consistently
* Handle external API communication
* Provide resilience against transient failures

### Component Interaction Summary

At a high level, component interactions follow this flow:

1. The user submits a weekly meal plan via the Web Frontend.
2. The API Layer receives and validates the request.
3. The Domain Layer applies business rules and stores the plan via the Persistence Layer.
4. The Notification Service triggers message delivery.
5. The Message Sender formats and sends the plan using the external messaging service.
6. Delivery status is stored for tracking and troubleshooting.

