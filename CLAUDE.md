# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a WhatsApp AI booking agent system for beauty salons, barbershops, and appointment-based services. The project is being built from scratch using FastAPI, Redis, OpenAI APIs, and other modern technologies to replicate an existing n8n workflow. The system handles automated appointment booking, cancellation, rescheduling, and customer service through WhatsApp Business API.

## Technology Stack

- **Backend**: FastAPI (Python)
- **Database**: Redis for session management, Airtable for data storage
- **AI Services**: OpenAI GPT-4, OpenAI Whisper (audio), OpenAI Vision (images), Google Gemini (backup)
- **External APIs**: WhatsApp Business API (Wasender/360messenger), Google Calendar API
- **Languages**: Python (primary)

## System Architecture

The system follows an agent-based architecture with specialized AI agents:

### Core Agents
- **Intent Recognition Agent**: Routes messages to appropriate specialized agents
- **Booking Agent**: Handles new appointment scheduling and availability checking
- **Cancellation Agent**: Manages appointment cancellations
- **Update Agent**: Processes appointment modifications and rescheduling
- **General Inquiry Agent**: Handles customer service and information requests

### Key Components
- **Multi-modal Processing**: Handles text, voice messages, images, and documents
- **Calendar Integration**: Real-time Google Calendar sync for availability
- **Session Management**: Redis-based conversation state persistence
- **Database Operations**: Airtable integration for appointments, services, and configuration

## Data Models

### Services Catalog (CSV structure reference: `nailServices.csv`)
- ServiceName, Description, Price, DurationMinutes, Category

### Bookings (CSV structure reference: `nailBookings.csv`)
- Name, Phone Number, starttime, endtime, eventId, Service, Status, Notes

### Configuration (CSV structure reference: `nailConfiguration.csv`)
- Setting, SalonName, Address, PhoneNumber, Hours, CancellationPolicy, GoogleReviewLink

## Development Commands

*Note: This project is new and commands will be added as the codebase develops*

### When implementing, you'll likely need:
```bash
# Install dependencies
pip install fastapi uvicorn openai google-calendar-api redis airtable-python-wrapper

# Run development server
uvicorn app:app --reload

# Run tests (when implemented)
pytest

# Environment setup
# Create .env file with API keys for WhatsApp, OpenAI, Google Calendar, etc.
```

## Key Implementation Guidelines

### Agent Development
- Each agent should be stateless with shared memory through Redis
- Implement proper error handling and fallback responses
- Use structured prompts for consistent AI behavior
- Maintain conversation context across multi-turn interactions

### Message Processing Flow
1. WhatsApp webhook receives message
2. Media processing (if audio/image/document)
3. Intent classification using OpenAI
4. Route to appropriate specialized agent
5. Process business logic (calendar, database operations)
6. Generate and send response via WhatsApp API

### External Integrations
- **WhatsApp Business API**: Webhook handling, message sending/receiving
- **Google Calendar**: Availability checking, appointment creation/modification
- **Airtable**: Customer data, appointments, service catalog, configuration
- **OpenAI APIs**: Text processing, vision, audio transcription
- **Redis**: Session storage, message queuing

### Security Considerations
- Validate WhatsApp webhook signatures
- Never log or expose customer personal information
- Implement rate limiting for API calls
- Secure storage of API keys and credentials

## Reference Materials

The `Whatsapp-agent-bot-tutorial/` directory contains:
- Complete n8n workflow JSON with 200+ nodes
- Sample data structures (CSV files)
- Error handling patterns
- Detailed PDF tutorial with setup instructions

Use these files to understand the expected behavior and data flow when implementing the FastAPI version.